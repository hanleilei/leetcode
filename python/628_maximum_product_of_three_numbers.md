# Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

这个直接用标准库的方法，可以通过 leetcode 当前的测试，但是问题还是有的，比方说这个测试用例：[-4,-1,-2,-3,1,2,3,4]，按理来说应该是得到的 48，但是当前的结果是 24.

```python
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        from functools import reduce
        return reduce(lambda x, y: x*y, heapq.nlargest(3, nums))
```

考虑了一些边界条件，直接翻译成代码：

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        neg_count = len([i for i in nums if i < 0])
        nums.sort()
        res = 0

        if neg_count >= 2:
            return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
        else:
            return nums[-1] * nums[-2] * nums[-3]
```
