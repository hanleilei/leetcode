# Power of two

[[bitManipulation]]

Given an integer, write a function to determine if it is a power of two.

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
