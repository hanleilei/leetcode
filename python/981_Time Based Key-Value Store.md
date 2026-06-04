# Time Based Key-Value Store

[[design]] [[hashtable]] [[binarysearch]]

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

Constraints:

    1 <= key.length, value.length <= 100
    key and value consist of lowercase English letters and digits.
    1 <= timestamp <= 107
    All the timestamps timestamp of set are strictly increasing.
    At most 2 * 105 calls will be made to set and get.

```python
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        # binary search: 找出第一个比k大的，然后-1
        lst = self.d[key]
        l,r=0,len(lst)
        if timestamp>=lst[-1][0]:
            return lst[-1][1]
        while l<r:
            mid = l + (r-l)//2
            if lst[mid][0] == timestamp:
                return lst[mid][1]
            if lst[mid][0] < timestamp:
                l = mid + 1
            else: 
                r = mid

        return lst[r-1][1] if r>0 else ""
```

```python
class TimeMap:
    def __init__(self):
        self.store = defaultdict(lambda: [[], []])  # [timestamps, values]

    def set(self, key: str, value: str, timestamp: int) -> None:
        timestamps, values = self.store[key]
        timestamps.append(timestamp)
        values.append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        timestamps, values = self.store[key]
        idx = bisect_right(timestamps, timestamp) - 1
        if idx >= 0:
            return values[idx]
        return ""
```
