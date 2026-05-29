# Break a Palindrome

Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.

下文把 palindrome 简称为 s。

s 是回文串，要改成不是回文串，可以改任意一个不在正中心的字母，破坏回文串的对称性，让 s 不是回文串。

要使字典序最小，改前面比改后面更好。

比如 s=abcba：

- 把左边的 b 改成 a 得到 aacba。
- 把右边的 b 改成 a 得到 abcaa。

可以发现，前面的字母没有变小，无论后面怎么改，都不是最优的。

特殊情况：

- 如果 s 的长度是 1，那么无论怎么改都是回文串，返回空串。
- 如果 s 除了回文中心都是字母 a，那么只能把最后一个字母改成 b，这样 s 不是回文串，且字典序最小。

```python
class Solution:
    def breakPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return ""
        # 把第一个不等于 a 的字母改成 a
        # 只需找前一半，如果前一半没有不等于 a 的字母，那么后一半肯定也没有
        for i in range(n // 2):
            if s[i] != 'a':
                return s[:i] + 'a' + s[i + 1:]
        # 除了回文中心，全是 a
        return s[:-1] + 'b'  # 最后一个字母改成 b
```
