# Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0

这个问题真的很有趣：

1. 判断能否整除
2. 确定符号
3. 确定整数部分
4. 确定小数部分
   1. 通过一个字典来记录，键值对，键是余数，值是该余数出现的位置
   2. 一旦发现余数开始重复，则说明开始循环
   3. 从第一个余数的坐标，前面是不重复的部分，后面是重复的部分。

```python
class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n % d == 0:
            return str(n // d)
        sign = "" if n * d >= 0 else '-'
        n, d = abs(n), abs(d)
        res = sign + str(n // d) + '.'
        n %= d 
        i, part = 0, ''
        m = {n: i}
        while n % d:
            n *= 10
            i += 1
            rem = n % d
            part += str(n // d)
            if rem in m:
                part = part[:m[rem]] + "("+part[m[rem]:]+")"
                return res + part
            m[rem] = i
            n = rem
        return res + part
```

例如：8639/70000 = 0.1234(142857)。
