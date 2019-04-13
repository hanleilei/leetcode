# valid parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

###### 注意算法，稍微多动一下脑筋

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'{':'}','[':']','(':')'}

        q = list()
        for i in s:
            if i in d.keys():
                q.append(i)
            else
                if len(q) > 0 and d[q.pop()] == i:
                    continue
                else:
                    return False

        return len(q) == 0

```

```python
class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']':'[', '}':'{'}
        res = list()

        for i in s:
            if i in d and res and res[-1] == d[i]:
                res.pop()
            else:
                res.append(i)
        return len(res) == 0
```
