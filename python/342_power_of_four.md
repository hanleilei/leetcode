## Power of four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

##### 与328类似

```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        return False if num<=0 else num == pow(4, round(math.log(num,4)))

```

再来一个速度快的
```python
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num%4 == 0:
            num /= 4
            if num < 4:
                break

        return n == 1
```

还有：
```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n%4 == 0:
            n /= 4
        return n==1
```
同样，可以和326一样的方案：

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n % 4 == 0 and n != 0:
            n //= 4
        while n == 1
```
