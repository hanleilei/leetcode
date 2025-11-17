# 1513. Number of Substrings With Only 1s

## 问题描述

Given a binary string s, return the number of substrings with all
characters 1's. Since the answer may be too large, return it modulo
10^9 + 7.

## 示例

**Example 1:**

```text
Input: s = "0110111"
Output: 9
```

Explanation: There are 9 substrings in total with only 1's characters.

- "1" -> 5 times
- "11" -> 3 times
- "111" -> 1 time

**Example 2:**

```text
Input: s = "101"
Output: 2
```

Explanation: Substring "1" is shown 2 times in s.

**Example 3:**

```text
Input: s = "111111"
Output: 21
```

Explanation: Each substring contains only 1's characters.

## 约束条件

- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.

## 解法

### 方法1：数学公式法（推荐）

核心思想：对于连续的 k 个1，可以形成的子串数量为 k*(k+1)/2。
分别统计每段连续1的长度，然后累加贡献。

数学推导：连续 k 个1可以形成的子串：

- 长度为1的子串：k 个
- 长度为2的子串：k-1 个
- 长度为3的子串：k-2 个
- ...
- 长度为k的子串：1 个
- 总数 = 1 + 2 + 3 + ... + k = k*(k+1)/2

```python
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        count = 0  # 当前连续1的个数
        
        for ch in s + "0":  # 处理最后可能的连续 "1"
            if ch == '1':
                count += 1
            else:
                # 遇到0，结算前面连续的1
                res += count * (count + 1) // 2
                res %= MOD
                count = 0
        
        return res
```

### 方法2：增量累加法

另一种思路是每遇到一个1，就计算以它结尾的所有子串数量。
如果当前是第 k 个连续的1，则以它结尾的子串有 k 个。

```python
class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        one = 1  # 下一个1将是连续序列中的第几个
        MOD = 10**9 + 7
        
        # 在末尾添加'0'作为哨兵，统一处理逻辑
        for ch in s + "0":
            if ch == '1':
                res += one  # 以当前1结尾的子串有one个
                one += 1    # 下一个1将是第one+1个
            else:
                one = 1     # 重置计数器
            res %= MOD
        
        return res
```

### 方法3：分组统计

使用 groupby 或手动分组，统计每段连续1的长度，然后应用公式。

```python
from itertools import groupby

class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        
        # 按字符分组，统计连续1的长度
        for char, group in groupby(s):
            if char == '1':
                length = len(list(group))
                res += length * (length + 1) // 2
                res %= MOD
        
        return res
```

## 算法分析

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 数学公式法 | O(n) | O(1) | 一次遍历，常数空间 |
| 增量累加法 | O(n) | O(1) | 一次遍历，常数空间 |
| 分组统计 | O(n) | O(n) | groupby需要额外空间 |

数学公式详细分析：

- 时间：遍历字符串一次，每个字符处理 O(1)
- 空间：只用几个变量记录状态
- 取模操作：每次累加后取模，防止整数溢出

### 执行过程示例

以 s = "0110111" 为例（方法1）：

```text
初始：res=0, count=0

ch='0': count=0, 不累加
ch='1': count=1
ch='1': count=2
ch='0': 结算：res += 2*(2+1)/2 = 3, count=0
ch='1': count=1
ch='1': count=2
ch='1': count=3
最后：res += 3*(3+1)/2 = 3+6 = 9
```

以 s = "0110111" 为例（方法2）：

```text
初始：res=0, one=1

ch='0': one=1
ch='1': res+=1 (res=1), one=2
ch='1': res+=2 (res=3), one=3
ch='0': one=1
ch='1': res+=1 (res=4), one=2
ch='1': res+=2 (res=6), one=3
ch='1': res+=3 (res=9), one=4
ch='0': one=1 (哨兵)
```

子串分解：

- "0**11**0111"：2个连续1 -> "1"(2次) + "11"(1次) = 3个子串
- "011**0111**"：3个连续1 -> "1"(3次) + "11"(2次) + "111"(1次) = 6个子串
- 总计：3 + 6 = 9

## 常见错误

### 错误1：未处理最后一段连续1

```python
# 错误：遍历结束后没有结算最后一段
for ch in s:
    if ch == '1':
        count += 1
    else:
        res += count * (count + 1) // 2
        count = 0
# 缺少：res += count * (count + 1) // 2
return res
```

**原因：** 如果字符串以1结尾，最后一段不会被结算

### 错误2：忘记取模

```python
# 错误：只在最后取模
res += count * (count + 1) // 2
# 正确：每次累加后取模
res = (res + count * (count + 1) // 2) % MOD
```

**原因：** 中间结果可能超过整数范围

### 错误3：公式计算错误

```python
# 错误：忘记除以2
res += count * (count + 1)  # 应该是 count * (count + 1) // 2
```

**原因：** 等差数列求和公式是 n*(n+1)/2

### 错误4：增量法中计数器初始值错误

```python
# 错误：one从0开始
one = 0  # 应该是 one = 1
for ch in s:
    if ch == '1':
        res += one
        one += 1
```

**原因：** 第一个1应该贡献1个子串，不是0个

## 相关题目

- [0696. Count Binary Substrings](./696_count_binary_substrings.md)
- [1759. Count Number of Homogenous Substrings](./1759_count_number_of_homogenous_substrings.md)
- [2222. Number of Ways to Select Buildings](./2222_number_of_ways_to_select_buildings.md)
- [2062. Count Vowel Substrings of a String](./2062_count_vowel_substrings_of_a_string.md)
- [3234. Count the Number of Substrings With Dominant Ones](./3234_Count%20the%20Number%20of%20Substrings%20With%20Dominant%20Ones.md)

