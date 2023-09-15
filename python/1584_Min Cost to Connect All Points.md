# Min Cost to Connect All Points

[[Minimum Spanning Tree]] [[Prim]]

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

## Example 1

![](https://assets.leetcode.com/uploads/2020/08/26/c.png)

```text
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

This is a typical minimum spanning tree question, it can be solved using either Kruskal or Prim's algorithm
Below is a Prim's algorithm implementation
Here is a wiki for [Pirm's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)
Time Complexity: Prim's Algorithm takes O(NlgN) but the whole solution is dominated by O(N*N) due to graph creation (nested loop)

```pytahon
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for record in c[j]: heapq.heappush(heap, record)
            if cnt >= n: break        
        return ans
```
