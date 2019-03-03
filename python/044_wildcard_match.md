# wildcard match

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '\*'.

```
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
```
The matching should cover the entire input string (not partial).

Note:
```
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
```
Example 1:
```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```
Example 2:
```
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
```
Example 3:
```
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```
Example 4:
```
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
```
Example 5:
```
Input:
s = "acdcb"
p = "a*c?b"
Output: false
```
来一个点赞最多的：

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        a=0; b=0; m=0; i=-1
        while (a<len(s)):
            if (b<len(p) and (p[b]=="?" or p[b]==s[a])): a=a+1; b=b+1
            elif (b<len(p) and p[b]=="*"): i=b; m=a; b=b+1
            elif (i!=-1): b=i+1; m=m+1; a=m
            else: return False
        while (b<len(p)):
            if p[b]=="*": b=b+1
            else: break
        return b==len(p)
```

迭代法：

```python
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p_ptr, s_ptr, last_s_ptr, last_p_ptr = 0, 0, -1, -1
        while s_ptr < len(s):
            if p_ptr < len(p) and (s[s_ptr] == p[p_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) and p[p_ptr] == '*':
                p_ptr += 1
                last_s_ptr = s_ptr
                last_p_ptr = p_ptr
            elif last_p_ptr != -1:
                last_s_ptr += 1
                s_ptr = last_s_ptr
                p_ptr = last_p_ptr
            else:
                return False

        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1

        return p_ptr == len(p)
```
还有两个基于dp的方法：

```python
# dp with rolling window
# Time:  O(m * n)
# Space: O(m + n)
class Solution2:
    # @return a boolean
    def isMatch(self, s, p):
        k = 2
        result = [[False for j in range(len(p) + 1)] for i in range(k)]

        result[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-1]
        for i in range(1,len(s) + 1):
            result[i % k][0] = False
            for j in range(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i % k][j] = result[(i-1) % k][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    result[i % k][j] = result[i % k][j-1] or result[(i-1) % k][j]

        return result[len(s) % k][len(p)]
```

```python
# dp
# Time:  O(m * n)
# Space: O(m * n)
class Solution3:
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]

        result[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-1]
        for i in range(1,len(s) + 1):
            result[i][0] = False
            for j in range(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i][j] = result[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    result[i][j] = result[i][j-1] or result[i-1][j]

        return result[len(s)][len(p)]

```
