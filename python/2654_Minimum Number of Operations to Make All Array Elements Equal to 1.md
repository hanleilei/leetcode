# Minimum Number of Operations to Make All Array Elements Equal to 1

[[greedy]]

## Problem Description

You are given a 0-indexed array `nums` consisting of positive integers.
You can do the following operation on the array any number of times:

- Select an index `i` such that `0 <= i < n - 1` and replace either
  `nums[i]` or `nums[i+1]` with their GCD value.

Return the minimum number of operations to make all elements of `nums`
equal to 1. If it is impossible, return -1.

The GCD of two integers is the greatest common divisor of the two integers.

### Examples

**Example 1:**

```text
Input: nums = [2,6,3,4]
Output: 4

Explanation:
- Step 1: gcd(3,4) = 1, replace nums[2] → [2,6,1,4]
- Step 2: gcd(6,1) = 1, replace nums[1] → [2,1,1,4]
- Step 3: gcd(2,1) = 1, replace nums[0] → [1,1,1,4]
- Step 4: gcd(1,4) = 1, replace nums[3] → [1,1,1,1]
```

**Example 2:**

```text
Input: nums = [2,10,6,14]
Output: -1

Explanation: 
It can be shown that it is impossible to make all elements equal to 1.
All numbers are even, so GCD will always be >= 2.
```

### Constraints

- 2 <= nums.length <= 50
- 1 <= nums[i] <= 10^6

---

## 解法：枚举最短区间 + 贪心扩展（最优✨）

```python
from math import gcd
from typing import List

class Solution:
    """
    核心思想：
    1. 如果数组中已有1，直接把其他元素变成1（n-num1次）
    2. 如果全局GCD>1，永远无法得到1
    3. 否则，找最短的GCD为1的子数组，然后扩展到整个数组
    """
n g    
    def minOperations(self, nums: List[int]) -> int:
        """
        时间复杂度：O(n^2 * log(max(nums)))
        空间复杂度：O(1)
        """
        n = len(nums)
        num1 = 0  # 统计1的个数
        g = 0     # 全局GCD

        # 第一遍扫描：统计1和全局GCD
        for x in nums:
            if x == 1:
                num1 += 1
            g = gcd(g, x)

        # 情况1：数组中已经有1
        # 只需要把其他非1的元素都变成1
        if num1 > 0:
            return n - num1

        # 情况2：全局GCD > 1
        # 说明所有数都有公因子，永远无法得到1
        if g > 1:
            return -1

        # 情况3：找最短的GCD为1的连续子数组
        min_len = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    # 找到了GCD为1的子数组
                    min_len = min(min_len, j - i + 1)
                    break

        # 总操作数 = 子数组变成1的操作数 + 扩展到整个数组的操作数
        # = (min_len - 1) + (n - 1)
        # = min_len + n - 2
        return min_len + n - 2
```

### 算法分析

```text
为什么是 min_len + n - 2？

假设最短区间长度为 L，数组长度为 n：

1️⃣ 将长度为L的区间变成1：需要 L-1 次操作
   例：[3,4] → gcd(3,4)=1 → 1次
       [2,3,4] → [2,1,4] → [1,1,4] → 2次

2️⃣ 有了1之后，扩展到整个数组：需要 n-1 次操作
   每个非1的元素都能通过与1做GCD变成1
   
总计：(L-1) + (n-1) = L + n - 2

例：nums = [2,6,3,4], n=4
    最短区间 [3,4] 的GCD=1，L=2
    答案 = 2 + 4 - 2 = 4 ✓
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n² log(max(nums))) |
| 空间复杂度 | O(1) |
| 关键技巧 | 枚举区间 + 贪心 |

---

## 执行流程示例

```text
Example: nums = [2,6,3,4]

步骤1：检查是否有1
  num1 = 0 ❌

步骤2：检查全局GCD
  gcd(2,6,3,4) = gcd(gcd(gcd(2,6),3),4) = 1 ✓
  
步骤3：枚举所有区间找最短GCD=1
  [2]     → gcd=2 ✗
  [2,6]   → gcd=2 ✗
  [2,6,3] → gcd=1 ✓ len=3
  [6]     → gcd=6 ✗
  [6,3]   → gcd=3 ✗
  [6,3,4] → gcd=1 ✓ len=3
  [3]     → gcd=3 ✗
  [3,4]   → gcd=1 ✓ len=2 ← 最短
  [4]     → gcd=4 ✗
  
  min_len = 2

步骤4：计算答案
  min_len + n - 2 = 2 + 4 - 2 = 4
```

---

## 三种情况总结

### 情况1：数组已有1

```python
nums = [2,1,4,6]
# num1 = 1，直接返回 n - num1 = 4 - 1 = 3
# 操作：1和2 → 1, 1和4 → 1, 1和6 → 1
```

### 情况2：全局GCD > 1（无解）

```python
nums = [2,10,6,14]
# 全局GCD = 2，永远无法得到1
# 返回 -1
```

### 情况3：需要先制造1

```python
nums = [2,6,3,4]
# 找最短区间 [3,4]，GCD=1，长度=2
# 答案 = 2 + 4 - 2 = 4
```

---

## 常见错误

### 错误1：只检查全局GCD

```python
# ❌ 错误
if gcd_all == 1:
    return n - 1  # 错误！不是简单的n-1
    
# ✓ 正确
# 需要找最短区间，答案是 min_len + n - 2
```

### 错误2：忘记处理已有1的情况

```python
# ❌ 错误
# 直接枚举区间，没有快速处理已有1的case

# ✓ 正确
if num1 > 0:
    return n - num1
```

### 错误3：区间枚举不完整

```python
# ❌ 错误
for i in range(n-1):
    g = gcd(nums[i], nums[i+1])  # 只检查相邻元素
    
# ✓ 正确
for i in range(n):
    g = 0
    for j in range(i, n):
        g = gcd(g, nums[j])  # 检查所有可能的子数组
```

---

## 复杂度对比

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|----------|----------|------|
| 暴力模拟 | O(n³) | O(1) | 每次操作模拟 |
| **枚举区间** | **O(n² log M)** | **O(1)** | **最优** |
| 优化GCD | O(n log M) | O(n) | 预处理前缀GCD |

---

## 相关题目

- [[914. X of a Kind in a Deck of Cards]] - 卡牌分组（GCD应用）
- [[1071. Greatest Common Divisor of Strings]] - 字符串的最大公因子
- [[1979. Find Greatest Common Divisor of Array]] - 数组的最大公约数
- [[2427. Number of Common Factors]] - 公因子的个数
- [[365. Water and Jug Problem]] - 水壶问题（GCD经典应用）
