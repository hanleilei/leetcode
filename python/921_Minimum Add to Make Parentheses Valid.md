# Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

## Example 1

```text
Input: s = "())"
Output: 1
```

## Example 2

```text
Input: s = "((("
Output: 3
```

## Constraints

```text
1 <= s.length <= 1000
s[i] is either '(' or ')'.
```

```python
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        while "()" in S:
            S = S.replace("()", "")
        
        return len(S)
```

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        ans = 0
        for i in s:
            if i == '(':
                open += 1
            else:
                if open:
                    open -= 1
                else:
                    ans += 1
        return ans + open
```
