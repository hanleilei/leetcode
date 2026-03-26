# Palindrome Partitioning

[[dfs]] [[backtracking]] [[string]]

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

dfs + recursion：

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        # 考虑 i 后面的逗号怎么选
        # start 表示当前这段回文子串的开始位置
        def dfs(i: int, start: int) -> None:
            if i == n:  # s 分割完毕
                ans.append(path.copy())  # 复制 path
                return

            # 不分割，不选 i 和 i+1 之间的逗号
            if i < n - 1:  # i=n-1 时只能分割
                # 考虑 i+1 后面的逗号怎么选
                dfs(i + 1, start)

            # 分割，选 i 和 i+1 之间的逗号（把 s[i] 作为子串的最后一个字符）
            t = s[start: i + 1]
            if t == t[::-1]:  # 判断是否回文
                path.append(t)
                # 考虑 i+1 后面的逗号怎么选
                # start=i+1 表示下一个子串从 i+1 开始
                dfs(i + 1, i + 1)
                path.pop()  # 恢复现场

        dfs(0, 0)
        return ans
```

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        # 考虑 s[i:] 怎么分割
        def dfs(i: int) -> None:
            if i == n:  # s 分割完毕
                ans.append(path.copy())  # 复制 path
                return
            for j in range(i, n):  # 枚举子串的结束位置
                t = s[i: j + 1]  # 分割出子串 t
                if t == t[::-1]:  # 判断 t 是不是回文串
                    path.append(t)
                    # 考虑剩余的 s[j+1:] 怎么分割
                    dfs(j + 1)
                    path.pop()  # 恢复现场

        dfs(0)
        return ans
```
