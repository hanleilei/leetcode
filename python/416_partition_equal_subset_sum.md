# 416. Partition Equal Subset Sum

[[dp]]

## 问题描述

Given a **non-empty** array `nums` containing **only positive integers**,
find if the array can be partitioned into two subsets such that the
sum of elements in both subsets is equal.

## 示例

**Example 1:**

```text
Input: nums = [1,5,11,5]
Output: true
```

Explanation: The array can be partitioned as `[1, 5, 5]` and `[11]`.

**Example 2:**

```text
Input: nums = [1,2,3,5]
Output: false
```

Explanation: The array cannot be partitioned into equal sum subsets.

## 约束条件

- $1 \le \text{nums.length} \le 200$
- $1 \le \text{nums}[i] \le 100$

## 解法

### 方法1：动态规划（0/1背包）推荐

将问题转化为0/1背包：能否从数组中选出若干数字，使其和等于
`sum(nums) / 2`。

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        0/1背包问题

        时间复杂度：O(n × target)
        空间复杂度：O(target)
        """
        # 剪枝：总和为奇数，无法平分
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        # dp[j] 表示能否凑出和为 j
        dp = [False] * (target + 1)
        dp[0] = True  # 和为0总是可达（不选任何数）

        # 遍历每个数字
        for num in nums:
            # 逆序遍历（关键！避免重复使用同一数字）
            for j in range(target, num - 1, -1):
                # 不选num 或 选num
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
```

### 方法2：集合记录可达和

使用集合记录所有可能的子集和，动态更新。

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        集合记录可达和

        时间复杂度：O(n × target)
        空间复杂度：O(target)
        """
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        # 存储所有可能的子集和
        reachable = {0}

        for num in nums:
            # 提前检查，找到就返回
            if target in reachable:
                return True

            # 计算加入当前数字后的新和
            new_sums = set()
            for s in reachable:
                new_sum = s + num
                if new_sum == target:
                    return True
                if new_sum < target:
                    new_sums.add(new_sum)

            # 更新可达和集合
            reachable.update(new_sums)

        return target in reachable
```

### 方法3：DFS + 记忆化

递归搜索所有可能的选择，使用记忆化避免重复计算。

```python
from typing import List, Set

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        DFS + 记忆化

        时间复杂度：O(n × target)
        空间复杂度：O(target)
        """
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        memo: Set[int] = set()

        def dfs(index: int, remaining: int) -> bool:
            """从index开始，能否凑出remaining"""
            # 基本情况
            if remaining == 0:
                return True
            if remaining < 0 or index >= len(nums):
                return False

            # 记忆化剪枝
            if remaining in memo:
                return False
            memo.add(remaining)

            # 选择当前数字 或 不选
            return (dfs(index + 1, remaining - nums[index]) or 
                    dfs(index + 1, remaining))

        return dfs(0, target)
```

### 方法4：位运算优化

使用位运算表示所有可能的和。

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        位运算优化

        时间复杂度：O(n × target)
        空间复杂度：O(1)
        """
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        # 用位表示所有可能的和
        # 第i位为1表示和i是可达的
        bits = 1  # 初始：和0可达

        for num in nums:
            # 左移num位，表示加上num后的新和
            bits |= bits << num

        # 检查第target位是否为1
        return (bits >> target) & 1 == 1
```

## 算法分析

### 核心思想详解

**问题转化**：

等和子集问题 → 0/1背包问题

- 原问题：能否分成两个和相等的子集？
- 转化后：能否选出若干数字，使其和等于 `sum / 2`？

**0/1背包特征**：

- 每个数字最多使用一次
- 背包容量为 `target = sum / 2`
- 物品重量和价值都是数字本身

**为什么必须逆序遍历？**

```python
# 正序遍历（错误）：
for num in nums:
    for j in range(num, target + 1):  # 正序
        dp[j] = dp[j] or dp[j - num]
# 问题：num=5时，dp[10]可能用到已更新的dp[5]，导致num被用两次

# 逆序遍历（正确）：
for num in nums:
    for j in range(target, num - 1, -1):  # 逆序
        dp[j] = dp[j] or dp[j - num]
# 正确：dp[j-num]始终是上一轮（未包含num）的状态
```

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| DP（0/1背包） | O(n × target) | O(target) | 最优解 |
| 集合记录 | O(n × target) | O(target) | 易理解 |
| DFS记忆化 | O(n × target) | O(target) | 递归 |
| 位运算 | O(n × target) | O(1) | 最省空间 |

其中 `target = sum(nums) / 2`。

### 执行过程示例

以 `nums = [1, 5, 11, 5]` 为例：

初始状态：

```text
sum = 22, target = 11
dp = [T, F, F, F, F, F, F, F, F, F, F, F]
     0  1  2  3  4  5  6  7  8  9  10 11
