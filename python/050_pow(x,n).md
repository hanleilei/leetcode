# Pow(x,n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

## Example 1

```text
Input: x = 2.00000, n = 10
Output: 1024.00000
```

## Example 2

```text
Input: x = 2.10000, n = 3
Output: 9.26100
```

## Example 3

```text
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

## Constraints

```text
-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
```

直接标准库：

```python
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    import math
    def myPow(self, x, n):
        return math.pow(x,n)
```

Recursive:

```python
class Solution:
    def myPow(self, x, n):
        if b == 0: return 1
        if b < 0: return 1.0 / self.myPow(a, -b)
        half = self.myPow(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a
```

或者

```python
class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n//2)
```

Iterative:

```python
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
```

或者写成：

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        return res
```

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x, n):
            if n == 0:
                return 1.0
            
            if n % 2:
                return x * fastPow(x, n//2) ** 2
            else:
                return fastPow(x, n//2) ** 2
        if n < 0:
            x = 1 / x
            n = -n
        
        return fastPow(x, n)
```
