# super Pow

[[math]]

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024

记得要用python的自带函数的性质，cpp的算法可以参考这个<http://ask.csdn.net/questions/171941。这样是不是太抖机灵了>

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

来用fast pow的方法：

$$
a^b =
\begin{cases}
    (a^{b/2})^2, & \text{当b为偶数} \\
    a \times a^{b-1}, & \text{当b为奇数}
\end{cases}
$$

```python
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = int(''.join([str(i) for i in b]))
        res = 1
        k = 1337
        a %= k
        while b > 0:
            if b & 1 == 1:
                res = (res * a) % k
            a = (a * a) % k
            b >>= 1
        return res
```
