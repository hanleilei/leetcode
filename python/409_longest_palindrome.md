# longest palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.


```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        c = Counter(s)
        return sum(v - 1 * (v % 2 != 0) for v in c.values()) + 1 * any(v % 2 != 0 for v in c.values())


```

或者：

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        odds = sum(v & 1 for v in Counter(s).values())
        return len(s) - odds + bool(odds)

```
