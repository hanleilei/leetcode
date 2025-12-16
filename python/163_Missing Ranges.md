# 163. Missing Ranges

## 问题描述

You are given an inclusive range `[lower, upper]` and a sorted
unique integer array `nums`, where all elements are within the
inclusive range.

A number `x` is considered **missing** if `x` is in the range
`[lower, upper]` and `x` is not in `nums`.

Return the **shortest sorted list of ranges** that exactly covers
all the missing numbers. That is, no element of `nums` is included
in any of the ranges, and each missing number is covered by one of
the ranges.

## 示例

**Example 1:**

```text
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
```

Explanation: The ranges are:

- `[2,2]` - 缺失数字 2
- `[4,49]` - 缺失数字 4 到 49
- `[51,74]` - 缺失数字 51 到 74
- `[76,99]` - 缺失数字 76 到 99

**Example 2:**

```text
Input: nums = [-1], lower = -1, upper = -1
Output: []
```

Explanation: There are no missing ranges since there are no missing
numbers.

**Example 3:**

```text
Input: nums = [], lower = 1, upper = 1
Output: [[1,1]]
```

## 约束条件

- $-10^9 \le \text{lower} \le \text{upper} \le 10^9$
- $0 \le \text{nums.length} \le 100$
- $\text{lower} \le \text{nums}[i] \le \text{upper}$
- All the values of `nums` are **unique**

## 解法

### 方法1：虚拟哨兵节点 推荐

在数组首尾添加虚拟节点，统一处理边界情况。

```python
from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        """
        虚拟哨兵节点法

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        result = []
        # 添加虚拟节点：lower-1 和 upper+1
        prev = lower - 1
        nums.append(upper+1)

        for num in nums:
            # 计算与前一个数的差距
            diff = num - prev

            if diff == 2:
                # 缺失一个数字
                result.append([prev + 1, prev + 1])
            elif diff > 2:
                # 缺失多个数字
                result.append([prev + 1, num - 1])

            prev = num

        return result
```

### 方法2：逐对比较（不修改原数组）

不修改原数组，通过比较相邻元素找缺失区间。

```python
from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        """
        逐对比较法

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        result = []

        # 处理nums为空的情况
        if not nums:
            return [[lower, upper]]

        # 检查lower到第一个数之间的缺失
        if nums[0] > lower:
            result.append([lower, nums[0] - 1])

        # 检查相邻数字之间的缺失
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                result.append([nums[i] + 1, nums[i + 1] - 1])

        # 检查最后一个数到upper之间的缺失
        if nums[-1] < upper:
            result.append([nums[-1] + 1, upper])

        return result
```

### 方法3：统一区间处理

使用统一的函数处理所有区间。

```python
from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        """
        统一区间处理法

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        def add_range(start: int, end: int) -> None:
            """添加缺失区间"""
            if start <= end:
                result.append([start, end])

        result = []
        prev = lower - 1

        for num in nums:
            # 添加prev+1到num-1的区间
            add_range(prev + 1, num - 1)
            prev = num

        # 添加最后一个区间
        add_range(prev + 1, upper)

        return result
```

### 方法4：双指针

使用指针遍历，明确标记当前期望的数字。

```python
from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        """
        双指针法

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        result = []
        expected = lower  # 当前期望的数字

        for num in nums:
            if num < expected:
                # 跳过小于期望的数字
                continue
            elif num == expected:
                # 找到期望的数字，期望下一个
                expected += 1
            else:
                # 发现缺失区间
                result.append([expected, num - 1])
                expected = num + 1

        # 处理最后的缺失区间
        if expected <= upper:
            result.append([expected, upper])

        return result
```

## 算法分析

### 核心思想详解

这道题的关键在于找到**相邻两个存在数字之间的空隙**。

**三个关键区间**：

1. **起始区间**：`[lower, nums[0]-1]`
2. **中间区间**：`[nums[i]+1, nums[i+1]-1]`
3. **结尾区间**：`[nums[-1]+1, upper]`

**虚拟哨兵的妙处**：

添加 `lower-1` 和 `upper+1` 作为虚拟节点，可以统一处理所有情况：

