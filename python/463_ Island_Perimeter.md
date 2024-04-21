# Island Perimeter

[[graph]] [[bfs]] [[dfs]]

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

## Example 1

![](https://assets.leetcode.com/uploads/2018/10/12/island.png)

```text
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
```

## Example 2

```text
Input: grid = [[1]]
Output: 4
```

## Example 3

```text
Input: grid = [[1,0]]
Output: 4
```

## Constraints

```text
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
```

先来个速度超级快的方案:

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        S = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    S += 4
                    if i and grid[i-1][j]:
                        S -= 2
                    if j and grid[i][j-1]:
                        S -= 2

        return S
```

要问好理解，还是要看这样的方法：

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        s = 0

        def sum_adjacent(i, j):
            adjacent = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            res = 0
            for x, y in adjacent:
                if x < 0 or y < 0 or x == m or y == n or grid[x][y] == 0:
                    res += 1
            return res
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    s += sum_adjacent(i, j)
        return s
```
