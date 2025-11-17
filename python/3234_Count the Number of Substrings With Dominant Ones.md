# 3234. Count the Number of Substrings With Dominant Ones

## 问题描述

You are given a binary string s.

Return the number of substrings with dominant ones.

A string has dominant ones if the number of ones in the string is
greater than or equal to the square of the number of zeros in the
string.

**Dominant Ones 定义：** ones >= zeros²

## 示例

**Example 1:**

```text
Input: s = "00011"
Output: 5
```

Explanation: The substrings with dominant ones are shown in the table
below.

| i | j | s[i..j] | Number of Zeros | Number of Ones |
|---|---|---------|-----------------|----------------|
| 3 | 3 | 1       | 0               | 1              |
| 4 | 4 | 1       | 0               | 1              |
| 2 | 3 | 01      | 1               | 1              |
| 3 | 4 | 11      | 0               | 2              |
| 2 | 4 | 011     | 1               | 2              |

**Example 2:**

```text
Input: s = "101101"
Output: 16
```

Explanation: The substrings with non-dominant ones are shown in the
table below. Since there are 21 substrings total and 5 of them have
non-dominant ones, it follows that there are 16 substrings with
dominant ones.

| i | j | s[i..j] | Number of Zeros | Number of Ones |
|---|---|---------|-----------------|----------------|
| 1 | 1 | 0       | 1               | 0              |
| 4 | 4 | 0       | 1               | 0              |
| 1 | 4 | 0110    | 2               | 2              |
| 0 | 4 | 10110   | 2               | 3              |
| 1 | 5 | 01101   | 2               | 3              |

## 约束条件

- 1 <= s.length <= 4 * 10^4
- s consists only of characters '0' and '1'.

## 解法

### 方法1：枚举0的位置 + 数学优化（推荐）

核心思想：由于条件是 ones >= zeros²，当 zeros 很大时，需要的 ones
数量会指数级增长。因此可以枚举子串中包含的0的个数，然后计算满足
条件的子串数量。

关键观察：

- 当 zeros = k 时，需要 ones >= k²
- 对于长度 n <= 40000 的字符串，zeros 最多约 sqrt(n) ≈ 200 时
  就会因为需要过多的1而无法满足
- 因此可以枚举0的个数（最多 O(sqrt(n)) 种情况），每种情况下计算
  贡献

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 记录所有0的位置
        pos0 = [-1]  # 哨兵，方便计算左边界
        total = 0    # 当前累计的1的总数
        res = 0

        for r, ch in enumerate(s):
            if ch == '0':
                pos0.append(r)
            else:
                total += 1
                # 情况1：子串中没有0（全是1）
                # 从最后一个0的位置+1到当前位置r的所有子串
                res += r - pos0[-1]

            # 情况2：子串中包含k个0
            # 倒序枚举0的个数，从当前位置向左扩展
            for i in range(len(pos0) - 1, 0, -1):
                cnt0 = len(pos0) - i  # 从第i个0到最后的0的个数
                if cnt0 * cnt0 > total:
                    # 剪枝：需要的1太多，后面更多0的情况更不可能
                    break

                # p: 第(i-1)个0的位置, q: 第i个0的位置
                p, q = pos0[i - 1], pos0[i]
                # cnt1: 从q到r之间的1的个数
                cnt1 = r - q - cnt0 + 1

                # 需要满足：cnt1 + extra >= cnt0²
                # 其中extra是左边可以扩展的1的个数
                # 左边界最远可以到p+1，但需要满足条件
                need = max(cnt0 * cnt0 - cnt1, 0)
                # 左边可用的1的个数是 q - p - 1
                res += max(q - need - p, 0)

        return res
