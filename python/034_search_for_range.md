# search for range

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

#### 主要还是想清楚问题怎么解决， 这里用了collections里面的Counter库



```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        from collections import Counter
        if target in nums:
            return [nums.index(target),Counter(nums)[target]+ nums.index(target)-1]
        else:
            return [-1,-1]
```
