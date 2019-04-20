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
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        res = [-1, -1]

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                res = [mid, mid]

                i = mid - 1
                while i >= 0 and nums[i] == target:
                    res[0] = i
                    i -= 1
                i = mid + 1
                while i < len(nums) and nums[i] == target:
                    res[1] = i
                    i += 1
                break
        return res
    
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
