# Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

Subscribe to see which companies asked this question

#### 就是一个对于平方根的求值，很简单，用标准库搞定

```python
class Solution:
    # @param {integer} x
    # @return {integer}
    import math
    def mySqrt(self, x):
        return int(math.sqrt(x))
```

似乎标准库不是一个好的方法，下面用牛顿法：

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        t = x
        while t * t > x:
            t = int(t / 2.0 + x / (2.0 * t))
        return t
```

或者二分法：

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high, mid = 0, x, x / 2
        while low <= high:
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) / 2
        return mid
```

按照九章的模板：

```Python
class Solution:
    def sqrt(self, x):        
        start, end, mid = 0, x, x//2

        while start + 1 < end:
            if mid * mid == x:
                start = mid
            elif mid * mid > x:
                end = mid
            else:
                start = mid
            mid = start + (end - start) // 2

        if start * start == x:
            return start
        if end * end == x:
            return end
        return end-1
```
