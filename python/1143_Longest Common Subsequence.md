# Longest Common Subsequence

[[dp]]

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

```
        ""   a   c   e
      -----------------
""  |   0    0   0   0
a   |   0    1   1   1
b   |   0    1   1   1
c   |   0    1   2   2
d   |   0    1   2   2
e   |   0    1   2   3
```

自顶向下：

```python
class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if s[i] == t[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        
        return dfs(n - 1, m - 1)
```

自底向上：

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
```

空间优化：

```python
class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        # 特判一方为另一方子串情况
        if s in t:
            return len(s)
        if t in s:
            return len(t)
        
        dp = [0] * (len(t) + 1)
        for x in s:
            pre = 0
            for j, y in enumerate(t):
                tmp = dp[j + 1]
                dp[j + 1] = pre + 1 if x == y else max(dp[j+1],  dp[j])
                pre = tmp
        return dp[-1]
```
