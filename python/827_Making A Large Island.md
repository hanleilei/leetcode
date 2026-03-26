# Making A Large Island

[[dfs]] [[bfs]] [[union-find]]

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:

    n == grid.length
    n == grid[i].length
    1 <= n <= 500
    grid[i][j] is either 0 or 1.

```python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def dfs(i: int, j: int) -> int:
            size = 1
            grid[i][j] = len(area) + 2  # 记录 (i,j) 属于哪个岛
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    size += dfs(x, y)
            return size

        # DFS 每个岛，统计各个岛的面积，记录到 area 列表中
        area = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    area.append(dfs(i, j))

        # 加上这个特判，可以快很多
        if not area:  # 没有岛
            return 1

        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x: continue
                s = set()
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= x < n and 0 <= y < n and grid[x][y]:
                        s.add(grid[x][y])  # 记录上下左右格子所属岛屿编号
                ans = max(ans, sum(area[idx - 2] for idx in s) + 1)  # 累加面积

        # 如果最后 ans 仍然为 0，说明所有格子都是 1，返回 n^2
        return ans if ans else n * n
```

```python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 洪水填充
        n = len(grid)
        def dfs(i, j, index):
            # index, 小岛指标 (用2,3,4去标记，1认为是未搜索过的陆地), area, 小岛面积,从 0 开始
            if i<0 or i>=n or j<0 or j>=n or grid[i][j]!=1:
                return 0
         
            grid[i][j] = index
            area = 1
            area += dfs(i+1, j, index)
            area += dfs(i-1, j, index)
            area += dfs(i, j+1, index)
            area += dfs(i, j-1, index)

            return area
        
        index = 2
        area_list = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area_list.append(dfs(i, j, index))
                    index += 1
        
        if not area_list: return 1
        ans = max(area_list)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    visited = []
                    new_area = 1
                    if i-1 >= 0 and grid[i-1][j] >= 2:
                        index = grid[i-1][j]
                        new_area += area_list[index-2]
                        visited.append(index)
                    if i+1 < n and grid[i+1][j] >= 2 and grid[i+1][j] not in visited:
                        index = grid[i+1][j]
                        new_area += area_list[index-2]
                        visited.append(index)
                    if j-1 >= 0 and grid[i][j-1] >= 2 and grid[i][j-1] not in visited:
                        index = grid[i][j-1]
                        new_area += area_list[index-2]
                        visited.append(index)
                    if j+1 < n and grid[i][j+1] >= 2 and grid[i][j+1] not in visited:
                        index = grid[i][j+1]
                        new_area += area_list[index-2]
                        visited.append(index)
                    ans = max(ans, new_area)
        
        return ans

        
```
