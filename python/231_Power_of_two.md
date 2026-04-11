# Power of two

[[bitManipulation]]

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

Constraints:

-2^31 <= n <= 2^31 - 1

这个看起来容易，起始还是要熟悉布尔运算中的与运算

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n-1)==0
```

还是power of three/four的套路：

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n % 2 == 0 and n != 0:
            n //= 2
        return n == 1
```

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        return bin(n).count("1") == 1
```
