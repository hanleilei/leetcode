# Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

这类所有解的问题，dfs是肯定的了。最优解：动态规划

```Python
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []

        res = []

        def walk(current, s):
            if not s:
                res.append(current)
                return
            walk(current + [s[0]], s[1:])
            for i in range(1,len(s)):
                if s[i] == s[0] and s[0:i+1] == s[0:i+1][::-1]:
                    walk(current + [s[0:i+1]],  s[i+1:])


        walk([], s)
        return res
```

```Python
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]
```

再来一个不用递归的方法：

```Python
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []

        dp = {0: [[]], 1: [[s[0]]]}  # 0 element, 1 element
        for i in range(2, len(s)+1): # start with 2 element
            dp[i] = []
            for j in range(i): #i = 2, j = 0, 1
                if s[j:i] == s[j:i][::-1]:
                    for sol in dp[j]:
                        dp[i].append(sol + [s[j:i]])
        return dp[len(s)]
```
