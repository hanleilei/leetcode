# contains duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

巧用enumerate和字典

前面加上一个判断，速度一下超过99%的提交用户，简直了。。

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or k<0 or len(nums)==len(set(nums)):
            return False

        d = dict()
        for m,  n in enumerate(nums):
            if n in d and m - d[n] <=k:
                return True
            d[n] = m
        return False
```
