# Valid perfect square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False

##### 用sqrt，用最简单粗暴的方法，计算最少

```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        from math import sqrt
        n = sqrt(num)
        if pow(int(n),2) == num:
            return True
        else:
            return False
```
上面的方法太老土，看下面的几个方法：

1. 二分法：

```python
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # binary search
        lo, hi = 0, num
        while hi >= lo:
            mid = (lo + hi) // 2
            if mid * mid >= num:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo * lo == num
```

2. 1 3 5 7 法，这个是因为 (x+1)^2 = x^2 + 2*x + 1，即所有的平方数都可以转换为1 + 3 + 5 + 7 + 。。。之和。

```python
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        # 1 3 5 7 method
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
```

3. 直接使用math库中的ceil和floor方法：

```python
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        a = num**0.5
        return math.ceil(a) == math.floor(a)
```
