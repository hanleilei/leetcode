# Happy number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
Credits:
Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.

#####关键点就在于如何判断循环停止，有一个办法就是如果列表中出现两次平方和的结果一致，就可以终止这个循环。这个问题用递归的解法似乎更简单，但是不喜欢，下面是一个非递归的解法

```python
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            t = 0
            while n:
                t += (n % 10) * ( n % 10 )
                n //= 10
            n = t
            if list(s).count(n):
                break
            else:
                s.add(n)
        return n == 1
```