```

### 方法2：枚举左端点 + 0位置数组

另一种思路是枚举每个左端点，然后根据0的位置数组快速计算。

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        # 记录所有0的位置
        zeros = [i for i, ch in enumerate(s) if ch == '0']
        tot1 = n - len(zeros)  # 总的1的个数
        zeros.append(n)  # 哨兵

        ans = 0
        i = 0  # zeros数组的索引

        for left, ch in enumerate(s):
            # 枚举包含的0的个数
            for k in range(i, len(zeros) - 1):
                cnt0 = k - i + 1  # 从第i个0到第k个0
                if cnt0 * cnt0 > tot1:
                    # 剪枝
                    break

                # 从left到zeros[k]这段包含cnt0个0
                cnt1 = zeros[k] - left + 1 - cnt0

                # 右端点可以扩展到下一个0之前
                if cnt1 >= cnt0 * cnt0:
                    # 整个区间都满足
                    ans += zeros[k + 1] - zeros[k]
                else:
                    # 需要再补充一些1
                    ans += max(0, zeros[k + 1] - zeros[k] - 
                              (cnt0 * cnt0 - cnt1))

            if ch == '0':
                i += 1
            else:
                # 不包含0的情况
                ans += zeros[i] - left
                tot1 -= 1

        return ans
```

## 算法分析

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 枚举0位置 | O(n·sqrt(n)) | O(n) | 外层O(n)，内层最多O(sqrt(n)) |
| 枚举左端点 | O(n·sqrt(n)) | O(n) | 同样的分析 |

时间复杂度详细分析：关键在于证明内层循环的复杂度是 O(sqrt(n))：

- 当 cnt0 = k 时，需要至少 k² 个1
- 对于长度为 n 的字符串，最多有 n 个1
- 因此 k² <= n，即 k <= sqrt(n)
- 所以枚举0的个数最多 O(sqrt(n)) 种情况
- 总时间复杂度：O(n·sqrt(n))

### 执行过程示例

以 s = "00011" 为例。

初始状态：

- pos0 = [-1, 0, 1]
- 目标：统计所有满足 ones >= zeros² 的子串

遍历过程：

```text
r=0, ch='0': pos0=[-1,0], total=0
  无1，跳过

r=1, ch='0': pos0=[-1,0,1], total=0
  无1，跳过

r=2, ch='0': pos0=[-1,0,1,2], total=0
  无1，跳过

r=3, ch='1': pos0=[-1,0,1,2], total=1
  无0情况：res += 3-2=1  (子串"1")
  1个0：需要>=1个1，满足，贡献计算
  2个0：需要>=4个1，不满足

r=4, ch='1': pos0=[-1,0,1,2], total=2
  无0情况：res += 4-2=2  (子串"11", "1")
  1个0：可以有多个左端点
  2个0：可以有左端点
```

最终结果：res = 5

## 常见错误

### 错误1：暴力枚举所有子串（超时）

```python
# 错误：O(n²) 枚举 + O(n) 统计 = O(n³)
def numberOfSubstrings(self, s: str) -> int:
    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            zeros = s[i:j+1].count('0')
            ones = j - i + 1 - zeros
            if ones >= zeros * zeros:
                res += 1
    return res
```

**原因：** n=40000 时会超时

### 错误2：未考虑剪枝优化

```python
# 错误：枚举所有可能的0的个数
for k in range(len(pos0)):  # 应该在 k² > total 时 break
    cnt0 = k
    # ...
```

**原因：** 没有利用 zeros² 快速增长的特性进行剪枝

### 错误3：边界计算错误

```python
# 错误：未正确处理哨兵节点
pos0 = []  # 应该初始化为 [-1]
```

**原因：** 缺少哨兵导致边界情况计算错误

### 错误4：重复计数

```python
# 错误：没有正确区分"无0"和"有k个0"的情况
# 可能会把同一个子串计数多次
```

**原因：** 需要仔细设计枚举逻辑，避免重复

## 相关题目

- [0795. Number of Subarrays with Bounded Maximum](./795_number_of_subarrays_with_bounded_maximum.md)
- [1358. Number of Substrings Containing All Three Characters](./1358_number_of_substrings_containing_all_three_characters.md)
- [2302. Count Subarrays With Score Less Than K](./2302_count_subarrays_with_score_less_than_k.md)
- [2444. Count Subarrays With Fixed Bounds](./2444_count_subarrays_with_fixed_bounds.md)
- [2743. Count Substrings Without Repeating Character](./2743_count_substrings_without_repeating_character.md)
