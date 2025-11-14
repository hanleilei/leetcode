# Maximum Number of Operations to Move Ones to the End

[[simulation]] [[greedy]] [[math]]

## Problem Description

You are given a binary string `s`.

You can perform the following operation on the string any number of times:

- Choose any index `i` from the string where `i + 1 < s.length` such that
  `s[i] == '1'` and `s[i + 1] == '0'`
- Move the character `s[i]` to the right until it reaches the end of the
  string or another '1'

Return the maximum number of operations that you can perform.

### Examples

**Example 1:**

```text
Input: s = "1001101"
Output: 4

Explanation:
- Operation 1: i=0, "1001101" → "0011101" (move first 1)
- Operation 2: i=4, "0011101" → "0011011" (move 1 at pos 4)
- Operation 3: i=3, "0011011" → "0010111" (move 1 at pos 3)
- Operation 4: i=2, "0010111" → "0001111" (move 1 at pos 2)
Total: 4 operations
```

**Example 2:**

```text
Input: s = "00111"
Output: 0

Explanation: All 1s are already at the end, no operations needed.
```

### Constraints

- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'

---

## 解法1：分组统计 + 贪心（最优✨）

```python
class Solution:
    """
    核心思想：
    1. 将字符串按0分组，得到若干个连续的1的片段
    2. 每个1片段需要跨越后面所有的0-group才能到达末尾
    3. 每个1需要移动的次数 = 它后面有多少个0-group
    """
    def maxOperations(self, s: str) -> int:
        """
        时间复杂度：O(n)
        空间复杂度：O(k) - k为1的片段数
        """
        # 按0分割，得到所有1的片段
        ones = [group for group in s.split("0") if group != ""]

        # 特殊处理：如果末尾是0，需要额外计数
        # 因为末尾的0也算一个需要跨越的gap
        if s[-1] == "0":
            ones.append('1')

        res = 0
        n = len(ones)

        # 每个1片段需要跨越后面所有的0-group
        for i in range(n):
            # ones[i]中每个1都要移动(n-i-1)次
            res += len(ones[i]) * (n - i - 1)

        return res
```

### 算法分析

```text
核心观察：每个1需要移动的次数 = 它后面有多少个0-group

例：s = "1001101"

分组：按0分割
  "1" "0" "0" "11" "0" "1"
  ↓
  ones = ["1", "11", "1"]
  
末尾是1，不需要额外添加

计算每组的贡献：
  - ones[0]="1"：  1个1 × 2个后续group = 2
  - ones[1]="11"： 2个1 × 1个后续group = 2  
  - ones[2]="1"：  1个1 × 0个后续group = 0
  
总计：2 + 2 + 0 = 4 ✓
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n) |
| 空间复杂度 | O(k) - k为1片段数 |
| 关键技巧 | 分组统计 |

---

## 解法2：单次遍历（空间优化）

```python
class Solution:
    def maxOperations(self, s: str) -> int:
        """
        一次遍历统计，不需要存储所有片段
        
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        res = 0
        ones_count = 0  # 当前累计的1的个数
        
        for i in range(len(s)):
            if s[i] == '1':
                ones_count += 1
            # 关键：遇到0且后面还有字符时
            # 前面所有的1都需要跨越这个0
            elif i + 1 < len(s) and s[i + 1] == '1':
                res += ones_count
        
        return res
```

### 优化思路

```text
不需要存储所有片段，只需统计：
- 遇到1：累加计数
- 遇到"10"模式：前面所有1都要跨越这个0

例：s = "1001101"
     ↓
i=0, s[0]='1': ones_count=1
i=1, s[1]='0', s[2]='0': 不处理
i=2, s[2]='0', s[3]='1': res += 1 (第一个1跨越)
i=3, s[3]='1': ones_count=2
i=4, s[4]='1': ones_count=3
i=5, s[5]='0', s[6]='1': res += 3 (3个1跨越)
i=6, s[6]='1': ones_count=4

结果：res = 1 + 3 = 4 ✓
```

---

## 执行流程示例

```text
Example: s = "1001101"

方法1（分组）：
  split by '0': ["1", "", "", "11", "", "1"]
  filter empty: ["1", "11", "1"]
  末尾='1'，不追加
  
  计算：
    i=0: len("1")×2 = 1×2 = 2
    i=1: len("11")×1 = 2×1 = 2
    i=2: len("1")×0 = 1×0 = 0
  
  总和：2+2+0 = 4

方法2（单次遍历）：
  i=0, '1': ones=1
  i=1, '0': skip
  i=2, '0', next='1': res+=1 (ones=1)
  i=3, '1': ones=2
  i=4, '1': ones=3
  i=5, '0', next='1': res+=3 (ones=3)
  i=6, '1': ones=4
  
  结果：res = 1+3 = 4
```

---

## 两种解法对比

| 方法 | 时间 | 空间 | 代码 | 说明 |
|------|------|------|------|------|
| 分组统计 | O(n) | O(k) | 简洁 | 直观易懂 |
| 单次遍历 | O(n) | O(1) | 略长 | 空间最优 |

---

## 常见错误

### 错误1：直接模拟每次操作

```python
# ❌ 超时
def maxOperations(self, s: str) -> int:
    count = 0
    s = list(s)
    while True:
        moved = False
        for i in range(len(s) - 1):
            if s[i] == '1' and s[i+1] == '0':
                # 移动操作...
                moved = True
                count += 1
        if not moved:
            break
    return count
# 问题：O(n²)时间复杂度
```

### 错误2：忽略末尾是0的情况

```python
# ❌ 错误
ones = [g for g in s.split("0") if g]
# 如果s="10"，应该是1次操作
# 但这样会得到0

# ✓ 正确
ones = [g for g in s.split("0") if g]
if s[-1] == "0":
    ones.append('1')  # 补上末尾的gap
```

### 错误3：重复计算

```python
# ❌ 错误
for i in range(len(s)):
    if s[i] == '1':
        # 计算这个1后面有多少个0
        zeros = s[i:].count('0')
        res += zeros
# 问题：会重复计算连续的1

# ✓ 正确
# 需要按组统计，或者只在"10"边界处计数
```

### 错误4：没有理解"10"模式的意义

```python
# ❌ 错误
for i in range(len(s)):
    if s[i] == '0':
        res += 1  # 简单地数0
        
# ✓ 正确
# 只有"10"模式才代表1需要跨越0
for i in range(len(s) - 1):
    if s[i] == '1' and s[i+1] == '0':
        res += ones_count
```

---

## 关键洞察

```text
问题转化：
  原问题：最多能执行多少次移动操作
  ↓
  转化为：每个1需要跨越多少个0-gap
  ↓
  等价于：统计所有(1的个数 × 后续0-gap数)
```

### 为什么这样等价？

1. 每个1最终都要移到最右边
2. 移动过程中，1遇到0就要跨越（算1次操作）
3. 多个连续的1作为整体移动，每个1独立计数
4. 所以答案 = Σ(每个1 × 它需要跨越的0-gap数)

---

## 相关题目

- [[283. Move Zeroes]] - 移动零（类似的移动问题）
- [[2486. Append Characters to String to Make Subsequence]] - 字符串操作
- [[2516. Take K of Each Character From Left and Right]] - 贪心策略
- [[2545. Sort the Students by Their Kth Score]] - 排序问题
- [[1525. Number of Good Ways to Split a String]] - 字符串分割