```

**Step 1**：处理 num = 1

```text
j=11: dp[11] = dp[11] or dp[10] = F or F = F
j=10: dp[10] = dp[10] or dp[9]  = F or F = F
...
j=1:  dp[1]  = dp[1]  or dp[0]  = F or T = T

dp = [T, T, F, F, F, F, F, F, F, F, F, F]
```

**Step 2**：处理 num = 5

```text
j=11: dp[11] = dp[11] or dp[6]  = F or F = F
...
j=6:  dp[6]  = dp[6]  or dp[1]  = F or T = T
j=5:  dp[5]  = dp[5]  or dp[0]  = F or T = T

dp = [T, T, F, F, F, T, T, F, F, F, F, F]
     0  1  2  3  4  5  6  7  8  9  10 11
```

**Step 3**：处理 num = 11

```text
j=11: dp[11] = dp[11] or dp[0]  = F or T = T ✓

dp = [T, T, F, F, F, T, T, F, F, F, F, T]
```

**Step 4**：处理 num = 5（第二次）

```text
已经 dp[11] = True，继续更新其他位置
j=11: dp[11] = dp[11] or dp[6]  = T or T = T
j=10: dp[10] = dp[10] or dp[5]  = F or T = T
...

dp = [T, T, F, F, F, T, T, F, F, F, T, T]
```

最终：`dp[11] = True`，返回 `True`

**可视化DP表格**：

| num | dp[0] | dp[1] | dp[2] | dp[3] | dp[4] | dp[5] | dp[6] | dp[7] | dp[8] | dp[9] | dp[10] | dp[11] |
|-----|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------|--------|
| 初始 | T | F | F | F | F | F | F | F | F | F | F | F |
| 1 | T | T | F | F | F | F | F | F | F | F | F | F |
| 5 | T | T | F | F | F | T | T | F | F | F | F | F |
| 11 | T | T | F | F | F | T | T | F | F | F | F | T |
| 5 | T | T | F | F | F | T | T | F | F | F | T | T |

## 常见错误

### 错误1：忘记检查总和奇偶性

```python
# 错误：没有剪枝
target = sum(nums) // 2
dp = [False] * (target + 1)

# 正确：提前返回
if sum(nums) % 2 != 0:
    return False
```

### 错误2：正序遍历导致重复使用

```python
# 错误：正序遍历，num会被重复使用
for num in nums:
    for j in range(num, target + 1):  # 正序
        dp[j] = dp[j] or dp[j - num]

# 正确：逆序遍历
for num in nums:
    for j in range(target, num - 1, -1):  # 逆序
        dp[j] = dp[j] or dp[j - num]
```

### 错误3：DP初始化错误

```python
# 错误：全部初始化为False
dp = [False] * (target + 1)
# 无法转移！

# 正确：dp[0] = True
dp[0] = True  # 和为0总是可达
```

### 错误4：遍历范围错误

```python
# 错误：从0开始遍历
for j in range(0, target + 1):
    ...

# 正确：从target到num
for j in range(target, num - 1, -1):
    ...
```

### 错误5：集合更新时机错误

```python
# 错误：边遍历边更新集合
for num in nums:
    for s in reachable:
        reachable.add(s + num)  # 会导致无限循环

# 正确：先收集新和，再批量更新
new_sums = set()
for s in reachable:
    new_sums.add(s + num)
reachable.update(new_sums)
```

### 错误6：DFS时切片数组效率低

```python
# 错误：切片创建新数组，效率低
def dfs(nums, target):
    for i, n in enumerate(nums):
        if dfs(nums[i+1:], target - n):  # 切片O(n)
            return True

# 正确：使用索引
def dfs(index, target):
    return dfs(index + 1, target - nums[index])
```

## 相关题目

- [0416. Partition Equal Subset Sum](./416_partition_equal_subset_sum.md)
- [0494. Target Sum](./494_target_sum.md) - 0/1背包变体
- [1049. Last Stone Weight II](./1049_last_stone_weight_ii.md) - 最小化差值
- [0698. Partition to K Equal Sum Subsets](./698_partition_to_k_equal_sum_subsets.md) - K个子集
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](./2035_partition_array_into_two_arrays_to_minimize_sum_difference.md) - 最小差值