```python
# 原数组：[0, 1, 3, 50, 75]
# 添加哨兵后：[-1, 0, 1, 3, 50, 75, 100]
#            ↑虚拟                    ↑虚拟

# 遍历时：
# -1 → 0: diff=1, 无缺失
# 0 → 1: diff=1, 无缺失
# 1 → 3: diff=2, 缺失[2,2]
# 3 → 50: diff=47, 缺失[4,49]
# ...
```

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 虚拟哨兵 | O(n) | O(1) | 最简洁 |
| 逐对比较 | O(n) | O(1) | 不修改数组 |
| 统一处理 | O(n) | O(1) | 代码清晰 |
| 双指针 | O(n) | O(1) | 易理解 |

所有方法的空间复杂度都是 O(1)（不计算输出数组）。

### 执行过程示例

以 `nums = [0,1,3,50,75], lower = 0, upper = 99` 为例：

**虚拟哨兵法执行过程：**

初始状态：

```text
prev = -1 (lower - 1)
nums_extended = [0, 1, 3, 50, 75, 100]
result = []
```

**Step 1**：处理 num = 0

```text
diff = 0 - (-1) = 1
diff <= 1，无缺失
prev = 0
```

**Step 2**：处理 num = 1

```text
diff = 1 - 0 = 1
diff <= 1，无缺失
prev = 1
```

**Step 3**：处理 num = 3

```text
diff = 3 - 1 = 2
diff == 2，缺失一个数字
result.append([2, 2])
prev = 3
result = [[2, 2]]
```

**Step 4**：处理 num = 50

```text
diff = 50 - 3 = 47
diff > 2，缺失多个数字
result.append([4, 49])
prev = 50
result = [[2, 2], [4, 49]]
```

**Step 5**：处理 num = 75

```text
diff = 75 - 50 = 25
diff > 2，缺失多个数字
result.append([51, 74]]
prev = 75
result = [[2, 2], [4, 49], [51, 74]]
```

**Step 6**：处理 num = 100（虚拟节点）

```text
diff = 100 - 75 = 25
diff > 2，缺失多个数字
result.append([76, 99])
prev = 100
result = [[2, 2], [4, 49], [51, 74], [76, 99]]
```

**可视化**：

```text
Range: [0 ............................ 99]
nums:   0 1   3         50      75
        ↓ ↓   ↓         ↓       ↓
存在:   √ √   √         √       √
缺失:       [2]  [4..49]  [51..74] [76..99]
```

## 常见错误

### 错误1：忘记处理边界情况

```python
# 错误：没有处理lower之前和upper之后
for i in range(len(nums) - 1):
    if nums[i + 1] - nums[i] > 1:
        result.append([nums[i] + 1, nums[i + 1] - 1])

# 正确：处理所有边界
if nums[0] > lower:
    result.append([lower, nums[0] - 1])
for i in range(len(nums) - 1):
    ...
if nums[-1] < upper:
    result.append([nums[-1] + 1, upper])
```

### 错误2：差值判断错误

```python
# 错误：diff为1时也添加区间
if diff >= 2:
    result.append([prev + 1, num - 1])

# 正确：diff为1说明连续，没有缺失
if diff == 2:
    result.append([prev + 1, prev + 1])  # 单个数字
elif diff > 2:
    result.append([prev + 1, num - 1])   # 多个数字
```

### 错误3：区间端点计算错误

```python
# 错误：区间端点不对
result.append([prev, num])  # 应该是prev+1和num-1

# 正确：
result.append([prev + 1, num - 1])
```

### 错误4：修改了输入数组

```python
# 错误：修改了输入（可能导致问题）
nums.append(upper + 1)

# 正确：使用新列表或不修改原数组
nums_extended = nums + [upper + 1]
# 或者不添加，单独处理
```

### 错误5：空数组处理不当

```python
# 错误：空数组时访问nums[0]会报错
if nums[0] > lower:
    ...

# 正确：先检查是否为空
if not nums:
    return [[lower, upper]]
if nums[0] > lower:
    ...
```

### 错误6：单个缺失数字的表示

```python
# 错误：单个数字表示为[num]
if diff == 2:
    result.append([prev + 1])

# 正确：表示为[num, num]
if diff == 2:
    result.append([prev + 1, prev + 1])
```

## 相关题目

- [0163. Missing Ranges](./163_Missing Ranges.md)
- [0228. Summary Ranges](./228_summary_ranges.md) - 总结区间
- [0057. Insert Interval](./057_insert_interval.md) - 插入区间
- [0056. Merge Intervals](./056_merge_intervals.md) - 合并区间
- [0352. Data Stream as Disjoint Intervals](./352_data_stream_as_disjoint_intervals.md) - 数据流的不相交区间
