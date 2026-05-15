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

对于最长公共子序列问题，常用的解法是动态规划。我们可以通过构建一个二维数组来存储子问题的解，从而避免重复计算。一下是动态规划的实现步骤：

## 状态定义

设：text1长度为 m，text2长度为 n
dp[i][j]表示 text1的前 i个字符​ 与 text2的前 j个字符​ 的最长公共子序列长度
这里采用 1-based 索引，方便处理空串：dp[0][j] = dp[i][0] = 0

## 状态转移

如果 text1[i-1] == text2[j-1]，说明当前字符相同，可以将最长公共子序列长度加 1，即 dp[i][j] = dp[i-1][j-1] + 1
如果 text1[i-1] != text2[j-1]，说明当前字符不同，最长公共子序列长度取决于 dp[i-1][j] 和 dp[i][j-1] 的较大值，即 dp[i][j] = max(dp[i-1][j], dp[i][j-1])

$$
dp[i][j] =
\begin{cases}
dp[i-1][j-1] + 1 & \text{if } text1[i-1] = text2[j-1] \\
\max(dp[i-1][j],\ dp[i][j-1]) & \text{otherwise}
\end{cases}
$$

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

对于已知的递推公式：

$$
dp[i][j] =
\begin{cases}
dp[i-1][j-1] + 1 & \text{if } text1[i-1] = text2[j-1] \\
\max(dp[i-1][j],\ dp[i][j-1]) & \text{otherwise}
\end{cases}
$$

我们可以发现 dp[i][j] 只依赖于 dp[i-1][j-1]、dp[i-1][j] 和 dp[i][j-1]，因此我们可以使用一维数组保存上一行的结果，从而将空间复杂度优化到 O(n)。具体实现如下：

状态压缩目标

用一维数组：
dp[j]表示当前考虑 text1 前 i 个字符时，与 text2 前 j 个字符的 LCS等价于原来的：$dp[i][j] \rightarrow dp[j]$

代码实现：

$$
\begin{aligned}
&\text{Let } dp[j] = \text{LCS}(s[0:i-1],\ t[0:j-1]) \\
\\
&\text{for each } x \in s: \\
&\quad pre = 0 \\
&\quad \text{for } j = 0 \dots n-1: \\
&\qquad tmp = dp[j+1] \\
&\qquad dp[j+1] =
\begin{cases}
pre + 1 & \text{if } x = t[j] \\
\max(dp[j+1],\ dp[j]) & \text{otherwise}
\end{cases} \\
&\qquad pre = tmp
\end{aligned}
$$

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
                tmp = dp[j + 1] # 记录当前 dp[j+1] 的值，后续更新 dp[j+1] 后 pre 仍然保持原来的值
                dp[j + 1] = pre + 1 if x == y else max(dp[j+1],  dp[j]) # dp[j+1] 代表 dp[i-1][j]，dp[j] 代表 dp[i][j-1]
                pre = tmp
        return dp[-1]
```

再来一个非常教科书级别的实现：从右下角开始往左上角递推，而不是从左上角往右下角递推：

对于已知的递推公式：

$$
dp[i][j] =
\begin{cases}
dp[i-1][j-1] + 1 & \text{if } text1[i-1] = text2[j-1] \\
\max(dp[i-1][j],\ dp[i][j-1]) & \text{otherwise}
\end{cases}
$$

| 二维含义                   | 你的变量 |
| -------------------------- | -------- |
| dp[i+1][j+1] | dp_below[j+1] |
| dp[i+1][j] | dp_below[j] |
| dp[i][j+1] | dp_current[j+1] |

$$
\begin{aligned}
&\text{Define } dp[i][j] = \text{LCS}(text1[i:],\ text2[j:]) \\
\\
&dp_{\text{curr}}[j] =
\begin{cases}
1 + dp_{\text{below}}[j+1] & \text{if } text1[i] = text2[j] \\
\max(dp_{\text{curr}}[j+1],\ dp_{\text{below}}[j]) & \text{otherwise}
\end{cases}
\end{aligned}
$$

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:   # 这些剪枝优化非常好
            return 0

        if len(text1) < len(text2):
            text1, text2 = text2, text1

        M, N = len(text1), len(text2)

        if text1 == text2:
            return M

        if set(text2).isdisjoint(text1):
            return 0        

        dp_below = [0]*(N+1)
        dp_current = [0]*(N+1)

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if text1[i] == text2[j]:
                    dp_current[j] = 1 + dp_below[j+1]
                else:
                    dp_current[j] = max(dp_current[j+1], dp_below[j])

            dp_below, dp_current = dp_current, dp_below

        return dp_below[0]
```

