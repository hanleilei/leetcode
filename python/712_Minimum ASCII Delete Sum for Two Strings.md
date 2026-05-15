# Minimum ASCII Delete Sum for Two Strings

[[dp]]

Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.

## bottom-up DP

这个和 1143. Longest Common Subsequence 的区别在于，最长公共子序列是求最长的公共子序列的长度，而这个题目是求最长公共子序列的 ASCII 码之和。所以把之前的状态转移方程稍微改一下就好了：

$dp[i+1][j+1]=dp[i][j]+ord(s1[i])$

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        total = sum(map(ord, s1+s2)) # 计算两个字符串的 ASCII 码之和
        dp = [[0] * (m+1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + ord(s1[i]) # 如果两个字符相等，那么最长公共子序列的 ASCII 码之和就是之前的加上当前字符的 ASCII 码
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return total - dp[-1][-1] * 2
```

## bottom up DP with space optimization

可以发现，计算状态dp[i][j]的时候，只会用到dp[i-1][j] 和 dp[i][j-1]的值，不会用到比 i - 1 或 j - 1 更早的状态。这里就采用滚动数组，优化掉一个维度。

使用 prev 数组存储上一轮的 dp[i - 1] 状态，以及 curr 数组存储当前轮的dp[i]的状态：

状态转移方程：

$ curr[j + 1] = prev[j] + ord(s1[i-1]) $

或

$ curr[j+1] = max(prev[j + 1], curr[j]) $

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # 前一行的状态，当前行的状态
        dp_prev = [0] * (n + 1)
        dp_curr = [0] * (n + 1)

        for i in range(m):
            for j in range(n):
                # 字符相同，公共长度+1
                if s1[i] == s2[j]:
                    dp_curr[j + 1] = dp_prev[j] + ord(s1[i])
                # 字符不同，取较大者
                else:
                    dp_curr[j + 1] = max(dp_prev[j + 1], dp_curr[j])
            # 更新上一行和当前行
            dp_prev, dp_curr = dp_curr, dp_prev

        total_ascii_sum = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        return total_ascii_sum - 2 * dp_prev[n]
```

用一个数组来存储当前行的状态，更新的时候从右往左更新，保证在计算 dp[j] 的时候，dp[j-1] 还没有被更新：

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s2)
        total = sum(map(ord, s1 + s2))

        dp = [0] * (m + 1)
        for x in s1:
            ord_x = ord(x)
            pre = 0
            for j, y in enumerate(s2):
                tmp = dp[j + 1]
                if x == y:
                    dp[j+1] = pre + ord_x
                else:
                    dp[j+1] = max(dp[j+1], dp[j])
                pre = tmp
        return total - dp[m] * 2
```

## top-down DP with memoization

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        total = sum(map(ord, s1 + s2))

        @cache
        def dfs(i: int, j: int) -> int:
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1) + ord(s1[i])
            return max(dfs(i + 1, j), dfs(i, j + 1))

        return total - dfs(0, 0) * 2
```

或者：

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def dfs(i: int, j: int):
            if i == -1 and j == -1:
                return 0
            
            if i == -1:
                return sum([ord(s2[k]) for k in range(j + 1)])
            if j == -1:
                return sum([ord(s1[k]) for k in range(i + 1)])
            
            if s1[i] == s2[j]:
                return dfs(i - 1, j - 1)
            else:
                return min(dfs(i - 1, j) + ord(s1[i]), dfs(i,j -1) + ord(s2[j]))
        return dfs(len(s1) - 1, len(s2) - 1)
```

这个题目和 edit distance 是一致的，直接上 dp

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = sum(ord(s1[k]) for k in range(i))
        for j in range(n + 1):
            dp[0][j] = sum(ord(s2[k]) for k in range(j))
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        return dp[m][n]
```
