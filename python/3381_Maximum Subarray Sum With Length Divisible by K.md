# 3381. Maximum Subarray Sum With Length Divisible by K

## 问题描述

You are given an array of integers `nums` and an integer `k`.

Return the **maximum sum** of a **subarray** of `nums`, such that
the size of the subarray is **divisible** by `k`.

A **subarray** is a contiguous **non-empty** sequence of elements
within an array.

## 示例

**Example 1:**

```text
Input: nums = [1,2], k = 1
Output: 3
```

Explanation: The subarray `[1, 2]` with sum 3 has length equal to 2
which is divisible by 1.

**Example 2:**

```text
Input: nums = [-1,-2,-3,-4,-5], k = 4
Output: -10
```

Explanation: The maximum sum subarray is `[-1, -2, -3, -4]` which has
length equal to 4 which is divisible by 4.

**Example 3:**

```text
Input: nums = [-5,1,2,-3,4], k = 2
Output: 4
```

Explanation: The maximum sum subarray is `[1, 2, -3, 4]` which has
length equal to 4 which is divisible by 2.

## 约束条件

- $1 \le k \le \text{nums.length} \le 2 \times 10^5$
- $-10^9 \le \text{nums}[i] \le 10^9$

## 解法

### 方法1：前缀和 + 同余分组 推荐

核心思想：长度为 k 的倍数的子数组，其起点和终点的下标模 k 同余。

对于子数组 `nums[i:j]`（长度为 `j - i`），要使长度被 k 整除，
需要 `(j - i) % k == 0`，即 `j % k == i % k`。

使用前缀和数组 `prefix[j]` 表示 `nums[0:j]` 的和，则子数组和为：

$$\text{sum}(i, j) = \text{prefix}[j] - \text{prefix}[i]$$

要最大化子数组和，对于每个位置 j，我们需要找到满足
`i % k == j % k` 的最小前缀和 `prefix[i]`。

```python
from typing import List
import sys

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        """
        前缀和 + 同余分组

        时间复杂度：O(n)
        空间复杂度：O(k)
        """
        # min_prefix[i] 存储下标模 k 余 i 的最小前缀和
        min_prefix = [sys.maxsize] * k
        # 初始化：下标 0 的前缀和为 0，0 % k = 0
        # 但题目要求非空子数组，所以初始化为下标 -1
        min_prefix[(-1) % k] = 0

        prefix_sum = 0
        max_sum = -sys.maxsize

        for j, num in enumerate(nums):
            prefix_sum += num
            remainder = j % k

            # 计算以 j 结尾的最大子数组和
            # 找到同余的最小前缀和
            max_sum = max(max_sum, prefix_sum - min_prefix[remainder])

            # 更新当前余数的最小前缀和
            min_prefix[remainder] = min(min_prefix[remainder], prefix_sum)

        return max_sum
```

### 方法2：使用 accumulate 预计算前缀和

使用 `itertools.accumulate` 预先计算所有前缀和。

```python
from typing import List
from itertools import accumulate

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        """
        accumulate + 同余分组

        时间复杂度：O(n)
        空间复杂度：O(n + k)
        """
        # 预计算前缀和，initial=0 表示 prefix[0] = 0
        prefix = list(accumulate(nums, initial=0))

        # min_prefix[i] 存储下标模 k 余 i 的最小前缀和
        min_prefix = [float('inf')] * k
        max_sum = float('-inf')

        for j, psum in enumerate(prefix):
            remainder = j % k

            # 计算最大子数组和
            max_sum = max(max_sum, psum - min_prefix[remainder])

            # 更新当前余数的最小前缀和
            min_prefix[remainder] = min(min_prefix[remainder], psum)

        return max_sum
```

### 方法3：动态规划思想

维护以每个位置结尾、长度被 k 整除的最大子数组和。

```python
from typing import List
import sys

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        """
        动态规划

        时间复杂度：O(n)
        空间复杂度：O(k)
        """
        n = len(nums)
        # dp[i][r] 表示考虑前 i 个元素，长度模 k 余 r 的最大和
        # 优化为滚动数组
        min_prefix = [sys.maxsize] * k
        min_prefix[0] = 0

        prefix_sum = 0
        result = -sys.maxsize

        for i in range(n):
            prefix_sum += nums[i]
            idx = (i + 1) % k

            # 长度被 k 整除的子数组
            if min_prefix[idx] != sys.maxsize:
                result = max(result, prefix_sum - min_prefix[idx])

            min_prefix[idx] = min(min_prefix[idx], prefix_sum)

        return result
```

## 算法分析

### 核心思想详解

长度被 k 整除的条件：

子数组 `nums[i:j]` 的长度为 `j - i`。要使长度被 k 整除：

$$(j - i) \bmod k = 0$$

等价于：

$$j \bmod k = i \bmod k$$

同余分组：

将所有下标按照模 k 的余数分组：

- 余数 0：下标 0, k, 2k, 3k, ...
- 余数 1：下标 1, k+1, 2k+1, ...
- ...
- 余数 k-1：下标 k-1, 2k-1, 3k-1, ...

前缀和优化：

对于每个下标 j，要找到满足 `i % k == j % k` 且使
`prefix[j] - prefix[i]` 最大的 i，即找最小的 `prefix[i]`。

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 前缀和分组 | O(n) | O(k) | 最优解 |
| accumulate | O(n) | O(n + k) | 代码简洁 |
| 动态规划 | O(n) | O(k) | 思路清晰 |

