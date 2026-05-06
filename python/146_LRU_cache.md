# LRU Cache

[[design]]

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

我的方案是用一个OrderedDict实现。

```python
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.dict = collections.OrderedDict()

    def get(self, key):
        if key not in self.dict:
            return -1
        value = self.dict[key]
        del self.dict[key]
        self.dict[key] = value
        return value

    def put(self, key, value):
        try:
            del self.dict[key]
            self.dict[key] = value
        except:
            if self.length == self.capacity:
                self.dict.popitem(last = False)
                self.length -= 1
            self.dict[key] = value
            self.length +=1
```

直接上OrderedDict，这里面有很多很好的函数：

```python
class LRUCache:

    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key) # 直接将key移动到末尾
            return self.od.get(key)
        return -1

    def put(self, key: int, value: int) -> None:
        self.od[key] = value
        if len(self.od) > self.size:
            self.od.popitem(last=False) # last = True 就是当作stack 操作，否则当作 queue 操作。
        self.od.move_to_end(key)
```

```python
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.size:
            self.popitem(last=False)
```

双向链表 + 哈希表：

```python
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
```
