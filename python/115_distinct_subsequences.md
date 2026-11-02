# distinct subsequences

[[dp]]

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

## Example 1

```text
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
```

## Example 2

```text
Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
```

从记忆化搜索到递推，再到空间优化。

s 的子序列，是从 s 中删除某些字母后，得到的字符串。比如 abcde 删除 b 和 d 后，得到子序列 ace。

一、寻找子问题

在示例 2 中，我们要解决的问题（原问题）是：

    统计 s=babgbag 的所有子序列中，t=bag 出现的个数。

考虑怎么通过删除字母得到子序列：

    如果删除 s 最右边的字母 g，那么需要解决的子问题为：统计 babgba 的所有子序列中，bag 出现的个数。
    如果不删除 s 最右边的字母 g，那么需要解决的子问题为：统计 babgba 的所有子序列中，ba 出现的个数。这些等于 ba 的子序列，在末尾加上（没有删除的）字母 g，就是子序列 t=bag 了。

由于删或不删都会把原问题变成一个和原问题相似的、规模更小的子问题，所以可以用递归解决。

    注 1：从右往左思考，主要是为了方便把递归翻译成递推。从左往右思考也是可以的。

    注 2：动态规划有「选或不选」和「枚举选哪个」两种基本思考方式。子序列相邻无关一般是「选或不选」，子序列相邻相关（例如 LIS 问题）一般是「枚举选哪个」。本题用到的是「选或不选」，或者说「删或不删」。

二、状态定义与状态转移方程

根据上面的讨论，我们需要在递归过程中跟踪以下信息：

    i：s 最右边的字母的下标。
    j：t 最右边的字母的下标。

因此，定义状态为 dfs(i,j)，表示 s[..i] 的所有子序列中，t[..j] 出现的个数。这里记号 s[..i] 表示 s[0] 到 s[i]。

接下来，思考如何从一个状态转移到另一个状态。

考虑是否删除 s[i]：

    删除 s[i]，那么接下来要解决的问题是：统计 s[..i−1] 的所有子序列中，t[..j] 出现的个数，即 dfs(i−1,j)。
    不删除 s[i]（前提是 s[i]=t[j]），那么接下来要解决的问题是：统计 s[..i−1] 的所有子序列中，t[..j−1] 出现的个数，即 dfs(i−1,j−1)。

这两种情况互斥，那么根据加法原理，有

$$
\text{dfs}(i,j) = \text{dfs}(i-1,j) + (\text{s}[i] = \text{t}[j] ? \text{dfs}(i-1,j-1) : 0)
$$

递归边界：

    dfs(i,−1)=1。此时 t 是空串，根据定义，我们只有一种方法可以从 s 中得到空串，即删除 s 的所有字母。
    如果 i<j，那么 dfs(i,j)=0。这是因为我们无法得到一个比 s[..i] 还长的子序列。

递归入口：dfs(∣s∣−1,∣t∣−1)，这是原问题，也是答案。其中 ∣s∣ 表示字符串 s 的长度。

递归实现如下：

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if i < j:
                return 0
            if j < 0:
                return 1
            res = dfs(i - 1, j)  # 删除 s[i]
            if s[i] == t[j]:
                res += dfs(i - 1, j - 1)  # 不删 s[i]，和 t[j] 匹配
            return res
        return dfs(len(s) - 1, len(t) - 1)
```

递推实现如下：

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0

        f = [[1] + [0] * m for _ in range(n + 1)]
        for i, x in enumerate(s):
            for j in range(max(m - n + i, 0), min(i + 1, m)):
                f[i + 1][j + 1] = f[i][j + 1]
                if x == t[j]:
                    f[i + 1][j + 1] += f[i][j]
        return f[n][m]
```

空间优化的递推实现如下：

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        if n < m:
            return 0

        f = [0] * (m + 1)
        f[0] = 1

        for i, x in enumerate(s):
            for j in range(min(i, m - 1),  max(m - n + i, 0) - 1,  -1):
                if x == t[j]:
                    f[j + 1] += f[j]

        return f[m]
```

```Python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1, l2 = len(s)+1, len(t)+1
        cur = [0] * l2
        cur[0] = 1
        for i in range(1, l1):
            pre = cur[:]
            for j in range(1, l2):
                cur[j] = pre[j] + pre[j-1]*(s[i-1] == t[j-1])
        return cur[-1]
```
