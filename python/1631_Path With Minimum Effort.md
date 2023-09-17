# Path With Minimum Effort

[[union find]] [[dijikstra]] [[binary search]] [[dfs]] 

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

## Example 1

![](https://assets.leetcode.com/uploads/2020/10/04/ex1.png)

```text
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
```

## Example 2

![](https://assets.leetcode.com/uploads/2020/10/04/ex2.png)

```text
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
```

## Example 3

![](https://assets.leetcode.com/uploads/2020/10/04/ex3.png)

```python
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
```

## Constraints

- rows == heights.length
- columns == heights[i].length
- 1 <= rows, columns <= 100
- 1 <= heights[i][j] <= 106

解题思路
拿到这个题时，大家的第一思路是不是**动态规划（DP）**呢？这个题和第 62 题『不同路径』很像，62 题是机器人从左上角走到右下角有多少不同的走法。

两个题目最大的不同点在于，第 62 题限制了机器人每次只能向下或者向右移动一步。因此，到达每个格子的状态只与其左边和上边的格子状态有关，而左边和上边的格子的状态我们都已经在之前计算过。因此第 62 题可以用 DP 求解。

本题中，如果我们定义每个格子的状态是到达该格子的最小体力消耗路径，那么每个格子的状态其实跟上下左右四个方向都有关。如果我们仍然按照从左到右，从上到下的两重 for 循环已经无法搞定 4 个方向，因此只能放弃 DP 方法。

那这个题在考察什么呢？重要的提示就在于 4 个方向！一个格子和周围 4 个方向相邻格子的状态都有关，这就是在考察图！（如果题目说的是 8 个方向，那么更明显）。

我们把每个格子当做图的一个节点，把相邻两个格子的高度差绝对值当做边的权重。就可以把输入的矩阵转化成为每条边都带有权重的图。上文中的示例给出的矩阵可以转成下面的图，可以看到从最左上角到最右下角的最小体力消耗路径为紫色所示的路径，最小体力消耗值是该路径中的边的最大权重，即为 2。

![](https://pic.leetcode-cn.com/1611888972-NzsBZC-image.png)

当把题目转成图的问题之后，怎么求解最小体力消耗路径呢？每日一题已经出了这么久的并查集，今天的题目也不会让我们失望。对，我们认为这是在求从最左上角的节点到最右下角的节点的连通性问题。具体来说，我们可以先把图中的所有边都去掉，然后按照边的权重大小，把边再逐个的添加上。当我们添加到某一条边时，最左上角的节点和最右下角的节点连通了，那么该边的权重就是我们要求的最小体力消耗值。

下面举例说明，以上面的图为例。

1. 最开始，移除所有边。

![](https://pic.leetcode-cn.com/1611889147-KDVKrI-image.png)

2. 然后添加上权重最小的边，即权重为 0 的边。此时的物理含义是判断 0 是不是最小体力消耗值，发现最左上角和最右下角未连通，需要继续。

![](https://pic.leetcode-cn.com/1611889001-DiIWlE-image.png)

3. 然后添加上权重第 2 小的边，即权重为 1 的边。此时的物理含义是判断 1 是不是最小体力消耗值，发现最左上角和最右下角未连通，需要继续。

![](https://pic.leetcode-cn.com/1611889026-yZqCqP-image.png)

4. 然后添加上权重第 3 小的边，即权重为 2 的边。此时的物理含义是判断 2 是不是最小体力消耗值，发现最左上角和最右下角已经连通，找到答案。

[](https://pic.leetcode-cn.com/1611889044-Ydwvwf-image.png)

本题中并查集的作用就是判断最左上角和最右下角是否连通，以及当每次添加上一条新的边时，若该边属于两个未联通的区域，则把两个区域连通起来。

## 代码

在分析完解题思路之后，代码就不难了。

1. 首先需要一个并查集的数据结构 DSU，这里直接使用模板。
2. 然后我们需要生成所有的边，并保存到 edges 中。edges[i] 是个 [边的权重，边的第一个顶点，边的第二个顶点] 三元组。把边的权重放在第一位的原因是，我们需要对边的权重排序，在 Python 中调用sort()函数，默认会根据第一个元素排。
3. 按照权重对所有的边进行排序sort()。
4. 遍历所有边，连通这个边的两个节点。并且判断，如果最左上角和最右下角两个节点是否连通了。如果已经连通，则此时的边的权重就是我们要求的最小体力消耗值。

代码中的一个技巧就是把二维左边转成了一维，即第 i 行第 j 列映射成了 i * N + j。因为实现并查集时使用的数组结构，因此需要把每个节点的二维坐标映射成该数组中的具体位置。这是一个在解决数组问题中的技巧。

另外，需要注意，在两重 for 循环中我们把每个顶点和右边、下边相邻的两个边放到了 edges 中。这样能保证所有的边都不重复不遗漏地放到 edges 里。此时也要注意数组越界，因为最右边的那一列节点没有更右边的边了，最下边的那一行也没有更下边的边了。

```python
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        M = len(heights)
        N = len(heights[0])
        dsu = DSU()
        edges = []
        for i in range(M):
            for j in range(N):
                pos = i * N + j
                if i < M - 1:
                    edges.append([abs(heights[i + 1][j] - heights[i][j]), pos, pos + N])
                if j < N - 1:
                    edges.append([abs(heights[i][j + 1] - heights[i][j]), pos, pos + 1])
        edges.sort()
        for edge in edges:
            dsu.union(edge[1], edge[2])
            if dsu.connected(0, M * N - 1):
                return edge[0]
        return 0
        
        
class DSU:
    def __init__(self):
        self.par = range(10001)

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

```

在来一个超级慢的DFS+binarySearch的方案：

```python
        m, n = len(heights), len(heights[0])
        neibs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def dfs(LIMIT, x, y):
            visited.add((x, y)) 
            for dx, dy in neibs:
                if 0<=dx+x<m and 0<=dy+y<n and (dx+x, dy+y) not in visited:
                    if abs(heights[x][y] - heights[dx+x][dy+y]) <= LIMIT:
                        dfs(LIMIT, dx+x, dy+y)
        
        beg, end = -1, max(max(heights, key=max))
        while beg + 1 < end:
            mid = (beg + end)//2
            visited = set()
            dfs(mid, 0, 0)
            if (m - 1, n - 1) in visited:
                end = mid
            else:
                beg = mid
                
        return end
```

```python
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        DIR = [0, 1, 0, -1, 0]
        
        def dfs(r, c, visited, threadshold):
            if r == m-1 and c == n-1: return True # Reach destination
            visited[r][c] = True
            for i in range(4):
                nr, nc = r+DIR[i], c+DIR[i+1]
                if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc]: continue
                if abs(heights[nr][nc]-heights[r][c]) <= threadshold and dfs(nr, nc, visited, threadshold): 
                    return True
            return False
        
        def canReachDestination(threadshold):
            visited = [[False] * n for _ in range(m)]
            return dfs(0, 0, visited, threadshold)
        
        left = 0
        ans = right = 10**6
        while left <= right:
            mid = left + (right-left) // 2
            if canReachDestination(mid):
                right = mid - 1 # Try to find better result on the left side
                ans = mid
            else:
                left = mid + 1
        return ans
```

Dijikstra‘s algorithms:

```python
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[math.inf] * n for _ in range(m)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)] # distance, row, col
        DIR = [0, 1, 0, -1, 0]

        while minHeap:
            d, r, c = heappop(minHeap)
            if d > dist[r][c]: continue  # this is an outdated version -> skip it
            if r == m - 1 and c == n - 1:
                return d  # Reach to bottom right
            
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i+1]
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))
```

TODO 这个题目需要再仔细研究一下， 尤其是 dijikstra 算法。