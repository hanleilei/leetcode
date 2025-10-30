# Minimum Number of Increments on Subarrays to Form a Target Array

[[array]] [[greedy]] [[stack]]

## Problem Description

You are given an integer array `target`. You have an integer array `initial` of the same size as `target` with all elements initially zeros.

In one operation you can choose **any subarray** from `initial` and **increment each value by one**.

Return *the minimum number of operations to form a target array from initial*.

The test cases are generated so that the answer fits in a 32-bit integer.

## Examples

**Example 1:**

```text
Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.
```

**Example 2:**

```text
Input: target = [3,1,1,2]
Output: 4
Explanation: [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]
```

**Example 3:**

```text
Input: target = [3,1,5,4,2]
Output: 7
Explanation: [0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2].
```

## Constraints

- `1 <= target.length <= 10^5`
- `1 <= target[i] <= 10^5`

## 解法一：贪心算法（最优解）

```python
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        贪心策略：从左到右遍历，计算增量操作
        时间复杂度：O(n)，空间复杂度：O(1)
        """
        operations = 0
        prev_height = 0
        
        for current_height in target:
            if current_height > prev_height:
                # 需要增加操作次数
                operations += current_height - prev_height
            # 更新前一个位置的高度
            prev_height = current_height
        
        return operations
```

或者单行版本：

```python
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return sum(max(b - a, 0) for b, a in zip(target, [0] + target))
```

### 算法思路

**核心思想**：将问题视为构建"高度图"，每次操作相当于在某个区间上增加一层。

**关键洞察**：

1. **从左到右贪心**：当遇到比前一个位置更高的值时，必须进行额外操作
2. **高度差累积**：每次增高操作的次数等于当前高度与前一个高度的差值
3. **下降不增加成本**：从高处到低处不需要额外操作，之前的操作已经覆盖

### 算法演示

以 `target = [1,2,3,2,1]` 为例：

```text
初始: prev_height = 0, operations = 0

位置0: current_height = 1
- 1 > 0, operations += 1-0 = 1
- prev_height = 1

位置1: current_height = 2  
- 2 > 1, operations += 2-1 = 1, total = 2
- prev_height = 2

位置2: current_height = 3
- 3 > 2, operations += 3-2 = 1, total = 3
- prev_height = 3

位置3: current_height = 2
- 2 < 3, 不增加操作
- prev_height = 2

位置4: current_height = 1
- 1 < 2, 不增加操作
- prev_height = 1

最终结果: 3
```

### 可视化理解

将数组看作"建筑物高度图"：

```text
target = [1,2,3,2,1]

可视化:
    3
  2 3 2
1 2 3 2 1

从左到右建设:
- 第1次操作: 整个区域加1层 [1,1,1,1,1]
- 第2次操作: 位置1-3加1层    [1,2,2,2,1]  
- 第3次操作: 位置2加1层      [1,2,3,2,1]
```

**复杂度分析**：

- 时间复杂度：O(n) - 单次遍历数组
- 空间复杂度：O(1) - 只使用常数额外空间

## 解法二：栈解法

```python
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        使用栈模拟操作过程
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        stack = [0]  # 哨兵，简化边界处理
        operations = 0
        
        for height in target + [0]:  # 添加哨兵简化处理
            while stack and stack[-1] > height:
                # 当前高度下降，之前的"山峰"需要额外操作
                prev_height = stack.pop()
                operations += prev_height - max(stack[-1], height)
            stack.append(height)
        
        return operations
```

### 核心思想

**核心思想**：使用单调栈维护"山峰"，当遇到下降时计算需要的额外操作。

**复杂度分析**：

- 时间复杂度：O(n) - 每个元素最多入栈出栈一次
- 空间复杂度：O(n) - 栈的空间

## 解法三：分治思想

```python
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        分治递归解法
        时间复杂度：O(n log n)，空间复杂度：O(log n)
        """
        def solve(arr, base):
            if not arr:
                return 0
            
            min_val = min(arr)
            operations = min_val - base
            
            # 分割数组，递归处理各段
            i = 0
            while i < len(arr):
                start = i
                # 找到连续的非最小值段
                while i < len(arr) and arr[i] > min_val:
                    i += 1
                # 递归处理该段
                operations += solve(arr[start:i], min_val)
                i += 1
            
            return operations
        
        return solve(target, 0)
```

### 分治思想

**核心思想**：每次找到数组的最小值，先进行全局操作到最小值，然后递归处理剩余部分。

**复杂度分析**：

- 时间复杂度：O(n log n) - 递归深度和数组处理
- 空间复杂度：O(log n) - 递归调用栈

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 贪心算法 | O(n) | O(1) | 最优解，简洁高效 |
| 栈解法 | O(n) | O(n) | 思路清晰，便于理解 |
| 分治解法 | O(n log n) | O(log n) | 递归思维，复杂度较高 |

## 边界情况处理

1. **单个元素**：直接返回该元素值
2. **严格递增数组**：每个位置都需要额外操作
3. **严格递减数组**：只需要第一个元素值的操作
4. **平坦数组**：只需要该值的操作次数

## 关键要点

1. **贪心策略**：从左到右处理，遇到上升就累加差值
2. **高度图思维**：将数组看作建筑物高度，操作就是分层建设
3. **差值累积**：只有上升时才需要额外操作
4. **一次遍历**：贪心算法只需要一次遍历即可得到最优解

## 常见错误

1. **过度复杂化**：试图模拟每个操作步骤而不是数学分析
2. **忽略下降**：没有理解下降时不需要额外操作
3. **边界处理**：没有正确处理数组开头和结尾
4. **理解偏差**：没有将问题抽象为高度图构建

## 算法扩展

1. **二维情况**：如果是二维数组该如何处理？
2. **操作限制**：如果每次操作有长度限制？
3. **不同操作**：如果可以进行减法操作？

## 相关题目

- [42. Trapping Rain Water](042_trapping_rain_water.md) - 接雨水
- [84. Largest Rectangle in Histogram](084_largest_rectangle_in_histogram.md) - 柱状图中最大的矩形
- [1793. Maximum Score of a Good Subarray](1793_maximum_score_of_a_good_subarray.md) - 好子数组的最大分数

这道题展示了如何通过贪心思维将复杂的操作问题转换为简单的数学计算。
