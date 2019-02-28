# increasing triplet subsequence

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
```
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
```
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:
```
Input: [1,2,3,4,5]
Output: true
```
Example 2:
```
Input: [5,4,3,2,1]
Output: false
```

```python
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = []
        for n in nums:
            index = bisect.bisect_left(res, n)
            if index == len(res):
                res.append(n)
            else:
                res[index] = n
            if len(res) == 3:
                return True
        return False
```

还有这样的算法，可以不用二分法，直接O(N)搞定：

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
```
