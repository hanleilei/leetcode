# LRU Cache
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

    # @return an integer        
    def get(self, key):
        try:
            value = self.dict[key]
            del self.dict[key]
            self.dict[key] = value
            return value
        except:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing        
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



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
以下是一个快速的版本

```python
# Fast Solution
from collections import deque
class LRUCache(object):
	def __init__(self, capacity):
		self.capacity = capacity
		self.queue = deque()
		self.map = {}
		self.timec = 0


	def get(self, key):
		self.timec += 1

		if (not key in self.map):
			return -1

		val, _ = self.map[key]
		self.map[key] = (val, self.timec)
		self.queue.appendleft((key, val, self.timec))        

		return val       


	def put(self, key, value):
		self.timec += 1
		self.map[key] = (value, self.timec)
		self.queue.appendleft((key, value, self.timec))

		self.fix_queue()       
	def fix_queue(self):
		while len(self.map) > self.capacity:
			key, val, time = self.queue.pop()
			val_r, time_r = self.map[key]

			if (val == val_r and time_r == time):
				self.map.pop(key)    
```
