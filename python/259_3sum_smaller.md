# 259. 3Sum Smaller

[[2points]] [[premium]]

## 问题描述

Given an array of `n` integers `nums` and an integer `target`, find the
number of index triplets `i, j, k` with `0 <= i < j < k < n` that satisfy
the condition `nums[i] + nums[j] + nums[k] < target`.

## 示例

**Example 1:**

```text
Input: nums = [-2,0,1,3], target = 2
Output: 2
```

Explanation: Because there are two triplets which sums are less than 2:

- `[-2,0,1]`
- `[-2,0,3]`

**Example 2:**

```text
Input: nums = [], target = 0
Output: 0
```

**Example 3:**

```text
Input: nums = [0], target = 0
Output: 0
```

## 约束条件

- $n == \text{nums.length}$
- $0 \le n \le 3500$
- $-100 \le \text{nums}[i] \le 100$
- $-100 \le \text{target} \le 100$

## 解法

### 方法1：排序 + 双指针（推荐）

固定第一个数，用双指针在剩余数组中找满足条件的两数之和。

```python
from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        排序 + 双指针

        时间复杂度：O(n²)
        空间复杂度：O(1) 或 O(log n)（排序栈空间）
        """
        count = 0
        nums.sort()  # 排序是关键
        n = len(nums)

        # 固定第一个数
        for i in range(n - 2):
            # 双指针在 [i+1, n-1] 范围内查找
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < target:
                    # 关键：right-left个三元组都满足条件
                    # (i, left, left+1), (i, left, left+2), ..., (i, left, right)
                    count += right - left
                    left += 1
                else:
                    # 和太大，右指针左移
                    right -= 1

        return count
```

### 方法2：优化的双指针（带剪枝）

添加剪枝优化，避免不必要的计算。

```python
from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        带剪枝优化的双指针

        时间复杂度：O(n²)
        空间复杂度：O(1)
        """
        count = 0
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            # 剪枝1：如果最小的三个数之和已经 >= target，后面都不满足
            if nums[i] + nums[i + 1] + nums[i + 2] >= target:
                break

            # 剪枝2：如果当前数和最大的两个数之和 < target，全部计入
            if nums[i] + nums[n - 2] + nums[n - 1] < target:
                # 剩余 (n-1-i) 个数，选2个的组合数
                count += (n - 1 - i) * (n - 2 - i) // 2
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count
```

### 方法3：二分搜索优化

对于每个 (i, j) 对，用二分查找满足条件的最大 k。

```python
from typing import List
import bisect

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        二分搜索优化

        时间复杂度：O(n² log n)
        空间复杂度：O(1)
        """
        count = 0
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                # 需要找满足 nums[k] < target - nums[i] - nums[j] 的最大k
                remainder = target - nums[i] - nums[j]

                # 在 [j+1, n) 范围内二分查找第一个 >= remainder 的位置
                left, right = j + 1, n
                while left < right:
                    mid = (left + right) // 2
                    if nums[mid] < remainder:
                        left = mid + 1
                    else:
                        right = mid

                # [j+1, left) 范围内的所有k都满足条件
                count += left - j - 1

        return count
```

## 算法分析

### 核心思想详解

**为什么排序后可以用双指针？**

排序后数组单调递增，当 `nums[i] + nums[left] + nums[right] < target` 时：

```text
nums[i] + nums[left] + nums[left+1] < target
nums[i] + nums[left] + nums[left+2] < target
...
nums[i] + nums[left] + nums[right] < target
```

所有 `(i, left, left+1)`, `(i, left, left+2)`, ..., `(i, left, right)`
共 `right - left` 个三元组都满足条件。

**关键计数逻辑**：

```python
if total < target:
    count += right - left  # 一次性计入多个三元组
    left += 1
```

**为什么不是 `count += 1`？**

可视化示例：

