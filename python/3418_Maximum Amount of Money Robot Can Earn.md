# Maximum Amount of Money Robot Can Earn

[[dp]]

You are given an m x n grid. A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The robot can move either right or down at any point in time.

The grid contains a value coins[i][j] in each cell:

    If coins[i][j] >= 0, the robot gains that many coins.
    If coins[i][j] < 0, the robot encounters a robber, and the robber steals the absolute value of coins[i][j] coins.

The robot has a special ability to neutralize robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.

Note: The robot's total coins can be negative.

Return the maximum profit the robot can gain on the route.

Example 1:

Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]

Output: 8

Explanation:

An optimal path for maximum coins is:

    Start at (0, 0) with 0 coins (total coins = 0).
    Move to (0, 1), gaining 1 coin (total coins = 0 + 1 = 1).
    Move to (1, 1), where there's a robber stealing 2 coins. The robot uses one neutralization here, avoiding the robbery (total coins = 1).
    Move to (1, 2), gaining 3 coins (total coins = 1 + 3 = 4).
    Move to (2, 2), gaining 4 coins (total coins = 4 + 4 = 8).

Example 2:

Input: coins = [[10,10,10],[10,10,10]]

Output: 40

Explanation:

An optimal path for maximum coins is:

    Start at (0, 0) with 10 coins (total coins = 10).
    Move to (0, 1), gaining 10 coins (total coins = 10 + 10 = 20).
    Move to (0, 2), gaining another 10 coins (total coins = 20 + 10 = 30).
    Move to (1, 2), gaining the final 10 coins (total coins = 30 + 10 = 40).

Constraints:

    m == coins.length
    n == coins[i].length
    1 <= m, n <= 500
    -1000 <= coins[i][j] <= 1000

1:1 地把记忆化搜索翻译成递推, 代码实现时，可以把 f[0][1][k] 初始化成 0，这样我们无需单独计算 f[1][1]。

```python
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        f = [[[-inf] * 3 for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][1] = [0] * 3
        for i, row in enumerate(coins):
            for j, x in enumerate(row):
                f[i + 1][j + 1][0] = max(f[i + 1][j][0], f[i][j + 1][0]) + x
                f[i + 1][j + 1][1] = max(f[i + 1][j][1] + x, f[i][j + 1][1] + x,
                                         f[i + 1][j][0], f[i][j + 1][0])
                f[i + 1][j + 1][2] = max(f[i + 1][j][2] + x, f[i][j + 1][2] + x,
                                         f[i + 1][j][1], f[i][j + 1][1])
        return f[m][n][2]
```

空间优化

举个例子，在计算 f[1][1] 时，会用到 f[0][1]，但是之后就不再用到了。那么干脆把 f[1][1] 记到 f[0][1] 中，这样对于 f[1][2] 来说，它需要的数据就在 f[0][1] 和 f[0][2] 中。f[1][2] 算完后也可以同样记到 f[0][2] 中。

所以第一个维度可以去掉。

```python
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins[0])
        f = [[-inf] * 3 for _ in range(n + 1)]
        f[1] = [0] * 3
        for row in coins:
            for j, x in enumerate(row):
                f[j + 1][2] = max(f[j][2] + x, f[j + 1][2] + x, f[j][1], f[j + 1][1])
                f[j + 1][1] = max(f[j][1] + x, f[j + 1][1] + x, f[j][0], f[j + 1][0])
                f[j + 1][0] = max(f[j][0], f[j + 1][0]) + x
        return f[n][2]
```
