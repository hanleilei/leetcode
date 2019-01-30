# Find peak element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Note:
Your solution should be in logarithmic complexity.

Credits:
Special thanks to \@ts for adding this problem and creating all test cases.

###### 我只能搞定暴力破解
```python
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, nums):
        size = len(nums)
        for x in range(1, size - 1):
            if nums[x] > nums[x - 1] and nums[x] > nums[x + 1]:
                return x
        return [0, size - 1][nums[0] < nums[size - 1]]
```
#### 下面是二分法的版本
```python
Solution(object):
   def findPeakElement(self, nums):
       """
       :type nums: List[int]
       :rtype: int
       """
       size = len(nums)
       return self.search(nums, 0, size - 1)

   def search(self, num, start, end):
       if start == end:
           return start
       if start + 1 == end:
           return [start, end][num[start] < num[end]]
       mid = (start + end) / 2
       if num[mid] < num[mid - 1]:
           return self.search(num, start, mid - 1)
       if num[mid] < num[mid + 1]:
           return self.search(num, mid + 1, end)
       return mid
```

再来一个最快的，超过100%的提交：：

```python
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        while low <= high:
            if low == high:
                return low
            mid = (low + high) // 2
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid

        return mid
```
