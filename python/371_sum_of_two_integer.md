# sum of two integer

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

###### 千万别被运算符重载这个坑给绕进去了

```python
class Solution(object):
   def getSum(self, a, b):
       """
       :type a: int
       :type b: int
       :rtype: int
       """
       return sum([a,b])
```

直接使用标准库operator中的add方法, 能击败100%的提交者：

```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        from operator import add
        return add(a, b)
```


###### 如果是用运算符重载：

```python
def subb():
    class A:
        def __init__(self,val):
            self.val = val
        def __lt__(self,other):
            return self.__class__(self.val+other.val)
        def __repr__(self):
            return str(self.val)

    i = A(3)
    j = A(5)
    return i<j

subb()
```
但是本题不适用。
