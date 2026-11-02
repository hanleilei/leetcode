# Count Islands With Total Value Divisible by K

You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.

Example 1:
![](https://assets.leetcode.com/uploads/2025/03/06/example1griddrawio-1.png)

Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

Output: 2

![](https://assets.leetcode.com/uploads/2025/03/06/example2griddrawio.png)

Explanation:

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

Example 2:

Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

Output: 6

Explanation:

The grid contains six islands, each with a total value that is divisible by 3.

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 1000
    1 <= m * n <= 10^5
    0 <= grid[i][j] <= 10^6
    1 <= k <= 10^6

和200一样

```python
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            res = grid[i][j]
            grid[i][j] = 0
            for x, y in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    res += dfs(x, y)
            return res
        
        res = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x and dfs(i, j) % k == 0:
                    res += 1
        return res
```
