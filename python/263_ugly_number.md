# ugly number

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

很简单，配置一下循环

```python
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        for i in [2,3,5]:
            while num % i == 0:
                num = num / i

        return num == 1
```

换一种方法：

```python
class Solution:
    def isUgly(self, n: int) -> bool:
        if n >= 1:
            for i in [2, 3, 5]:
                while n % i == 0:
                    n //= i
        return n == 1
```

```python
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0: return False
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        return n == 1
```
