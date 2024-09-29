# Different Ways to Add Parentheses

[[dp]]

Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

## Example 1

```text
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
```

## Example 2

```text
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]

Explanation:

(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
```

## Constraints

- 1 <= expression.length <= 20
- expression consists of digits and the operator '+', '-', and '*'.
- All the integer values in the input expression are in the range [0, 99].
- The integer values in the input expression do not have a leading '-' or '+' denoting the sign.

```python
class Solution:
    def __init__(self):
        self.memo = dict()

    def diffWaysToCompute(self, input: str) -> List[int]:
        if input in self.memo:
            return self.memo[input]
        res = []
        for i in range(len(input)):
            c = input[i]
            # 扫描算式 input 中的运算符
            if c in ['-', '*', '+']:
                # 以运算符为中心，分割成两个字符串，分别递归计算
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                # 通过子问题的结果，合成原问题的结果
                for a in left:
                    for b in right:
                        if c == '+':
                            res.append(a + b)
                        elif c == '-':
                            res.append(a - b)
                        elif c == '*':
                            res.append(a * b)
        # base case
        # 如果 res 为空，说明算式是一个数字，没有运算符
        if not res:
            res.append(int(input))
        # 将结果添加进备忘录
        self.memo[input] = res
        return res
```

```python
class Solution(object):
    def diffWaysToCompute(self, input):
        m = {}
        return self.dfs(input, m)
        
    def dfs(self, input, m):
        if input in m:
            return m[input]
        if input.isdigit():
            m[input] = int(input)
            return [int(input)]
        res = []
        for i, c in enumerate(input):
            if c in "+-*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                res.extend(eval(str(x)+c+str(y)) for x in l for y in r)
        m[input] = res
        return res
```
