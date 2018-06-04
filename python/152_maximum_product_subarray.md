# maximum product subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```
Example 2:
```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
直接上DP

```python
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=big=small=nums[0]
        for n in nums[1:]:
            big, small=max(n, n*big, n*small), min(n, n*big, n*small)
            maximum=max(maximum, big)
        return maximum
```

再来看一个更快的版本：

```python
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = -float("inf")
        product = 1
        for num in nums:
            product *= num
            max_val = max(product, max_val)
            if num == 0:
                product = 1
        product = 1
        for num in nums[::-1]:
            product *= num
            max_val = max(product, max_val)
            if num == 0:
                product = 1
        return max_val

```
这个算法的优秀之处在于两次遍历，没有那么多的乘法运算。
