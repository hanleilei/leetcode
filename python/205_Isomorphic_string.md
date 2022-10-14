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

或者 caikehe 大大但做法：

```python
def isIsomorphic1(self, s, t):
    d1, d2 = {}, {}
    for i, val in enumerate(s):
        d1[val] = d1.get(val, []) + [i]
    for i, val in enumerate(t):
        d2[val] = d2.get(val, []) + [i]
    return sorted(d1.values()) == sorted(d2.values())

def isIsomorphic2(self, s, t):
    d1, d2 = [[] for _ in xrange(256)], [[] for _ in xrange(256)]
    for i, val in enumerate(s):
        d1[ord(val)].append(i)
    for i, val in enumerate(t):
        d2[ord(val)].append(i)
    return sorted(d1) == sorted(d2)

def isIsomorphic3(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

def isIsomorphic4(self, s, t):
    return [s.find(i) for i in s] == [t.find(j) for j in t]

def isIsomorphic5(self, s, t):
    return map(s.find, s) == map(t.find, t)

def isIsomorphic(self, s, t):
    d1, d2 = [0 for _ in xrange(256)], [0 for _ in xrange(256)]
    for i in range(len(s)):
        if d1[ord(s[i])] != d2[ord(t[i])]:
            return False
        d1[ord(s[i])] = i+1
        d2[ord(t[i])] = i+1
    return True
```

再来一个根据 grandyang 的 cpp 版本：

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in range(len(s)):

            s_ch, t_ch = s[i], t[i]

            if s_ch not in s_map:
                s_map[s_ch] = i

            if t_ch not in t_map:
                t_map[t_ch] = i

            if s_map[s_ch] != t_map[t_ch]:
                return False

        return True
```

这个方法其实非常巧妙，比方说 s= 'abdc', t = 'abab', 或者 s = 'paper', t = 'title' 也就是说，如果是同一个模式，之前遇到的值，则直接比较，如果之前没有遇到，加入字典。
