# unique paths ii

[[dp]]

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

![](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:

1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:

![](https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg)

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

自顶向下：

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or obstacleGrid[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dfs(m - 1, n - 1)
```

自底向上：

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
        return dp[m][n]
```

再来一个二维的DP：

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
```

$$
[
cnt_{i,j} =
\begin{cases}
    0, & \text{if } \text{isObs}(i, j) \\
    1, & \text{if } i = 0 \text{ and } j = 0 \\
    cnt_{i-1,j}, & \text{if } j = 0 \\
    cnt_{i,j-1}, & \text{if } i = 0 \\
    cnt_{i-1,j} + cnt_{i,j-1}, & \text{otherwise}
\end{cases}
]
$$

空间压缩：

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        dp = [0] * (n + 1)
        dp[1] = 1

        for row in obstacleGrid:
            for j, x in enumerate(row):
                if x == 0:
                    dp[j+1] += dp[j]
                else:
                    dp[j + 1] = 0
        return dp[n]
```

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n = obstacleGrid.size();
        int m = obstacleGrid[0].size();
        int dp[n][m];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m;j++){
                if (obstacleGrid[i][j] == 1) dp[i][j] = 0;
                else if (i ==0 && j == 0) dp[i][j] = 1;
                else{
                    dp[i][j] = 0;
                    if (i > 0) dp[i][j] += dp[i-1][j];
                    if (j > 0) dp[i][j] += dp[i][j-1];
                }
            }
        }
        return dp[n-1][m-1];
    }
};
```

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] += dp[i - 1][j] if i > 0 else 0
                    dp[i][j] += dp[i][j - 1] if j > 0 else 0

        return dp[-1][-1]
```
