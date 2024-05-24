# Find the Safest Path in a Grid

[[bfs]] [[heap]]

You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if `grid[r][c] = 1`
An empty cell if `grid[r][c] = 0`
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

Example 1:

![](https://assets.leetcode.com/uploads/2023/07/02/example1.png)

```text
Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 0
Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).
```

Example 2:

![](https://assets.leetcode.com/uploads/2023/07/02/example2.png)

```text
Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
```

Example 3:

![](https://assets.leetcode.com/uploads/2023/07/02/example3.png)

```text
Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
```

Constraints:

```text
1 <= grid.length == n <= 400
grid[i].length == n
grid[i][j] is either 0 or 1.
There is at least one thief in the grid.
```

```python
class Solution:
    def maximumSafenessFactor(self, g: List[List[int]]) -> int:
        q = deque()
        dir = [1, 0, -1, 0, 1]
        n = len(g)
        
        # 将所有 g[i][j] == 1 的点加入队列
        q = deque([(i,j) for i in range(n) for j in range(n) if g[i][j] == 1])
        # for i in range(n):
        #     for j in range(n):
        #         if g[i][j] == 1:
        #             q.append((i, j))
        
        # 使用 BFS 扩展每个 1 的影响范围
        while q:
            i, j = q.popleft()
            for d in range(4):
                x, y = i + dir[d], j + dir[d + 1]
                if 0 <= x < n and 0 <= y < n and g[x][y] == 0:
                    g[x][y] = g[i][j] + 1
                    q.append((x, y))
        
        # 使用最大堆（优先队列）来寻找最大安全因子路径
        pq = []
        heapq.heappush(pq, (-g[0][0], 0, 0))  # Python的heapq是最小堆，所以我们使用负值来模拟最大堆
        
        while pq:
            sf, i, j = heapq.heappop(pq)
            sf = -sf  # 还原为正值
            if i == n - 1 and j == n - 1:
                return sf - 1
            for d in range(4):
                x, y = i + dir[d], j + dir[d + 1]
                if 0 <= x < n and 0 <= y < n and g[x][y] > 0:
                    heapq.heappush(pq, (-min(sf, g[x][y]), x, y))
                    g[x][y] *= -1  # 标记为访问过
        
        return -1  # 如果没有找到路径，返回-1
```
