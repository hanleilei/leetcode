# contains duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

###### 巧用enumernate和字典

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()
        for m,  n in enumerate(nums):
            if n in d and m - d[n] <=k:
                return True
            d[n] = m
        return False                
```
