# Find the Derangement of An Array

In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: 3
Output: 2
Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
Note:
n is in the range of [1, 106].

###### 使用公式 f(n) = (n-1) * ( f(n-1) + f(n-2) ), 下面的是我使用的解法：

```python
class Solution:
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        from functools import lru_cache
        @lru_cache(maxsize = None)
        def envelope(n):
            if n <= 1:
                return 0
            if n == 2:
                return 1
            else:
                return (n-1) * (envelope(n-1) + envelope(n-2))
        return envelope(n)
```
很遗憾，超时了。。一直以为使用这类的字典，或者系统自带的字典可以解决这类问题，看起来还是不行，还是要用类似于动态规划的方法。下面是借鉴别人的写法。

```python
class Solution:
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        X, Y = 1, 0
        for e in range(2, n+1):
            X, Y = Y, (e - 1) * (X + Y) % MOD
        return Y

```
