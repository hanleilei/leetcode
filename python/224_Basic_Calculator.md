# Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

##### Example 1:
```
Input: "1 + 1"
Output: 2
```
##### Example 2:
```
Input: " 2-1 + 2 "
Output: 3
```
##### Example 3:
```
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
```
##### Note:

* You may assume that the given expression is always valid.
* Do not use the eval built-in library function.

基本思路：

操作的步骤是：

如果当前是数字，那么更新计算当前数字；
如果当前是操作符+或者-，那么需要更新计算当前计算的结果res，并把当前数字num设为0，sign设为正负，重新开始；
如果当前是(，那么说明后面的小括号里的内容需要优先计算，所以要把res，sign进栈，更新res和sign为新的开始；
如果当前是)，那么说明当前括号里的内容已经计算完毕，所以要把之前的结果出栈，然后计算整个式子的结果；
最后，当所有数字结束的时候，需要把结果进行计算，确保结果是正确的。


```python
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss)
            elif ss in ["-", "+"]:
                res += sign*num
                num = 0
                sign = [-1, 1][ss=="+"]
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign

```

再来stefan大大的算法：

Keep a global running total and a stack of signs (+1 or -1), one for each open scope. The "global" outermost sign is +1.

Each number consumes a sign.
Each + and - causes a new sign.
Each ( duplicates the current sign so it can be used for the first term inside the new scope. That's also why I start with [1, 1] - the global sign 1 and a duplicate to be used for the first term, since expressions start like 3... or (..., not like +3... or +(....
Each ) closes the current scope and thus drops the current sign.
Also see the example trace below my programs.

```python
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1
        return total

```
