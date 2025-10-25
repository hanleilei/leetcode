# find pivot index

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

## Example 1

```text
Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
```

## Example 2

```text
Input:
nums = [1, 2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
```

## Note

- The length of nums will be in the range [0, 10000].
- Each element nums[i] will be an integer in the range [-1000, 1000]

求和，然后做变换。

```Python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums)

        for i, v in enumerate(nums):
            right -= v
            if left == right:
                return i
            left += v
        return -1

```

似乎用 enumerate 速度会变慢，换一个方法写：

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right = right - nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1
```

再来一个速度快的

```Python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
```

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            if total - nums[i] == left * 2:
                return i
            else:
                left += nums[i]
        return -1
```

还可以用前缀和：

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        preSum[0] = 0
        # 计算 nums 的前缀和
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        # 根据前缀和判断左半边数组和右半边数组的元素和是否相同
        for i in range(1, len(preSum)):
            # 计算 nums[i-1] 左侧和右侧的元素和
            leftSum = preSum[i - 1] - preSum[0]
            rightSum = preSum[n] - preSum[i]
            if leftSum == rightSum:
                # 相对 nums 数组，preSum 数组有一位索引偏移
                return i - 1
        return -1
```
