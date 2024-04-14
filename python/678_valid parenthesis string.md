# Valid Parenthesis String

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.

```text
class Solution(object):
1.The idea is, we firstly treat * as left (, then we need to make sure the left ( is always more than or equal to ).
2.We can use a stack to do this.
3.Then similarly, we treat * as a right ), we go through s from right to left, to make sure the right ) is always
4.more than or equal to (. If both experiments succeed, then return True.
```

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        # stack 1, try to test all the ( and * can balance all the )
        stack = list()
        for i in s:
            if i in "(*":
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False
        # stack 2, try to test all the ) and * can balance all the (
        stack = list()
        for j in s[::-1]:
            if j in ")*":
                stack.append(j)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False
        return True
```

再来一个lee215的方法：

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin, cmax = 0, 0
        for i in s:
            if i == "(":
                cmax += 1
                cmin += 1
            elif i == ")":
                cmax -= 1
                cmin -= 1
            else:
                cmax += 1
                cmin -= 1
            if cmax < 0: return False
            cmin = max(cmin, 0)
        return cmin == 0
                
```
