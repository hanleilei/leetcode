# Find peak element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

暴力法：

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

下面是二分法的版本

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
       mid = (start + end) // 2
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
