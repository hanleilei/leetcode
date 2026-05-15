# Delete Operation for Two Strings

[[dp]]

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.

```
        ""   s   e   a
      -----------------
""  |   0    1   2   3
s   |   1    0   1   2
e   |   2    1   0   1
a   |   3    2   1   0
```

这个问题和最长公共子序列问题非常类似，最长公共子序列问题的状态转移方程是：

$$
dp[i][j] =
\begin{cases}
dp[i-1][j-1] & \text{if } word1[i-1] = word2[j-1] \\
\min(dp[i-1][j],\ dp[i][j-1]) + 1 & \text{otherwise}
\end{cases}
$$

## bottom-up DP

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m+1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
```

或者，和1143一样，不要初始化：

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)] 

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
        return m + n - 2 * dp[-1][-1]
```

## bottom-up space-optimized DP

空间优化：由于 dp[i][j] 只依赖于 dp[i-1][j-1], dp[i-1][j], dp[i][j-1]，所以我们可以使用两个一维数组来代替二维数组。只要注意更新顺序，保证在计算 dp[j] 时，dp[j-1] 还没有被更新即可。

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))

        for i in range(1, m + 1):
            prev = dp[0]  # dp[j-1] 的初始值
            dp[0] = i  # dp[i][0] 的值
            for j in range(1, n + 1):
                temp = dp[j]  # 保存 dp[j] 的值，供下一次迭代使用
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], dp[j-1]) + 1
                prev = temp  # 更新 prev 为当前的 dp[j]
        return dp[-1]
```

或者：

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        f = list(range(m+1))
        for i,x in enumerate(word1):
            pre = f[0]
            f[0] = i + 1
            for j,y in enumerate(word2):
                tmp = f[j+1]
                if x == y:
                    f[j+1] = pre 
                else:
                    f[j+1] = min(f[j+1], f[j]) + 1
                pre = tmp
        return f[m]
```

# top-down DP with memoization

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                memo[i, j] = dfs(i + 1, j + 1)
            else:
                memo[i, j] = min(dfs(i + 1, j), dfs(i, j + 1)) + 1
            return memo[i, j]
        return dfs(0, 0)
```
