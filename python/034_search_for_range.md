# search for range

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

#### 主要还是想清楚问题怎么解决， 这里用了collections里面的Counter库。或者二分法。



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
二分法：

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0; right = len(nums) - 1
        result = [-1, -1]
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                result[0] = mid  
                result[1] = mid  

                i = mid - 1  
                while i >= 0 and nums[i] == target:  
                    result[0] = i  
                    i -= 1  

                i = mid + 1  
                while i < len(nums) and nums[i] == target:  
                    result[1] = i  
                    i += 1  

                break
        return result
```
再来一个标准库的：

```python
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        if not nums:
            return [-1, -1]

        l = bisect.bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            l = -1
        r = bisect.bisect_right(nums, target) - 1
        if nums[r] != target:
            r = -1

        return [l, r]
```
