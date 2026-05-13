# sum of two integer

[[bitManipulation]]

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5

Constraints:

-1000 <= a, b <= 1000

千万别被运算符重载这个坑给绕进去了

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

bit manipulation:

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            # 计算不带进位的加法，并截断为 32 位
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        
        # 如果 a 是负数（最高位为 1），转换为 Python 的负数表示
        if a > MAX_INT:
            a = ~(a ^ MASK)
        return a
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

###### 如果是用运算符重载

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
