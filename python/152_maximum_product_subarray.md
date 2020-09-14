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

再来一个最简单的算法：

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        B = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(nums),max(B))
```


很有趣，算法都差不多，但是，速度却差别很大：

 ```python
 class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min=nums[0]
        curr_max=nums[0]
        max_product=nums[0]
        for num in nums[1:]:
            min_temp=curr_min
            curr_min=min(num,num*curr_min,num*curr_max)
            curr_max=max(num,num*min_temp,num*curr_max)
            max_product=max(max_product,curr_max)
        return max_product
 ```

最快的：

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in nums:
            local_max = max(1, local_max)
            if x > 0:
                local_max, local_min = local_max * x, local_min * x
            else:
                local_max, local_min = local_min * x, local_max * x
            global_max = max(global_max, local_max)
        return global_max
```

再看看Lee215的方法， 超级快。。
```Python
class Solution:
    def maxProduct(self, A: List[int]) -> int:
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)
```
