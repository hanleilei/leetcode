# ugly number

An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors.

Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:

-2^31 <= n <= 2^31 - 1

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
                num = num // i

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
