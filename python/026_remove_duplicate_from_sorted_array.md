# remove duplicate from sorted array

[[2points]]

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

 使用一个指针 j，当 i 向后遍历数组时，如果遇到与 A[j]不同的，将 A[i]和 A[j+1]交换，同时 j=j+1，即 j 向后移动一个位置，然后 i 继续向后遍历

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                nums[i], nums[j+1] = nums[j+1], nums[i]
                j = j+1
        return j+1
```

```python
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i=0
        for num in nums[1:]:
            if num!=nums[i]:
                i+=1
                nums[i]=num
        return i+1
```

快慢双指针的方法：

```python
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        slow = 0
        quick = 0
        while quick < len(nums):
            if nums[quick] != nums[slow]:
                slow+= 1
                nums[slow] = nums[quick]
            quick += 1
        return slow +1
```
