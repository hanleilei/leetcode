# Detect Cycles in 2D Grid

[[bfs]] [[dfs]] [[unionfind]]

Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.

Example 1:

Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:

Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:

Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 500
    grid consists only of lowercase English letters.

dfs solution, time complexity `O(m*n)`, space complexity `O(m*n)`

```python
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(x: int, y: int, px: int, py:int) -> bool:
            visited[x][y] = True
            for i, j in (x, y + 1), (x, y - 1), (x+1, y), (x - 1, y):
                if ((i != px or j != py) and 
                    0 <= i < m and 0 <= j < n and 
                    grid[i][j] == grid[x][y] and
                    (visited[i][j] or dfs(i, j, x, y))):
                    return True
            return False
                
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and dfs(i, j, -1, -1):
                    return True
        return False
```

bfs solution, time complexity `O(m*n)`, space complexity `O(m*n)`

```python
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]

        def bfs(i, j):
            queue = deque()
            queue.append((i, j, -1, -1))  # (x, y, parent_x, parent_y)
            visited[i][j] = True

            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            while queue:
                x, y, px, py = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # boundary check
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue

                    # same character condition
                    if grid[nx][ny] != grid[x][y]:
                        continue

                    # skip parent
                    if nx == px and ny == py:
                        continue

                    # cycle detected
                    if visited[nx][ny]:
                        return True

                    visited[nx][ny] = True
                    queue.append((nx, ny, x, y))

            return False

        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if bfs(i, j):
                        return True

        return False
```

```python
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if not visited[r][c]:
                    # BFS 搜索相同字符的区域
                    queue = deque()
                    queue.append((r, c, -1, -1))
                    visited[r][c] = True
                    
                    while queue:
                        x, y, px, py = queue.popleft()
                        
                        # 四个方向
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nx, ny = x + dx, y + dy
                            
                            # 检查边界和字符匹配
                            if (0 <= nx < m and 0 <= ny < n and 
                                grid[nx][ny] == grid[x][y]):
                                
                                # 如果是父节点，跳过
                                if nx == px and ny == py:
                                    continue
                                
                                # 如果已经访问过，说明有环
                                if visited[nx][ny]:
                                    return True
                                
                                # 否则标记为已访问并加入队列
                                visited[nx][ny] = True
                                queue.append((nx, ny, x, y))
        
        return False
```

union find solution, time complexity `O(m*n*alpha(m*n))`, space complexity `O(m*n)`

```python
class Solution:
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        parent = list(range(m * n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return True
            parent[pa] = pb
            return False

        for i in range(m):
            for j in range(n):
                idx = i * n + j

                if i > 0 and grid[i][j] == grid[i-1][j]:
                    if union(idx, (i-1)*n + j):
                        return True

                if j > 0 and grid[i][j] == grid[i][j-1]:
                    if union(idx, i*n + j-1):
                        return True

        return False
```
