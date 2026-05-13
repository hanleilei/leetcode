# evaluate reverse polish notation

[[stack]]

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

## Example 1

```text
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

## Example 2

```text
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

## Example 3

```text
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

## Constraints

```text
1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
```

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = list()
        op = ""
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                res.append(int(t))
            else:
                if t == "+":
                    op = operator.add
                if t == "-":
                    op = operator.sub
                if t == "*":
                    op = operator.mul
                if t == "/":
                    op = operator.floordiv
                a = res.pop()
                b = res.pop()
                
                if t == "/" and a * b < 0 and b % a != 0: # 完全就是在修补python的除法向下取整导致的负数除法结果不符合题意的问题
                    c = op(b, a) + 1
                else:
                    c = op(b, a)
                res.append(c)
        return res[0]
```

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(b / a)) # 直接用int()来修补python的除法向下取整导致的负数除法结果不符合题意的问题
        return stack[-1]
```

简洁的版本。

```python
def evalRPN(self, tokens: List[str]) -> int:
    s = []
    ops = {'+': lambda a,b: b+a, '-': lambda a,b: b-a, '*': lambda a,b: b*a, '/': lambda a,b: int(b/a)}
    for t in tokens: s.append(ops[t](s.pop(), s.pop()) if t in ops else int(t))
    return s[0]
```

```python
def evalRPN(self, tokens: List[str]) -> int:
    s = []
    for t in tokens: s.append(int(t) if t not in '+-*/' else {'+':lambda a,b:b+a,'-':lambda a,b:b-a,'*':lambda a,b:b*a,'/':lambda a,b:int(b/a)}[t](s.pop(),s.pop()))
    return s[0]
```
