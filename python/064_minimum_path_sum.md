# minimum path sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

```text
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

用到的思想显然就是动态规划，重建一个和grid相同的二维数组，然后类似于BFS，每一步都是上一步的递增，得到的最小值记录在当前所在的位置。

```python
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j]+= min(grid[i][j-1] if j>0 else float("inf"), grid[i-1][j] if i>0 else float("inf")) if i !=0 or j != 0 else 0
        return grid[-1][-1]
```

再来一个更简洁的。

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

```

下面的这个算法。。略精妙，将全部结果存在一个一维数组里面。

```python
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [0] + [float('inf')] * (n-1)
        for i in range(m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]
```
