# unique path

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![](https://leetcode.com/static/images/problemset/robot_maze.png)

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100


可以用排列组合来求解，一共要走(m-1)+(n-1)步，其中(m-1)步向下，(n-1)向右，且有公式 mCn = n!/m!(n-m)! ，那么可以用下面的代码求解：

```python
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m -= 1
        n -= 1
        return math.factorial(m+n) // (math.factorial(n) * math.factorial(m))
```

当然了，更常见的一种做法就是动态规划，要到达一个格子只有从它上面或者左边的格子走过来，递推关系式：dp[i][j]=dp[i-1][j]+dp[i][j-1]。初始化条件是左边和上边都只有一条路径，索性在初始化时把所有格子初始化为1。

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for __ in range(n)] for __ in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        return dp[m - 1][n - 1]
```

这种优化是对上述方法空间的一种优化，使得空间复杂度从原来的 O(n*m)下降为 O(n)。对于起点到点(i,j)的路径总数：ways[j]= 起点到点(i-1, j) 的路径总数：ways[j] + 起点到点(i, j-1)的路径总数 ways[j-1]，于是我们就得到递推式：ways[j] = ways[j] + ways[j-1]

```python
class Solution(object):  
    def uniquePaths(self, m, n):  
        """
        :type m: int
        :type n: int
        :rtype: int
        """  
        ways = [0]*n  
        ways[0] = 1  
        for i in range(m) :  
            for j in range(1, n) :  
                ways[j] += ways[j-1]  
        return ways[n-1]  
```

当然，类似的还是少不了递归，而且不会超时。

```python
from functools import lru_cache
class Solution:
    @lru_cache(maxsize = 64)
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1: return 1
        return self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)        
```
