# add strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


##### 居然用强制类型转化就可以了。。。想来本意并非如此，也算是抖个机灵。。

```python
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1)+int(num2))
```
下面的是一个用函数式编程的方法实现。

```python
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(
              reduce(lambda a, b: 10*a + b,
                 map(lambda x: ord(x[0])+ord(x[1])-2*ord('0'),
                   list(itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0'))[::-1]
                 )
              )
            )
```
