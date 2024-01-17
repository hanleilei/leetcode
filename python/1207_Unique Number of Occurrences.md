# Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

## Example 1

```text
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```

## Example 2

```text
Input: arr = [1,2]
Output: false
```

## Example 3

```text
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
```

Constraints:

```text
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
```

都是阅读理解的套路

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict(collections.Counter(arr))
        return len(d.values()) == len(set(d.values()))
```

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for i in arr:
            d[i] += 1
        return len(d.values()) == len(set(d.values()))
```
