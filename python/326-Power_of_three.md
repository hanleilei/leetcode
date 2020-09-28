# Power of three

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

###### 不用循环和迭代，但是需要理解math库的pow函数和log函数的使用方法

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
        while n == 1
```
