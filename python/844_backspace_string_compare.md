# backspace string compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.



Example 1:
```
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
```
Example 2:
```
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
```
Example 3:
```
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
```
Example 4:
```
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
```

Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

先来一个超级简洁的：

```python
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        from functools import reduce
        def back(res, c):
            if c != '#': res.append(c)
            elif res: res.pop()
            return res
        return reduce(back, S, []) == reduce(back, T, [])
```

再来一个冗余比较多的：

```python
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stt = list()
        sts = list()
        if len(S) == 0 and len(T) == 0:
            return True
        for i in range(len(S)):
            try:
                if S[i] != '#':
                    sts.append(S[i])
                else:
                    sts.pop()
            except:
                pass
        for i in range(len(T)):
            try:
                if T[i] != "#":
                    stt.append(T[i])
                else:
                    stt.pop()
            except:
                pass
        return ''.join(stt) == ''.join(sts)
```

还是用reduce的版本比较好。。上面的重复代码可以写成函数。

还有一个用lambda表达式的版本：

```python
def backspaceCompare(self, S, T):
        back = lambda res, c: res[:-1] if c == '#' else res + c
        return reduce(back, S, "") == reduce(back, T, "")
```
