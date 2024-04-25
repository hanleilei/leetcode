# Move Zeros

[[2points]]

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

还好，就是要理解 python 中列表的处理方式

```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j = j + 1
```

如果觉得这个理解有问题，可以直接用题目描述的含义，直接实现：

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                if count != i:
                    nums[i] = 0
                count += 1
```

和27题目类似，唯一的差别就是多加上一个循环，把最后的几个元素变成0

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        for slow in range(slow, len(nums)):
            nums[slow]= 0

        return nums
```

再来一个snowball方法, 很有趣，也很有想法，来自于[olsh](https://leetcode.com/problems/move-zeroes/solutions/172432/the-easiest-but-unusual-snowball-java-solution-beats-100-o-n-clear-explanation/)：

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        snowBallSize = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowBallSize += 1
            elif snowBallSize > 0:
                t = nums[i]
                nums[i] = 0
                nums[i - snowBallSize] = t
```
