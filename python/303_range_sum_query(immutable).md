# range sum query

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
```
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

## Note:
1. You may assume that the array does not change.
2. There are many calls to sumRange function.

## 思路：

先保存一个数组，数组中的每个元素都是从零到当前位置的数值之和。然后在后续直接遍历这个数组，如果求一段数字，只需要做两个数组元素的差值就可以了。

```python
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.res = nums[:]
        size = len(nums)
        for i in range(1, size):
            self.res[i] = self.res[i - 1] + nums[i]


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.res[j]
        return self.res[j] - self.res[i-1]
```