补充升级：Bit-Parallel DP (Hyyrö's Algorithm)

注意这里的剪枝优化，对于一些特殊情况（如一方是另一方的子串，或者两者没有任何公共字符），我们可以直接返回结果，避免进入 DP 计算。这些优化在实际面试中非常有用，可以显著提升性能。

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
        # 1. Optimization: Trim common prefix and suffix
        # This drastically reduces N and M for many real-world cases.
        i, j = 0, 0
        n1, n2 = len(text1), len(text2)
        while i < n1 and i < n2 and text1[i] == text2[i]:
            i += 1
        while j < n1 - i and j < n2 - i and text1[n1 - 1 - j] == text2[n2 - 1 - j]:
            j += 1
            
        common_len = i + j
        text1 = text1[i : n1 - j]
        text2 = text2[i : n2 - j]
        
        if not text1 or not text2:
            return common_len

        # 2. Precompute Match Masks
        # Each character in the alphabet gets a bitmask where the k-th bit 
        # is 1 if text1[k] matches that character.
        masks = {}
        for idx, char in enumerate(text1):
            masks[char] = masks.get(char, 0) | (1 << idx)
        
        # 3. Bit-Parallel DP (Hyyrö's Algorithm)
        # v represents a row in the DP table where the k-th bit is 1 
        # if the LCS increases at that position.
        v = 0
        for char in text2:
            match_mask = masks.get(char, 0)
            # The "Magic" bitwise formula:
            # It simulates the DP transitions for an entire row at once.
            x = match_mask | v
            v = x & (x ^ (x - ((v << 1) | 1)))
            
        # The total length is the number of 1-bits in the final state
        return bin(v).count('1') + common_len
```

这个算法的核心思想是利用位运算来同时处理多个状态转移，从而大幅提升效率。通过预计算匹配掩码，我们可以在每次迭代中快速更新 DP 状态，而不需要逐个字符比较。这种方法在处理长字符串时尤其有效，可以将时间复杂度降低到 O(n * m / w)，其中 w 是机器字长（通常为 64）。

leetcode.cn 上能跑出来 0ms。

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        # Step 1: Trim common prefix and suffix
        n1, n2 = len(text1), len(text2)

        prefix = 0
        while prefix < n1 and prefix < n2 and text1[prefix] == text2[prefix]:
            prefix += 1

        # BUG FIX: 原代码后缀上界用 n1-i / n2-i，没有排除已计入前缀的部分，
        # 导致前缀很长时后缀窗口与前缀重叠。正确做法是用剩余长度作上界。
        suffix = 0
        limit1 = n1 - prefix
        limit2 = n2 - prefix
        while (suffix < limit1 and suffix < limit2
               and text1[n1 - 1 - suffix] == text2[n2 - 1 - suffix]):
            suffix += 1

        common_len = prefix + suffix
        text1 = text1[prefix : n1 - suffix if suffix else n1]
        text2 = text2[prefix : n2 - suffix if suffix else n2]

        if not text1 or not text2:
            return common_len

        # Step 2: 预计算 match masks，每个字符一个 word 列表
        # masks[c][w] 的第 b 位为 1，当且仅当 text1[w*64+b] == c
        WORD = 64
        MASK = (1 << WORD) - 1
        num_words = (len(text1) + WORD - 1) // WORD

        masks = {}
        for idx, char in enumerate(text1):
            w, b = divmod(idx, WORD)
            bucket = masks.setdefault(char, [0] * num_words)
            bucket[w] |= (1 << b)

        # Step 3: Hyyrö 位并行 DP（多字长版本）
        #
        # 核心公式拆解为两个独立的跨字长操作：
        #
        # A. 计算 shifted_v = (v << 1) | 1
        #    word[w] 的最高位溢出，进入 word[w+1] 的最低位
        #    word[0] 的最低位补 1（DP 的初始 seed）
        #
        # B. 计算 x - shifted_v（跨字长减法，传借位 borrow）
        #    x[w] = match[w] | v[w]
        #    若 x[w] - shifted_v[w] < 0，向高位借 1
        #
        # BUG FIX: 原版把两步合并成一个 carry，导致移位进位和减法借位
        # 互相干扰，结果错误。正确做法是严格分两步处理。
        v = [0] * num_words

        for char in text2:
            mw = masks.get(char)
            new_v = [0] * num_words

            # A: 计算 shifted_v = (v << 1) | 1
            shifted_v = [0] * num_words
            carry_shift = 1           # 最低位补 1
            for w in range(num_words):
                shifted_v[w] = ((v[w] << 1) & MASK) | carry_shift
                carry_shift = (v[w] >> (WORD - 1)) & 1   # 当前 word 最高位

            # B: 逐 word 计算 x & (x ^ (x - shifted_v))，跨 word 传借位
            borrow = 0
            for w in range(num_words):
                m = mw[w] if mw else 0
                x_w = m | v[w]
                diff = x_w - shifted_v[w] - borrow
                if diff < 0:
                    diff += (1 << WORD)
                    borrow = 1
                else:
                    borrow = 0
                new_v[w] = x_w & (x_w ^ (diff & MASK))

            v = new_v

        lcs_inner = sum(bin(w).count('1') for w in v)
        return lcs_inner + common_len
```
