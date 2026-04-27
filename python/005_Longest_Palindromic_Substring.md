# Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

#### manacher 算法

Given a string S, we are to find the longest sub-string s of S such that the reverse of s is exactly the same as s.

First insert a special character ‘#’ between each pair of adjacent characters of S, in front of S and at the back of S. After that, we only need to check palindrome sub-strings of odd length.

Let P[i] be the largest integer d such that S[i-d,…,i+d] is a palindrome.  We calculate all P[i]s from left to right. When calculating P[i], we have to compare S[i+1] with S[i-1], S[i+2] with S[i-2] and so on. A comparison is successful if two characters are the same, otherwise it is unsuccessful. In fact, we can possibly skip some unnecessary comparisons utilizing the previously calculated P[i]s.
Assume P[a]+a=max{ P[j]+j :  j<i }. If P[a]+a >= i, then we have P[i] >= min{ P[2*a-i],  2*a-i-(a- P[a])}.

Is it the algorithm linear time? The answer is yes.

First the overall number of unsuccessful comparisons is obviously at most N.

A more careful analysis show that S[i] would never be compared successfully with any S[j](j<i) after its first time successful comparison with some S[k] (k<i).

So the number of overall comparisons is a most 2N.

还有一些中文的blog：<http://blog.csdn.net/ggggiqnypgjg/article/details/6645824>
还有这个：<https://www.felix021.com/blog/read.php?2040> （写的非常清楚）

```Python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
```

直接在leetcode的blog上也有：<https://articles.leetcode.com/longest-palindromic-substring-part-ii/>

还有这个算法，需要仔细考虑以下：

```Python
class Solution:
    def longestPalindrome(self, s):
        l = len(s)
        if l <= 2:
            return s
        if s == s[::-1]:
            return s

        maxLen, start = 1, 0

        for i in range(l):
            odd = s[i - maxLen - 1:i + 1]
            even = s[i - maxLen:i + 1]
            if i - maxLen >= 1 and odd == odd[::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and even == even[::-1]:
                start = i - maxLen
                maxLen += 1

        return s[start:start + maxLen]
```

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max_length = 0
        self.start = 0

        if s == None or len(s) < 2:
            return s
        
        for i in range(len(s)):
            self.extendpal(s, i, i)
            self.extendpal(s, i, i + 1)
            if self.max_length == len(s):
                return s[self.start: self.start + self.max_length]
        return s[self.start: self.start + self.max_length]

    def extendpal(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
    
        length = right - left - 1
        if length > self.max_length:
            self.max_length = length
            self.start = left + 1 
```

上面的算法由于添加了新的test case，现在不能通过了，例如："ac"

这类回文的问题，我们可以从中间往两边扩展，注意有一个条件要求就是i的位置，和i可以是单数或者双数，即回文的长度可以是单数或者单数。

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isvalid(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        res = ""

        for i in range(len(s)):
            s1 = isvalid(s, i, i)
            s2 = isvalid(s, i, i+1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res
```

rolling hash + binary search + prefix_sum

很好的思考过程，但是。。要特么面试写这样写要死翘翘。。

参考这个[视频](https://www.bilibili.com/video/BV1MzBpBzEMk/?spm_id_from=333.1387.list.card_archive.click&vd_source=87d6dd47dbb44dd80e0f5eb84dd30767)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        n = len(s)
        hasher = PalindromeHasher(s)
        max_len = 1
        start = 0
        
        # 枚举中心位置（考虑奇偶回文）
        for i in range(n):
            # 奇数长度回文，中心为i
            left, right = 0, min(i, n-1-i)
            while left < right:
                mid = (left + right + 1) // 2
                # 检查以i为中心，半径为mid的子串是否是回文
                if hasher.get_hash(i-mid, i-1) == hasher.get_hash(i+1, i+mid, False):
                    left = mid
                else:
                    right = mid - 1
            current_len = 2 * left + 1
            if current_len > max_len:
                max_len = current_len
                start = i - left
                
            # 偶数长度回文，中心在i和i+1之间
            if i < n-1 and s[i] == s[i+1]:
                left, right = 0, min(i, n-2-i)
                while left < right:
                    mid = (left + right + 1) // 2
                    if hasher.get_hash(i-mid, i) == hasher.get_hash(i+1, i+1+mid, False):
                        left = mid
                    else:
                        right = mid - 1
                current_len = 2 * left + 2
                if current_len > max_len:
                    max_len = current_len
                    start = i - left
                    
        return s[start:start+max_len]

import sys

class PalindromeHasher:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        # 选择两个进制和模数，用于双哈希以降低碰撞概率
        self.base1, self.mod1 = 131, 10**9+7
        self.base2, self.mod2 = 13131, 10**9+9
        # 初始化哈希数组和幂数组
        self.h1, self.h2 = [0] * (self.n + 1), [0] * (self.n + 1)
        self.r1, self.r2 = [0] * (self.n + 2), [0] * (self.n + 2) # 反向哈希
        self.p1, self.p2 = [1] * (self.n + 1), [1] * (self.n + 1)
        
        # 预处理哈希值
        for i in range(1, self.n + 1):
            self.h1[i] = (self.h1[i-1] * self.base1 + (ord(s[i-1]) - 96)) % self.mod1
            self.h2[i] = (self.h2[i-1] * self.base2 + (ord(s[i-1]) - 96)) % self.mod2
            self.p1[i] = (self.p1[i-1] * self.base1) % self.mod1
            self.p2[i] = (self.p2[i-1] * self.base2) % self.mod2
            
        # 预处理反向字符串的哈希值
        for i in range(self.n, 0, -1):
            self.r1[i] = (self.r1[i+1] * self.base1 + (ord(s[i-1]) - 96)) % self.mod1
            self.r2[i] = (self.r2[i+1] * self.base2 + (ord(s[i-1]) - 96)) % self.mod2

    def get_hash(self, l, r, forward=True):
        """获取子串s[l:r+1]的哈希值（正向或反向）"""
        # 确保索引在有效范围内
        l, r = l + 1, r + 1  # 调整为1-indexed
        if forward:
            h1 = (self.h1[r] - self.h1[l-1] * self.p1[r-l+1]) % self.mod1
            h2 = (self.h2[r] - self.h2[l-1] * self.p2[r-l+1]) % self.mod2
        else:
            h1 = (self.r1[l] - self.r1[r+1] * self.p1[r-l+1]) % self.mod1
            h2 = (self.r2[l] - self.r2[r+1] * self.p2[r-l+1]) % self.mod2
        return (h1, h2)
```
