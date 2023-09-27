# LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

Follow up:
Could you do both operations in O(1) time complexity?

## Example

```text
LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

看到O(1)，首先想到的是用dict。一开始想的是构建一个key_val_dict，然后访问key的时候得val；然后构建一个key_freq_dict，访问key的时候得frequency；然后构建一个freq_key_dict，访问freq的时候得到同一个frequency下访问过的key的list，用以判断哪个是最近最少使用的key（p.s. 我总觉得这个最近最少读起来真的很恶心，是不是我的语文理解能力有问题？总觉得应该描述为最早最少）。
然后一顿操作下来，把自己烦死了。时间关系，就参考了一下题解和评论有没有用类似我这种思路解决问题的，确实还是有的。如果用我一开始的这种构建dict的做法，肯定还是做得出来的，但是会多很多不必要的麻烦，然后把自己作死。

本题关键思路：按照题意直接用dict暴力解决，这个dict的key就是输入的key，然而对应这个key的value就包装在了一个list里面，[value, frequency, time]，frequency就是访问过的次数，time这里指的是对这个Cache访问操作了第几次。关键就是这个time了，这里是为了方便的找到哪个key是最少使用的里面，最早使用的那个。如果我们每get一次，或者put一次，都给这个time+=1，那time小的就是最早的那个了。

```python
class LFUCache:
    # 根据上述解释，这里就把dict命名为freq，方便记忆，也就是key对应val_freq_time的list的意思
    def __init__(self, capacity: int):
        self.freq = {}
        self.capacity = capacity
        self.__time = 0
    # get相对简单，如果key不在这个dict里面，返回-1
    # 如果在的话，我们返回key所对应的list中的第0个也就是value，然后第1个也就是frequency就要+1，第2个也就time就更新为本次get操作的time
    def get(self, key: int) -> int:
        self.__time += 1
        if key in self.freq:
            self.freq[key][1] += 1
            self.freq[key][2] = self.__time
            return self.freq[key][0]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        self.__time += 1
        # 这里题目没说capacity不可以是0，把这个删掉的话，0的用例就会错
        if self.capacity == 0:
            return None
        # 首先考虑如果key已经存在，那就更新key对应的value，并且key的访问次数+1，key的访问time更新
        if key in self.freq:
            self.freq[key][0] = value
            self.freq[key][1] += 1
            self.freq[key][2] = self.__time
        else:
            # 如果key第一次见，当dict的大小还小于capacity的话，就直接给dict插入新元素
            if len(self.freq) < self.capacity:
                self.freq[key] = [value, 0, self.__time]
            else:
                # 如果不够放了，那我们就按题意先找访问次数最少的freq能有多少
                min_freq = self.freq[min(self.freq, key=lambda x: self.freq[x][1])][1]
                # 然后我们找出访问次数为最少的都有哪些key，并放在一个新的dict里面
                min_key_dict = {}
                for k in self.freq:
                    if self.freq[k][1] == min_freq:
                        min_key_dict[k] = self.freq[k]
                # 然后我们找出这些访问最少的key，最早访问的key值是多少，然后就把原dict的这个key删掉
                min_time_key = min(min_key_dict, key=lambda x: min_key_dict[x][2])
                self.freq.pop(min_time_key)
            # 删完就可以放心的key了
            self.freq[key] = [value, 0, self.__time]

```

再来一个：

```python
from collections import defaultdict, OrderedDict
class Node():
    def __init__(self, key=-1, val=-1, count=-1):
        self.key = key
        self.val = val
        self.count = count

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = {} # key to node;
        self.count2node = defaultdict(OrderedDict) # count 2 ordered dictionary of nodes
        self.minCount = sys.maxsize

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        # count
        node = self.key2node[key]
        keycount = node.count
        node.count += 1

        del self.count2node[keycount][key]
        if not self.count2node[keycount]:
            del self.count2node[keycount]

        self.count2node[node.count][key] = node

        # minimal count
        if not self.count2node[self.minCount]:
            self.minCount += 1

        return node.val

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if key not in self.key2node:
            if len(self.key2node) == self.capacity:
                ckey, minNode = self.count2node[self.minCount].popitem(last=False)
                ccnt = minNode.count
                del self.key2node[ckey]
            node = Node(key, value, 1)
            self.key2node[key] = node
            self.count2node[1][key] = node
            self.minCount = min(self.minCount, 1)

        elif key in self.key2node:
            self.key2node[key].val = value
            self.get(key)
```

以及：

```python
class LFUCache:
    def __init__(self, capacity):
        self._cap = capacity
        self._key2count = {}
        self._count2nodes = {}
        self._min = 0

    def get(self, key):
        key2count = self._key2count
        count2nodes = self._count2nodes

        if key not in key2count:
            return -1

        count = key2count[key]
        value = count2nodes[count][key]
        del count2nodes[count][key]
        if not count2nodes[count]:
            del count2nodes[count]
        if self._min not in count2nodes:
            self._min += 1
        count += 1
        key2count[key] = count
        if count not in count2nodes:
            count2nodes[count] = {}
        count2nodes[count][key] = value
        return value

    def put(self, key, value):
        if self._cap == 0:
            return -1

        key2count = self._key2count
        count2nodes = self._count2nodes

        if key in key2count:
            count = key2count[key]
            del count2nodes[count][key]
            if not count2nodes[count]:
                del count2nodes[count]
            count += 1
            if count not in count2nodes:
                count2nodes[count] = {}
            if self._min not in count2nodes:
                self._min += 1
            count2nodes[count][key] = value
            key2count[key] = count
            return

        if len(key2count) == self._cap:
            nodes = count2nodes[self._min]
            first_key = next(iter(nodes))
            del key2count[first_key]
            del nodes[first_key]
            if not nodes:
                del count2nodes[self._min]

        key2count[key] = self._min = 1
        if 1 not in count2nodes:
            count2nodes[1] = {}
        count2nodes[1][key] = value

```

这个题目有点垃圾。。更像是做research的。
