# Basic Calculator

[[stack]] [[math]] [[string]]

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus `-` sign, non-negative integers and empty spaces.

## Examples

**Example 1:**
```text
Input: s = "1 + 1"
Output: 2
```

**Example 2:**
```text
Input: s = " 2-1 + 2 "
Output: 3
```

**Example 3:**
```text
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.
- `s` represents a valid expression.
- `'+'` is not used as a unary operation (i.e., `"+1"` and `"+(2 + 3)"` is invalid).
- `'-'` could be used as a unary operation (i.e., `"-1"` and `"-(2 + 3)"` is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

**Follow up:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

## 解法一：栈 + 状态管理（推荐）

基本思路：

操作的步骤是：

如果当前是数字，那么更新计算当前数字；
如果当前是操作符+或者-，那么需要更新计算当前计算的结果res，并把当前数字num设为0，sign设为正负，重新开始；
如果当前是(，那么说明后面的小括号里的内容需要优先计算，所以要把res，sign进栈，更新res和sign为新的开始；
如果当前是)，那么说明当前括号里的内容已经计算完毕，所以要把之前的结果出栈，然后计算整个式子的结果；
最后，当所有数字结束的时候，需要把结果进行计算，确保结果是正确的。

```python
class Solution:
    def calculate(self, s: str) -> int:
        """
        使用栈来处理括号优先级
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        res, num, sign, stack = 0, 0, 1, []
        
        for char in s:
            if char.isdigit():
                # 构建多位数字
                num = 10 * num + int(char)
            elif char in ['+', '-']:
                # 处理之前的数字
                res += sign * num
                num = 0
                # 更新符号
                sign = 1 if char == '+' else -1
            elif char == '(':
                # 保存当前状态，开始新的括号运算
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ')':
                # 完成括号内运算，恢复之前状态
                res += sign * num
                res *= stack.pop()  # 恢复括号前的符号
                res += stack.pop()  # 恢复括号前的结果
                num = 0
            # 忽略空格
        
        # 处理最后一个数字
        return res + sign * num
```

### 算法思路

**核心思想**：使用栈来处理括号的嵌套，维护当前的结果和符号状态。

**处理流程**：
1. **数字处理**：累积构建多位数字
2. **运算符处理**：更新结果，重置数字，设置新符号
3. **左括号处理**：保存当前状态到栈，重新开始计算
4. **右括号处理**：完成括号内计算，恢复之前状态

### 算法演示

以 `"(1+(4+5+2)-3)+(6+8)"` 为例：

```text
初始: res=0, num=0, sign=1, stack=[]

'(': stack=[0,1], res=0, sign=1
'1': num=1
'+': res=0+1*1=1, num=0, sign=1
'(': stack=[0,1,1,1], res=0, sign=1
'4': num=4
'+': res=0+1*4=4, num=0, sign=1
'5': num=5
'+': res=4+1*5=9, num=0, sign=1
'2': num=2
')': res=9+1*2=11, sign=stack.pop()=1, res=11*1+stack.pop()=11+1=12
'-': res=1+1*12=13, num=0, sign=-1
'3': num=3
')': res=13+(-1)*3=10, sign=stack.pop()=1, res=10*1+stack.pop()=10+0=10
'+': res=10+1*0=10, num=0, sign=1
'(': stack=[10,1], res=0, sign=1
'6': num=6
'+': res=0+1*6=6, num=0, sign=1
'8': num=8
')': res=6+1*8=14, sign=stack.pop()=1, res=14*1+stack.pop()=14+10=24

最终: res + sign * num = 24 + 1 * 0 = 24
```

## 解法二：Stefan大神的符号栈法

```python
class Solution:
    def calculate(self, s: str) -> int:
        """
        Stefan大神的优雅解法：维护符号栈
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        total = 0
        i, signs = 0, [1, 1]  # [全局符号, 当前作用域符号]
        
        while i < len(s):
            char = s[i]
            if char.isdigit():
                # 解析完整数字
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if char in '+-(':
                # '+' -> 1, '-' -> -1, '(' -> 复制当前符号
                signs.append(signs[-1] * (1 if char != '-' else -1))
            elif char == ')':
                signs.pop()
            i += 1
        return total
```

### Stefan解法核心思想

**符号栈管理**：
- 维护一个符号栈，每个元素表示当前作用域的符号
- 每个数字消费一个符号
- `+/-` 产生新符号：当前符号 × (±1)
- `(` 复制当前符号用于新作用域
- `)` 关闭当前作用域

## 解法三：递归解法

```python
class Solution:
    def calculate(self, s: str) -> int:
        """
        递归处理括号
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        def helper(index):
            result = 0
            num = 0
            sign = 1
            
            while index < len(s):
                char = s[index]
                if char.isdigit():
                    num = num * 10 + int(char)
                elif char == '+':
                    result += sign * num
                    num = 0
                    sign = 1
                elif char == '-':
                    result += sign * num
                    num = 0
                    sign = -1
                elif char == '(':
                    # 递归处理括号内容
                    num, index = helper(index + 1)
                elif char == ')':
                    return result + sign * num, index
                index += 1
            
            return result + sign * num
        
        return helper(0)
```

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 栈+状态管理 | O(n) | O(n) | 直观易懂，状态清晰 |
| 符号栈法 | O(n) | O(n) | 代码简洁，思路巧妙 |
| 递归解法 | O(n) | O(n) | 结构清晰，易于扩展 |

## 关键要点

1. **括号处理**：使用栈保存状态，处理嵌套优先级
2. **符号管理**：正确维护当前运算的符号状态
3. **数字解析**：处理多位数字的累积构建
4. **边界处理**：注意最后一个数字的处理

## 相关题目

- [227. Basic Calculator II](227_basic_calculator_ii.md) - 包含乘除运算
- [772. Basic Calculator III](772_basic_calculator_iii.md) - 完整四则运算
- [150. Evaluate Reverse Polish Notation](150_evaluate_reverse_polish_notation.md) - 后缀表达式

经典的表达式求值问题，展示了栈在处理嵌套结构中的重要应用。
