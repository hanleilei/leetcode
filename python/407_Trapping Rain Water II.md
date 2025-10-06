# Trapping Rain Water II

[[heap]] [[bfs]]

Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

Example 1:

![](https://assets.leetcode.com/uploads/2021/04/08/trap1-3d.jpg)

Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:

![](https://assets.leetcode.com/uploads/2021/04/08/trap2-3d.jpg)

Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 10**4

```python
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        # Initial
        # Board cells cannot trap the water
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        # Add Board cells first
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

        # Start from level 0
        level, res = 0, 0
        
        while heap:
            height, x, y = heapq.heappop(heap)
            level = max(height, level)

            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))

                    # If cell's height smaller than the level, then it can trap the rain water
                    if heightMap[i][j] < level:
                        res += level - heightMap[i][j]

                    # Set the height to -1 if the cell is visited
                    heightMap[i][j] = -1

        return res
```


```python
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        res = 0
        heap = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        # 初始化边界，将最外层的柱子加入堆
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][0] = visited[i][n-1] = True
        
        for j in range(1, n-1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited[0][j] = visited[m-1][j] = True
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 四个方向
        
        while heap:
            height, i, j = heapq.heappop(heap)
            
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    res += max(0, height - heightMap[ni][nj])
                    heapq.heappush(heap, (max(heightMap[ni][nj], height), ni, nj))
                    visited[ni][nj] = True
        
        return res
```

TODO
还是没有彻底搞懂这个题目