其中 n 是数组长度。

### 执行过程示例

以 `nums = [-5,1,2,-3,4]`, `k = 2` 为例。

**初始状态：**

```text
min_prefix = [0, inf]  # min_prefix[i] 表示余数为 i 的最小前缀和
prefix_sum = 0
max_sum = -inf
```

**Step 1**：处理 `nums[0] = -5`（下标 0）

```text
prefix_sum = -5
j = 0, remainder = 0 % 2 = 0

计算：-5 - min_prefix[0] = -5 - 0 = -5
max_sum = max(-inf, -5) = -5

更新：min_prefix[0] = min(0, -5) = -5
min_prefix = [-5, inf]
```

**Step 2**：处理 `nums[1] = 1`（下标 1）

```text
prefix_sum = -5 + 1 = -4
j = 1, remainder = 1 % 2 = 1

计算：-4 - min_prefix[1] = -4 - inf = -inf
max_sum = max(-5, -inf) = -5

更新：min_prefix[1] = min(inf, -4) = -4
min_prefix = [-5, -4]
```

**Step 3**：处理 `nums[2] = 2`（下标 2）

```text
prefix_sum = -4 + 2 = -2
j = 2, remainder = 2 % 2 = 0

计算：-2 - min_prefix[0] = -2 - (-5) = 3
max_sum = max(-5, 3) = 3
子数组 nums[0:2] = [-5,1,2]，长度 2

更新：min_prefix[0] = min(-5, -2) = -5
min_prefix = [-5, -4]
```

**Step 4**：处理 `nums[3] = -3`（下标 3）

```text
prefix_sum = -2 + (-3) = -5
j = 3, remainder = 3 % 2 = 1

计算：-5 - min_prefix[1] = -5 - (-4) = -1
max_sum = max(3, -1) = 3

更新：min_prefix[1] = min(-4, -5) = -5
min_prefix = [-5, -5]
```

**Step 5**：处理 `nums[4] = 4`（下标 4）

```text
prefix_sum = -5 + 4 = -1
j = 4, remainder = 4 % 2 = 0

计算：-1 - min_prefix[0] = -1 - (-5) = 4
max_sum = max(3, 4) = 4
子数组 nums[0:4] = [-5,1,2,-3,4]，长度 4 ❌
实际是 nums[1:5] = [1,2,-3,4]，长度 4 ✓
（因为 prefix[4] - prefix[0] = nums[1:5]）

更新：min_prefix[0] = min(-5, -1) = -5
min_prefix = [-5, -5]
```

**最终结果**：`max_sum = 4`

对应子数组 `[1, 2, -3, 4]`，和为 4，长度为 4（被 2 整除）。

## 常见错误

### 错误1：初始化 min_prefix 错误

```python
# 错误：全部初始化为 0
min_prefix = [0] * k

# 正确：需要初始化为无穷大，除了余数对应空前缀的位置
min_prefix = [float('inf')] * k
# 下标 -1（空前缀）模 k 的余数为 (k-1) 或 0（看实现）
min_prefix[(k-1) % k] = 0  # 或者 min_prefix[0] = 0（看下标从0还是1开始）
```

### 错误2：混淆下标和前缀和的对应关系

```python
# 错误：使用 prefix_sum 的余数
remainder = prefix_sum % k  # 错误！

# 正确：使用下标的余数
remainder = j % k
```

### 错误3：忘记题目要求非空子数组

```python
# 错误：可能得到空子数组（和为0）
for j, num in enumerate(nums):
    prefix_sum += num
    max_sum = max(max_sum, prefix_sum)  # 错误！

# 正确：必须减去某个之前的前缀和
max_sum = max(max_sum, prefix_sum - min_prefix[remainder])
```

### 错误4：同余条件理解错误

```python
# 错误：认为长度必须是 k
if (j - i) == k:
    ...

# 正确：长度必须是 k 的倍数
if (j - i) % k == 0:
    ...
# 等价于：j % k == i % k
```

### 错误5：更新顺序错误

```python
# 错误：先更新再计算
min_prefix[remainder] = min(min_prefix[remainder], prefix_sum)
max_sum = max(max_sum, prefix_sum - min_prefix[remainder])

# 正确：先计算再更新（否则会用到自己）
max_sum = max(max_sum, prefix_sum - min_prefix[remainder])
min_prefix[remainder] = min(min_prefix[remainder], prefix_sum)
```

### 错误6：负数数组处理不当

```python
# 错误：初始化为 0
max_sum = 0  # 当所有数都是负数时会出错

# 正确：初始化为负无穷
max_sum = float('-inf')
```

## 相关题目

- [0053. Maximum Subarray](./053_Maximum_Subarray.md) - 最大子数组和
- [0918. Maximum Sum Circular Subarray](./918_maximum_sum_circular_subarray.md) - 环形最大子数组和
- [0974. Subarray Sums Divisible by K](./974_subarray_sums_divisible_by_k.md) - 和被 K 整除的子数组
- [0560. Subarray Sum Equals K](./560_subarray_sum_equals_k.md) - 和为 K 的子数组
- [1590. Make Sum Divisible by P](./1590_make_sum_divisible_by_p.md) - 使数组和被 P 整除
