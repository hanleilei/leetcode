# Rotate Function

[[math]]

You are given an integer array nums of length n.

Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:

$F(k) = 0 * arr_k[0] + 1* arr_k[1] + ... + (n - 1) * arr_k[n - 1]$.
Return the maximum value of F(0), F(1), ..., F(n-1).

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

```yaml
Input: nums = [4,3,2,6]
Output: 26
Explanation:

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
```

Example 2:

```yaml
Input: nums = [100]
Output: 0
```

Constraints:

n == nums.length
1 <= n <= 105
-100 <= nums[i] <= 100

```
 nums: [A0,A1,A2,A3]

 F0 = 0*A0 + 1*A1 + 2*A2 + 3*A3

 F1 = 0*A3 + 1*A0 + 2*A1 + 3*A2 
    = F0 + A0 + A1 + A2 - 3*A3 
    = F0 + sum-A3 - 3*A3 
    = F0 + sum - 4*A3

 F2 = 0*A2 + 1*A3 + 2*A0 + 3*A1 
    = F1 + A3 + A0 + A1 - 3*A2 
    = F1 + sum - 4*A2

 F3 = 0*A1 + 1*A2 + 2*A3 + 3*A0 
    = F2 + A2 + A3 + A0 - 3*A1 
    = F2 + sum - 4*A1
```

抽象：

```
 F(i) = F(i-1) + sum - n * A(n-i)
```

```python
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        r = cur = sum(i * j for i, j in enumerate(nums))
        s = sum(nums)
        k = len(nums)
        while nums:
            cur += s - nums.pop() * k
            r = max(cur, r)
        return r
```

这种用pop的方式会改变原数组，如果不想改变原数组，可以使用索引：

```python
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        res = cur = sum(i * v for i, v in enumerate(nums))
        total = sum(nums)

        for i in range(n - 1, 0, -1): # 注意这里的顺序，因为我们需要从后往前计算
            cur += total - nums[i] * n
            res = max(res, cur)
        return res
```

```python
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        res = 0
        f = 0
        n = len(nums)
        s = 0

        for i in range(n):
            s += nums[i]
            f += i * nums[i]
        
        res = f
        for i in range(1, n):
            f += s - n * nums[n - i]
            res = max(res, f)
        return res
```
