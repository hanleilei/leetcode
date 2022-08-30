# Power of three

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

###### 不用循环和迭代，但是需要理解 math 库的 pow 函数和 log 函数的使用方法

```python
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        return False if n<=0 else n == pow(3, round(math.log(n,3)))

```

不用标准库， 而且速度超级快！

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n % 3 == 0 and n != 0:
            n //= 3
        return n == 1
```

再来一个：

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n //= 3
        return True
```
