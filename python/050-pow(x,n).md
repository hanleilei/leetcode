# Pow(x,n)

Implement pow(x, n).

 #### 确实是简单的不要不要的，一次搞定

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
        return self.myPow(x*x, n/2)
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
