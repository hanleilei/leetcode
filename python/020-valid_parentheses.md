# valid parentheses

[[stack]]

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

## Example 1

```text
Input: s = "()"
Output: true
```

## Example 2

```text
Input: s = "()[]{}"
Output: true
```

## Example 3

```text
Input: s = "(]"
Output: false
```

## Example 4

```text
Input: s = "([])"
Output: true
```

## Constraints

```text
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
```

注意算法，稍微多动一下脑筋, 非常典型的 stack 问题

```python
class Solution:
    def isValid(self, s: str) -> bool:
        d = {"}": "{", ")":"(", "]":"["}
        stack = list()
        for i in s:
            if stack and i in d:
                t = stack.pop()
                if d[i] != t:
                    return False
            else:
                stack.append(i)
        return len(stack)== 0
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
