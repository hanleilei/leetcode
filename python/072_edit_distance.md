# 72. Edit Distance

## 问题描述

Given two words word1 and word2, find the minimum number of
operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

## 示例

**Example 1:**

```text
Input: word1 = "horse", word2 = "ros"
Output: 3
```

Explanation:

- horse -> rorse (replace 'h' with 'r')
- rorse -> rose (remove 'r')
- rose -> ros (remove 'e')

**Example 2:**

```text
Input: word1 = "intention", word2 = "execution"
Output: 5
```

Explanation:

- intention -> inention (remove 't')
- inention -> enention (replace 'i' with 'e')
- enention -> exention (replace 'n' with 'x')
- exention -> exection (replace 'n' with 'c')
- exection -> execution (insert 'u')

## 约束条件

- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.

## 解法分析

这是一个经典的动态规划问题，也被称为编辑距离（Levenshtein
Distance）。

### 核心思路

定义 $dp[i][j]$ 表示将 word1 的前 i 个字符转换为 word2 的前 j
个字符所需的最少操作数。

状态转移方程：

1. 如果 $word1[i-1] = word2[j-1]$，字符相同：
   - $dp[i][j] = dp[i-1][j-1]$

2. 如果字符不同，取三种操作的最小值：
   - 插入：$dp[i][j] = dp[i][j-1] + 1$
   - 删除：$dp[i][j] = dp[i-1][j] + 1$
   - 替换：$dp[i][j] = dp[i-1][j-1] + 1$

边界条件：

- $dp[0][j] = j$（word1为空，需要插入j个字符）
- $dp[i][0] = i$（word2为空，需要删除i个字符）

参考资料：[GeeksforGeeks - Edit Distance](https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/)

## 解法

### 方法1：二维DP（推荐）

标准的动态规划解法，清晰易懂。自底向上

列出状态转移方程：

$$
[
cnt_{i,j} =
\begin{cases}
    0, & \text{if } i = 0 \text{ and } j = 0 \\
    j, & \text{if } i = 0 \\
    i, & \text{if } j = 0 \\
    cnt_{i-1,j-1}, & \text{if } word1[i-1] = word2[j-1] \\
    \min(cnt_{i-1,j}, cnt_{i,j-1}, cnt_{i-1,j-1}) + 1  & \text{if } word1[i-1] \neq word2[j-1]
\end{cases}
]
$$

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # 创建DP表，dp[i][j]表示word1前i个字符转换为word2前j个字符的最小操作数
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化边界条件
        for i in range(m + 1):
            dp[i][0] = i  # word2为空，需要删除i个字符
        for j in range(n + 1):
            dp[0][j] = j  # word1为空，需要插入j个字符

        # 填充DP表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 字符相同，不需要操作
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 字符不同，取三种操作的最小值
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,      # 删除word1[i]
                        dp[i][j - 1] + 1,      # 插入word2[j]
                        dp[i - 1][j - 1] + 1   # 替换word1[i]为word2[j]
                    )

        return dp[m][n]
```

### 方法2：空间优化的DP

由于 $dp[i][j]$ 只依赖于 $dp[i-1][j-1]$、$dp[i-1][j]$ 和 $dp[i][j-1]$，可以将空间复杂度优化到O(n)。

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # 只使用一维数组
        dp = list(range(n + 1))

        for i in range(1, m + 1):
            prev = dp[0]  # 保存dp[i-1][j-1]
            dp[0] = i

            for j in range(1, n + 1):
                temp = dp[j]  # 保存当前值，作为下一次的prev

                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1

                prev = temp

        return dp[n]
```

### 方法3：记忆化递归（DFS + Memo）

自顶向下的递归方法，使用记忆化避免重复计算。

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            # 记忆化
            if (i, j) in memo:
                return memo[(i, j)]

            # 边界条件
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            # 字符相同，无需操作
            if word1[i] == word2[j]:
                result = dfs(i + 1, j + 1)
            else:
                # 三种操作取最小值
                result = min(
                    dfs(i + 1, j + 1),  # 替换
                    dfs(i + 1, j),      # 删除
                    dfs(i, j + 1)       # 插入
                ) + 1

            memo[(i, j)] = result
            return result

        return dfs(0, 0)
```

或者：

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(s), len(t)
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if s[i] == t[j]:
                return dfs(i - 1, j - 1)
            return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1
        return dfs(n - 1, m - 1)
```

或者：

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            else:
                inserted = helper(i, j + 1)
                deleted = helper(i + 1, j)
                replaced = helper(i + 1, j + 1)
                return min(inserted, deleted, replaced) + 1
        return helper(0, 0)
