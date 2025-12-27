# Longest Palindromic Subsequence

[[dp]]

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

 

Constraints:

    1 <= s.length <= 1000
    s consists only of lowercase English letters.

自底向上的二维dp

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        # 创建二维DP数组，初始化为0
        dp = [[0] * n for _ in range(n)]
        
        # 单个字符的最长回文子序列长度为1
        for i in range(n):
            dp[i][i] = 1
        
        # 枚举子串长度，从2到n
        for length in range(2, n + 1):
            # 枚举子串起点
            for i in range(0, n - length + 1):
                j = i + length - 1  # 子串终点
                if s[i] == s[j]:
                    # 如果首尾字符相同，长度为内部子串长度+2
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # 如果首尾字符不同，取两种情况的较大值
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]
```

自底向上的一维dp

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [0] * n
        for i in range(n - 1, -1, -1):
            f[i] = 1
            pre = 0  # 初始值为 f[i+1][i]
            for j in range(i + 1, n):
                tmp = f[j]
                f[j] = pre + 2 if s[i] == s[j] else max(f[j], f[j - 1])
                pre = tmp
        return f[-1]
```

dfs:

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2;
            return max(dfs(i + 1, j), dfs(i, j - 1))
        return dfs(0, len(s) - 1)
```
