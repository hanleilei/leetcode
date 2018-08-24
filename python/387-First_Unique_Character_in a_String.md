# First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

###### 我的算法是找到所有只出现一次的字母，然后取这些字母出现的最小位置

```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        lt = list()
        for i in range(len(s)):
            d[s[i]] = i
        from collections import Counter
        for k, v in Counter(s).items():
            if v == 1:
                lt.append(d[k])
        if lt == []:
            return -1
        return min(lt)
```

写了这么多，其实两行就可以：
```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from string import ascii_lowercase
        return min([s.index(x) for x in ascii_lowercase if s.count(x) == 1] or [-1])
```

再来一个硬上的：

```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        from collections import defaultdict
        d = defaultdict(list)
        for i, v in enumerate(s):
            d[v].append(i)
        lt = [i for i in d.keys() if len(d[i]) == 1]
        if len(lt) == 0:
            return -1
        return min([d[k] for k in lt])[0]
```
