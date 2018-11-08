# Range Sum Query - Mutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:
```
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
```

Note:

1. The array is only modifiable by the update function.
2. You may assume the number of calls to update and sumRange function is distributed evenly.

先看看stefan大大的算法，删除两行，再加上两行：

```Python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.update = nums.__setitem__
        self.sumRange = lambda i, j: sum(nums[i:j+1])

```

这也能过，但是速度很慢，那就看个速度快的：

```Python
class IndexTree(object):
    def __init__(self,nums):
        n = len(nums)
        sum = [0] * (n+1)
        for i in range(1,n+1):
            sum[i] = sum[i-1] + nums[i-1]
        self.sum = [0] * (n+1)
        for i in range(1,n+1):
            self.sum[i] = sum[i] - sum[i-(i&-i)]


    def getSum(self,i):
        res = 0
        while i != 0:
            res += self.sum[i]
            i -= (i & -i)
        return res

    def update(self,i,val):
        n = len(self.sum) - 1
        while i <= n:
            self.sum[i] += val
            i += (i & -i)

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.tree = IndexTree(nums)
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.tree.update(i+1,diff)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree.getSum(j+1) - self.tree.getSum(i)
```
使用的是segment tree。
