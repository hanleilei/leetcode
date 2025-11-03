# Minimum Time to Make Rope Colorful

[[greedy]] [[dp]] [[2points]]

## Problem Description

Alice has `n` balloons arranged on a rope. You are given a 0-indexed string `colors` where `colors[i]` is the color of the `i`th balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array `neededTime` where `neededTime[i]` is the time (in seconds) that Bob needs to remove the `i`th balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

## Examples

**Example 1:**

```text
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: Remove the blue balloon at index 2. This takes 3 seconds. No more consecutive same color. Total time = 3.
```

**Example 2:**

```text
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. No need to remove any balloons.
```

**Example 3:**

```text
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Remove the balloons at indices 0 and 4. Each takes 1 second. Total time = 2.
```

## Constraints

- `n == colors.length == neededTime.length`
- `1 <= n <= 10^5`
- `1 <= neededTime[i] <= 10^4`
- `colors` contains only lowercase English letters.

---

## 解法一：贪心法（最优解）

**核心思想：**

对于连续相同颜色的气球，只保留一个，移除其余的，且每次移除代价最小的。

**代码实现：**

```python
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res, max_cost = 0, 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                max_cost = 0
            res += min(max_cost, neededTime[i])
            max_cost = max(max_cost, neededTime[i])
        return res
```

或者：

```python
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0          # 累加移除的总代价
        max_val = 0      # 当前颜色段中最大的neededTime
        l = ""           # 上一个气球的颜色

        for c, n in zip(colors, neededTime):
            if c == l:   # 当前气球和上一个气球颜色相同
                if n < max_val:
                    ans += n      # 移除当前气球，累加代价
                else:
                    ans += max_val  # 移除之前的最大气球，累加代价
                    max_val = n     # 更新最大neededTime为当前气球
            else:
                l = c
                max_val = n        # 新颜色段，重置最大neededTime
        return ans
```

**时间复杂度：** O(n)
**空间复杂度：** O(1)

---

## 解法二：双指针法

```python
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        left = 0
        for right in range(1, len(colors)):
            if colors[right] == colors[left]:
                if neededTime[right] >= neededTime[left]:
                    res += neededTime[left]
                    left = right
                else:
                    res += neededTime[right]
            else:
                left = right
        return res
```

**思路说明：**

- 用`left`指针指向当前连续颜色段的最大代价气球
- 每遇到相同颜色，移除较小代价的气球

---

## 解法三：分组求和法

```python
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        i = 0
        n = len(colors)
        while i < n:
            j = i
            total, max_cost = 0, 0
            while j < n and colors[j] == colors[i]:
                total += neededTime[j]
                max_cost = max(max_cost, neededTime[j])
                j += 1
            res += total - max_cost
            i = j
        return res
```

**思路说明：**

- 对每一段连续相同颜色，移除所有但保留最大代价的那个

---

## 算法分析

### 为什么贪心法最优？

- 每次只保留最大代价的气球，移除其余，保证总代价最小
- 只需一次遍历即可完成

### 复杂度对比

| 方法 | 时间复杂度 | 空间复杂度 | 优缺点 |
|------|------------|------------|--------|
| 贪心法 | O(n) | O(1) | ✅ 最优解 |
| 双指针 | O(n) | O(1) | 代码直观 |
| 分组法 | O(n) | O(1) | 逻辑清晰 |

---

## 相关题目

- [921. Minimum Add to Make Parentheses Valid](921_minimum_add_to_make_parentheses_valid.md)
- [1047. Remove All Adjacent Duplicates In String](1047_remove_all_adjacent_duplicates_in_string.md)
