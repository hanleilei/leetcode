# Convert an Array Into a 2D Array With Conditions

[[hashtable]]

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

## Example 1

```text
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
```

## Example 2

```text
Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
```

## Constraints

```text
1 <= nums.length <= 200
1 <= nums[i] <= nums.length
```

越来越感觉，medium就是阅读理解。。

```python
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        if len(nums)== len(set(nums)): return [nums]
        d = dict(Counter(nums))
        res = list()
        while not all(i == 0 for i in d.values()):
            t = list()
            for k, v in d.items():
                if v > 0:
                    t.append(k)
                    d[k] = v - 1
            res.append(t)
        return res
```

再来一个速度快的，但是好像也不快。。

```python
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []

        for num in nums:
            found = False
            for group in res:
                if num in group:
                    continue
                else:
                    found = True
                    group.add(num)
                    break
            
            if not found:
                res.append(set([num]))
        
        return res
```

再来一个lee215的方案：

```python
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        k = max(count.values())
        A = list(count.elements())
        return [A[i::k] for i in range(k)]
```
