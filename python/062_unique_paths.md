# unique path

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

## Example 1

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```text
Input: m = 3, n = 7
Output: 28
```

## Example 2

```text
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

## Constraints

```text
1 <= m, n <= 100
```

## Solution 3: Math Solution

There are total m+n-2 moves to go from Top-Left to Bottom-Right.
In m+n-2 moves, there are m-1 down moves and n-1 right moves.
You can imagine there are m+n-2 moves as: X X X ... X X X
X can be one of two values: down D or right R.
So, basically, it means we need to calculate how many ways we could choose m-1
down moves from m+n-2 moves, or n-1 right moves from m+n-2 moves.

So total `ways = C(m+n-2, m-1) = C(m+n-2, n-1) = (m+n-2)! / (m-1)! / (n-1)!`.

可以用排列组合来求解，一共要走(m-1)+(n-1)步，其中(m-1)步向下，(n-1)向右，且有公式 mCn = n!/m!(n-m)! ，那么可以用下面的代码求解：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        return math.factorial(m+n) // (math.factorial(n) * math.factorial(m))
```

或者：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1
        j = 1
        for i in range(m, m+n-2 + 1):
            ans *= i
            ans //= j
            j += 1
        return ans
```

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 1
        for i in range(min(m, n) - 1):
            res *= n + m -2 -i
            res //= i + 1
        return res
```


Complexity

Time: O(M + N), where M <= 100 is number of rows, N <= 100 is number of columns.
Space: O(1)

## Solution 1: Bottom up DP

Let `dp[r][c]` is number of paths to move from [0, 0] to [r, c].
Then `dp[m-1][n-1]` is our result.
There are maximum 2 ways to cell (r, c), that is:
From upper cell, `dp[r][c] += dp[r-1][c]`
From left cell, `dp[r][c] += dp[r][c-1]`
当然了，更常见的一种做法就是动态规划，要到达一个格子只有从它上面或者左边的格子走过来，
递推关系式：`dp[i][j]=dp[i-1][j]+dp[i][j-1]`。初始化条件是左边和上边都只有一条路径，
索性在初始化时把所有格子初始化为 1。这个也是速度最快的方法。

```python
class Solution(object):
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for __ in range(n)] for __ in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        return dp[m - 1][n - 1]
```

Complexity

Time: O(M*N), where M <= 100 is number of rows, N <= 100 is number of columns.
Space: O(M*N)

## Solution 2: Bottom up DP (Space Optimized)

Since we only access 2 states: current state dp and previous state dpPrev,
we can reduce the space complexity to O(M).

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp, dpPrev = [0] * n, [0] * n
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[c] = 1
                else:
                    dp[c] = dpPrev[c] + dp[c-1]
            dp, dpPrev = dpPrev, dp
        return dpPrev[n-1]
```

Complexity

Time: O(M*N), where M <= 100 is number of rows, N <= 100 is number of columns.
Space: O(M)

这种优化是对上述方法空间的一种优化，使得空间复杂度从原来的 O(n\*m)下降为 O(n)。对于起点到点(i,j)的路径总数：
ways[j]= 起点到点(i-1, j) 的路径总数：ways[j] + 起点到点(i, j-1)的路径总数 ways[j-1]，
于是我们就得到递推式：ways[j] = ways[j] + ways[j-1]

```python
class Solution(object):
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [0]*n
        ways[0] = 1
        for i in range(m) :
            for j in range(1, n) :
                ways[j] += ways[j-1]
        return ways[n-1]
```

当然，类似的还是少不了递归:

```python
from functools import lru_cache
class Solution:
    @lru_cache(maxsize = 64)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        return self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)
```
