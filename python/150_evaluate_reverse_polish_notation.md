# evaluate reverse polish notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
```
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
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
