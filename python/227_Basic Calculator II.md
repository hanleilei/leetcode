# Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5

Constraints:

1 <= s.length <= 3 *10^5
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
The answer is guaranteed to fit in a 32-bit integer.

这个问题的解法是计算机科学的基础算法："Dijkstra 双栈算法" 的扩展之一，优先级双栈法。

```python
class Solution:
    def calculate(self, s: str):
        nums, ops = [], []
        priority = {'+':1, '-':1, '*':2, '/':2}
        i = 0
        n = len(s)
        while i < n:
            if s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                nums.append(num)
                continue
            if s[i] in priority:
                while ops and priority[ops[-1]] >= priority[s[i]]:
                    op = ops.pop()
                    b, a = nums.pop(), nums.pop()
                    nums.append(a+b if op=='+' else a-b if op=='-' else a*b if op=='*' else a//b)
                ops.append(s[i])
            i += 1
        while ops:
            op = ops.pop()
            b, a = nums.pop(), nums.pop()
            nums.append(a+b if op=='+' else a-b if op=='-' else a*b if op=='*' else a//b)
        return nums[-1]
```

换个写法：

```python
class Solution:
    def calculate(self, s: str) -> int:
        data, ops = [], []
        priority = {'+': 1, '-': 1, '*': 2, '/': 2}
        def calc():
            b = data.pop()
            a = data.pop()
            op = ops.pop()
            if op == "+":
                data.append(a + b)
            elif op == "-":
                data.append(a - b)
            elif op == "*":
                data.append(a * b)
            else:
                data.append(a // b)

        i = 0

        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                data.append(num)
                continue
            elif s[i] in "+-*/":
                while ops and priority[ops[-1]] >= priority[s[i]]:
                    calc()
                ops.append(s[i])
            i += 1
        while ops:
            calc()
        return data[-1]
```

单栈：

```python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'

        for c in s + '+':   # 末尾补一个运算符，方便把最后一个数结算掉
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ':
                continue
            else:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] = int(stack[-1] / num)  # 向 0 截断

                op = c
                num = 0

        return sum(stack)
```

对于"Dijkstra 双栈算法"，我们维护两个栈：一个用于存储数字，另一个用于存储操作符。我们根据操作符的优先级来决定何时进行计算。当遇到一个新的操作符时，我们会比较它与栈顶操作符的优先级，如果栈顶操作符的优先级更高或相等，我们就进行计算，直到栈顶操作符的优先级低于当前操作符为止。最后，我们将所有剩余的操作符进行计算，得到最终结果。

差别在于本题目没有括号，可以参考 224. Basic Calculator 来处理括号的情况。而且在题解最后的通用框架，同时解决了括号和多种运算符的优先级问题。
