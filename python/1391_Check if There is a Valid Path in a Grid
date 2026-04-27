# Check if There is a Valid Path in a Grid

[[dfs]] [[graph]]

You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

    1 which means a street connecting the left cell and the right cell.
    2 which means a street connecting the upper cell and the lower cell.
    3 which means a street connecting the left cell and the lower cell.
    4 which means a street connecting the right cell and the lower cell.
    5 which means a street connecting the left cell and the upper cell.
    6 which means a street connecting the right cell and the upper cell.

![](https://assets.leetcode.com/uploads/2020/03/05/main.png)

You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

Example 1:

![](https://assets.leetcode.com/uploads/2020/03/05/e1.png)

Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).

Example 2:

![](https://assets.leetcode.com/uploads/2020/03/05/e2.png)

Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)

Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    1 <= grid[i][j] <= 6

```python
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # 定义每个街道类型允许的连接方向
        graph = [
            [(0, -1), (0, 1)],   # 类型1: 左右
            [(-1, 0), (1, 0)],   # 类型2: 上下
            [(0, -1), (1, 0)],   # 类型3: 左下
            [(1, 0), (0, 1)],    # 类型4: 右下
            [(0, -1), (-1, 0)],  # 类型5: 左上
            [(-1, 0), (0, 1)]    # 类型6: 右上
        ]
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        stack = [(0, 0)]
        
        while stack:
            i, j = stack.pop()
            if i == m - 1 and j == n - 1:
                return True
                
            if visited[i][j]:
                continue
                
            visited[i][j] = True
            cur = grid[i][j] - 1  # 转换为0-based索引
            
            for dx, dy in graph[cur]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    # 检查从(x,y)是否能回到(i,j)，即连接是否双向匹配
                    neighbor_type = grid[x][y] - 1
                    for ndx, ndy in graph[neighbor_type]:
                        if x + ndx == i and y + ndy == j:
                            stack.append((x, y))
                            break
        return False
```

```python
DIRS = (
    (),
    ((0, -1), (0, 1)),  # 站在街道 1，可以往左或者往右
    ((-1, 0), (1, 0)),  # 站在街道 2，可以往上或者往下
    ((0, -1), (1, 0)),  # 站在街道 3，可以往左或者往下
    ((0, 1), (1, 0)),   # 站在街道 4，可以往右或者往下
    ((0, -1), (-1, 0)), # 站在街道 5，可以往左或者往上
    ((0, 1), (-1, 0)),  # 站在街道 6，可以往右或者往上
)

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(x: int, y: int) -> bool:
            if x == m - 1 and y == n - 1:
                return True
            
            vis[x][y] = True
            for dx, dy in DIRS[grid[x][y]]:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and not vis[i][j] and (-dx, -dy) in DIRS[grid[i][j]] and dfs(i, j):
                    return True
            return False
        return dfs(0, 0)
```
