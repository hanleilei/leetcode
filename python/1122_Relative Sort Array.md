# Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]

Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map = dict(Counter(arr1))
        
        for i in range (len(arr1)):
            if arr1[i] not in hash_map:
                hash_map[arr1[i]] = 1000 + arr1[i]
        arr1.sort(key = lambda x: hash_map[x])
        return arr1
```

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k = {b: i for i, b in enumerate(arr2)}
        return sorted(arr1, key = lambda a: k.get(a, 1000+a))
```

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = list()
        counter = collections.Counter(arr1)
        s = sorted(list(set(arr1) - set(arr2)))
        
        for i in arr2 + s:
            res.extend([i] * counter[i])
        return res
```
