# climbing stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

## 算是大把用动态规划解决类似问题的方式了。

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current,
        return current
```
