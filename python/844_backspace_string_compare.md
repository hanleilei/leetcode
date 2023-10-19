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
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def verify(s):
            a = list()
            for i in s:
                if i == "#":
                    if len(a) > 0:
                        a.pop()
                else:
                    a.append(i)
            return a
        return verify(s) == verify(t)
```

还是用reduce的版本比较好。。上面的重复代码可以写成函数。

还有一个用lambda表达式的版本：

```python
def backspaceCompare(self, S, T):
        back = lambda res, c: res[:-1] if c == '#' else res + c
        return reduce(back, S, "") == reduce(back, T, "")
```