```text
nums = [-2, 0, 1, 3], target = 2
i = 0 (nums[i] = -2)

left = 1, right = 3: -2 + 0 + 3 = 1 < 2
  满足的三元组：(-2, 0, 1), (-2, 0, 3)
  数量：right - left = 3 - 1 = 2
```

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 排序+双指针 | O(n²) | O(1) | 最优解 |
| 带剪枝优化 | O(n²) | O(1) | 常数优化 |
| 二分搜索 | O(n² log n) | O(1) | 可读性好 |

### 执行过程示例

以 `nums = [-2, 0, 1, 3]`, `target = 2` 为例：

**初始状态**：

```text
排序后：[-2, 0, 1, 3]
target = 2
```

**i = 0 (nums[i] = -2)**：

```text
left = 1, right = 3
total = -2 + 0 + 3 = 1 < 2
  满足：(-2, 0, 1), (-2, 0, 3)
  count += 3 - 1 = 2
  count = 2
  left = 2

left = 2, right = 3
total = -2 + 1 + 3 = 2 >= 2
  不满足
  right = 2

left = 2, right = 2 (退出循环)
```

**i = 1 (nums[i] = 0)**：

```text
left = 2, right = 3
total = 0 + 1 + 3 = 4 >= 2
  不满足
  right = 2

left = 2, right = 2 (退出循环)
```

**i = 2**：已到达 n-2，外层循环结束

**最终结果**：`count = 2`

**可视化表格**：

| i | left | right | nums[i] | nums[left] | nums[right] | total | 操作 | count |
|---|------|-------|---------|------------|-------------|-------|------|-------|
| 0 | 1 | 3 | -2 | 0 | 3 | 1 | +2 | 2 |
| 0 | 2 | 3 | -2 | 1 | 3 | 2 | right-- | 2 |
| 0 | 2 | 2 | - | - | - | - | 退出 | 2 |
| 1 | 2 | 3 | 0 | 1 | 3 | 4 | right-- | 2 |
| 1 | 2 | 2 | - | - | - | - | 退出 | 2 |

## 常见错误

### 错误1：忘记排序

```python
# 错误：未排序直接使用双指针
def threeSumSmaller(self, nums, target):
    count = 0
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        # 双指针逻辑依赖单调性！

# 正确：先排序
nums.sort()
```

### 错误2：计数逻辑错误

```python
# 错误：只加1
if total < target:
    count += 1  # 只统计了一个三元组
    left += 1

# 正确：加 right - left
if total < target:
    count += right - left  # 统计所有满足条件的
    left += 1
```

### 错误3：边界条件未处理

```python
# 错误：数组长度不足时未判断
for i in range(n - 2):
    ...
# n < 3 时会导致 range(负数)

# 正确：提前检查
if n < 3:
    return 0
```

### 错误4：指针移动逻辑错误

```python
# 错误：total >= target 时移动 left
if total >= target:
    left += 1  # 应该减小和，但left移动会增大和

# 正确：移动 right
if total >= target:
    right -= 1  # 减小和
```

### 错误5：重复计数

```python
# 错误：内层循环继续计数
if total < target:
    count += right - left
    for k in range(left + 1, right + 1):  # 重复计数
        count += 1

# 正确：一次性计入
count += right - left
left += 1
```

### 错误6：剪枝条件错误

```python
# 错误：条件判断反了
if nums[i] + nums[i+1] + nums[i+2] < target:
    break  # 应该是 >= target 时才break

# 正确
if nums[i] + nums[i+1] + nums[i+2] >= target:
    break
```

## 相关题目

- [0001. Two Sum](./001_two_sum.md) - 两数之和
- [0015. 3Sum](./015_3sum.md) - 三数之和等于0
- [0016. 3Sum Closest](./016_3sum_closest.md) - 最接近的三数之和
- [0018. 4Sum](./018_4sum.md) - 四数之和
- [0611. Valid Triangle Number](./611_valid_triangle_number.md) - 三角形计数，类似思想
