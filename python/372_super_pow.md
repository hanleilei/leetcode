# super Pow
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024

###### 记得要用python的自带函数的性质，cpp的算法可以参考这个http://ask.csdn.net/questions/171941。这样是不是太抖机灵了。。。
```python
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        return pow(a,int(''.join([str(i) for i in b])),1337)

```