```

### 方法4：BFS

使用BFS搜索最短路径，时间复杂度较高，仅作理解用。

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dq, visited, res = deque([(0, 0)]), {(0, 0)}, 0
        while dq:
            size = len(dq)
            for i in range(size):
                x, y = dq.popleft()
                while x < m and y < n and word1[x] == word2[y]:
                    x += 1
                    y += 1
                if x == m and y == n:
                    return res

                if x < m and y < n and (replace_xy:= (x + 1, y + 1)) not in visited:
                    visited.add(replace_xy)
                    dq.append(replace_xy)
                if x < m and (delete_xy:= (x + 1, y)) not in visited:
                    visited.add(delete_xy)
                    dq.append(delete_xy)
                if y < n and (insert_xy:= (x, y + 1)) not in visited:
                    visited.add(insert_xy)
                    dq.append(insert_xy)
            res += 1
        return res
```

这个BFS算法在leetcode的环境中表现最好，原因是：

✅ 提前终止：找到答案立即返回（DP必须填完整个表）
✅ 跳过相同字符：减少实际处理的状态数
✅ 测试用例友好：LeetCode测试中编辑距离通常较小

但是还是建议用dp，毕竟我一下子就能看得懂dp，这个bfs还是要想一下的。

## 算法分析

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 二维DP | O(m·n) | O(m·n) | 标准DP，最直观 |
| 空间优化DP | O(m·n) | O(n) | 滚动数组优化空间 |
| 记忆化递归 | O(m·n) | O(m·n) | 递归+备忘录 |
| BFS | O(m·n) | O(m·n) | 速度最快，但是略复杂 |

二维DP详细分析：

- 时间：双重循环遍历所有状态，每个状态O(1)计算
- 空间：需要(m+1)×(n+1)的二维数组
- 实际运行：对于500长度字符串，需要约250K空间，完全可接受

### 执行过程示例

以 word1="horse", word2="ros" 为例，构建DP表：

```text
    ""  r  o  s
""   0  1  2  3
h    1  1  2  3
o    2  2  1  2
r    3  2  2  2
s    4  3  3  2
e    5  4  4  3

DP表构建过程：

- $dp[0][*]$: 插入0~3个字符
- $dp[*][0]$: 删除0~5个字符
- $dp[1][1]$: h->r, 需要1次替换
- $dp[2][2]$: ho->ro, o相同，取 $dp[1][1]=1$
- $dp[5][3]$: horse->ros, 最终答案=3

```

操作路径回溯 - 从 $dp[5][3]=3$ 回溯到 $dp[0][0]$：

1. horse -> rorse (替换h为r, $dp[5][3] \to dp[4][2]$)
2. rorse -> rose (删除r, $dp[4][2] \to dp[3][2]$)
3. rose -> ros (删除e, $dp[3][2] \to dp[3][3]$)

## 常见错误

### 错误1：状态转移方程理解错误

错误示例：混淆了三种操作的含义，忘记+1

```python
dp[i][j] = min(
    dp[i][j - 1],      # 应该加1
    dp[i - 1][j],      # 应该加1
    dp[i - 1][j - 1]   # 应该加1
)
```

**原因：** 每种操作都需要+1表示增加一次操作

### 错误2：边界条件处理错误

错误示例：未初始化边界

```python
dp = [[0] * (n + 1) for _ in range(m + 1)]
# 直接开始填充会导致第一行第一列错误
```

**原因：** $dp[i][0]$ 和 $dp[0][j]$ 必须初始化为i和j

### 错误3：字符索引错误

错误示例：使用i和j直接访问字符（应该是word1\[i-1\]和word2\[j-1\]）

```python
if word1[i] == word2[j]:
    dp[i][j] = dp[i-1][j-1]
```

**原因：** dp数组索引从1开始，但字符串索引从0开始

### 错误4：空间优化时prev变量维护错误

错误示例：未正确保存上一轮的值

```python
for j in range(1, n + 1):
    if word1[i-1] == word2[j-1]:
        dp[j] = prev  # prev可能已经被覆盖
```

**原因：** 需要在更新前保存当前值作为下一次的prev

## 相关题目

- [0583. Delete Operation for Two Strings](./583_delete_operation_for_two_strings.md)
- [0712. Minimum ASCII Delete Sum for Two Strings](./712_minimum_ascii_delete_sum_for_two_strings.md)
- [1143. Longest Common Subsequence](./1143_longest_common_subsequence.md)
- [0161. One Edit Distance](./161_one_edit_distance.md)
- [1035. Uncrossed Lines](./1035_uncrossed_lines.md)


