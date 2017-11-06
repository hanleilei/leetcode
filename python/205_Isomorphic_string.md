# Isomorphic string

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

##### 惭愧，想不出来更好的办法，就只能这样求两次。。

```python
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return self.isp(s, t) and self.isp(t, s)

    def isp(self, s, t):
        size = len(s)
        d = dict()
        for i in range(size):
            if s[i] not in d:
                d[s[i]] = t[i]
            if d[s[i]] != t[i]:
                return False
        return True
```
