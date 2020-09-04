# contains duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

###### 巧用enumernate和字典

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
