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
