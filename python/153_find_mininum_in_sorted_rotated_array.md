# Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

### 抖机灵。。。和33一样


```python
class Solution(object):
    def findMin(self, nums):
        if len(nums) == 0:
            return 0

        start, end = 0, len(nums) -1
        target = nums[-1]

        while start +1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                end=mid
            else:
                start = mid
        return min(nums[start], nums[end])

```

在programming pearls 里面有介绍这个问题，直接用二分法：

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            m = i + (j - i) // 2
            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m
        return nums[i]
```
