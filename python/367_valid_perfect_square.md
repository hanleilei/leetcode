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
