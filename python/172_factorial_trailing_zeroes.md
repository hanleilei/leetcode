# Factorial trailing zeroes

[[math]]

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to \@ts for adding this problem and creating all test cases.

S我们很容易观察到质因子中2的个数总是大于等于5的个数。因此只要计数5的个数就可以了

那么怎样计算n!的质因子中所有5的个数呢？一个简单的方法是计算floor(n/5)。例如，7!有一个5，10!有两个5。除此之外，还有一件事情要考虑。诸如25，125之类的数字有不止一个5。例如，如果我们考虑28!，我们得到一个额外的5，并且0的总数变成了6。

处理这个问题也很简单，首先对n÷5，移除所有的单个5，然后÷25，移除额外的5，以此类推。

下面是归纳出的计算后缀0的公式。

```
n!后缀0的个数 = n!质因子中5的个数
              = floor(n/5) + floor(n/25) + floor(n/125) + ....
```

```python
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        ans = 0
        while n >= x:
            ans += n/x
            x *= 5
        return ans

```

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return n // 5 + n // 25 + n // 125 + n // 625 + n // 3125
```
