# divide two integer

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

## Example 1

```text
Input: dividend = 10, divisor = 3
Output: 3
```

## Example 2

```text
Input: dividend = 7, divisor = -3
Output: -2
```

## Note

* Both dividend and divisor will be 32-bit signed integers.
* The divisor will never be 0.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

主要还是需要理解Python中的bitwise操作：https://wiki.python.org/moin/BitwiseOperators

其中  x << y 表示：
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

```python
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
```

```python
class Solution:
    def divide(self, a: int, b: int) -> int:
        # 判断结果的正负号
        if (a>0 and b >0) or (a<0 and b<0):
            flag = False
        else: flag = True

        # 用绝对值进行除法运算
        a = abs(a)
        b = abs(b)

        # 初始化返回值res → result
        res = 0

        # 使用二分法求商（移位运算符）
        while a >= b:
            n = 1
            t = b
            # 左移运算符，每次将除数b扩大2倍（由t记录），由n记录扩大的倍数，跟a比较，求得距离a最近的nb值
            while a > (t << 1):
                n <<= 1
                t <<= 1
            a -= t                   # 跳出内循环while时，t=nb
            res += n                 # 针对剩余a-nb值，采用“更相减损术”求对b的倍数，并加到n里面，即为最后的商值

        # 对绝对值计算的结果，补上正负号
        if flag: res = - res

        # 输出结果res
        return res if -2**31 <= res <= 2**31 - 1 else 2**31 - 1
```

```python
class Solution:
    def divide(self, a: int, b: int) -> int:
        ret = 0
        flag = False if (a > 0 and b > 0) or (a < 0 and b < 0) else True
        a, b = abs(a), abs(b)

        def calc(x, y):
            n = 1
            while x > y << 1:
                y <<= 1
                n <<= 1
            return n, y

        while a >= b:
            cnt, val = calc(a, b)
            ret += cnt
            a -= val
        ret = -ret if flag else ret
        return ret - 1 if ret >= 2 ** 31 else ret
```
