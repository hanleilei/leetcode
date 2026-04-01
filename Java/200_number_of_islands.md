# number of islands

[[bfs]] [[dfs]]

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

先来一个递归版本的 DFS：

```java
public class Solution {
    int dx[] = {0, 0, 1, -1};
    int dy[] = {1, -1, 0, 0};
    char[][] g;

    public int numIslands(char[][] grid) {
        int island = 0;
        g = grid;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (g[i][j] == '0') continue;
                island += sink(i, j);
            }
        }
        return island;
    }

    private int sink(int i, int j) {
        // terminate condition: if i or j is out of bound, or if g[i][j] is '0', return 0
        if (i < 0 || i >= g.length || j < 0 || j >= g[0].length || g[i][j] == '0') {
            return 0;
        }
        // i, j == '1', we sink the island by setting g[i][j] to '0'
        g[i][j] = '0';

        for (int k = 0; k < 4; k++) {
            int x = i + dx[k];
            int y = j + dy[k];
            if (x >= 0 && x < g.length && y >= 0 && y < g[0].length) {
                if (g[x][y] == '1') {
                    sink(x, y);
                }
            }
        }
        return 1;
    }
}
```
