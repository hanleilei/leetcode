# Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

### Example:
```
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```
### Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

套用九章的模版，算法复杂度为O(n)，思路一下就很清晰了：


```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums == []:
            return 0
        size = len(nums)
        j = 1
        res = float('inf')
        total = nums[0]

        for i in range(size):
            while j < size and total < s:
                total += nums[j]
                j += 1
            if total >= s:
                res = min(res, j - i)
            total -= nums[i]

        return res if res != float('inf') else 0
```
