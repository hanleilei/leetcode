# number of islands

[[bfs]] [[dfs]]

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

```
Input:
11110
11010
11000
00000

Output: 1
```

Example 2:

```
Input:
11000
11000
00100
00011

Output: 3
```

先来一个递归版本的 DFS：

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        num = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if self.visit(grid, i, j):
                    num += 1
        return num

    def visit(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != "1":
            return False
        grid[i][j] = "0"
        self.visit(grid, i-1, j)
        self.visit(grid, i+1, j)
        self.visit(grid, i, j-1)
        self.visit(grid, i, j+1)
        return True
```

再来一个方案：

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    number_of_islands += 1
                    self.callBFS(grid, i, j)

        return number_of_islands

    @staticmethod
    def callBFS(grid: List[List[str]],  i: int, j: int):
        grid[i][j] = '0'

        if i > 0 and grid[i-1][j] == '1':
            Solution.callBFS(grid, i-1, j)

        if j > 0 and grid[i][j-1] == '1':
            Solution.callBFS(grid, i, j - 1)

        if i < (len(grid) - 1) and grid[i+1][j] == '1':
            Solution.callBFS(grid, i + 1, j)

        if j < (len(grid[0]) - 1) and grid[i][j + 1] == '1':
            Solution.callBFS(grid, i, j + 1)
```

再来一个 BFS 版本的方案：

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        s = set([(i, j) for i in range(row) for j in range(col) if grid[i][j] == "1"])
        num = 0
        while s:
            num += 1
            from collections import deque
            queue = deque([s.pop()])
            while queue:
                i, j = queue.popleft()
                for item in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if item in s:
                        s.remove(item)
                        queue.append(item)
        return num
```

stepfan 大大对于 bfs 版本的优化：

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        s = {(i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == "1"}
        num = 0
        while s:
            num += 1
            queue = collections.deque([s.pop()])
            while queue:
                i, j = queue.popleft()
                for item in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if item in s:
                        s.remove(item)
                        queue.append(item)
        return num
```

然后是一个更简化的版本：

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))  # map in python3 return iterator
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
```
