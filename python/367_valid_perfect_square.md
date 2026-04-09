# Valid perfect square

[[binarysearch]]

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

Constraints:

1 <= num <= 2^31 - 1

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

1. 1 3 5 7 法，这个是因为 (x+1)^2 = x^2 + 2*x + 1，即所有的平方数都可以转换为1 + 3 + 5 + 7 + 。。。之和。

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
