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
1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
```

真正恶心的部分在于做除法的部分，要符合leetcode的规范。。

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op = set(['+', '/','-','*'])
        stack = list()
        for i in tokens:
            a, b = 0, 0
            if i not in op:
                stack.append(int(i))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(b-a)
                elif i == "*":
                    stack.append(a*b)
                elif i == "/":
                    if b*a < 0 and b % a != 0:
                        stack.append(b/a+1)
                    else:
                        stack.append(b/a)
        return int(stack[0])
```

时隔六年，继续搞

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
                
                if t == "/" and a * b < 0 and b % a != 0: # 最难搞的地方了
                    c = op(b, a) + 1
                else:
                    c = op(b, a)
                res.append(c)
        return res[0]
```
