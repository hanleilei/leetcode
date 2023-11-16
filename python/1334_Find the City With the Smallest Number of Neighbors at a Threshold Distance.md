# Find the City With the Smallest Number of Neighbors at a Threshold Distance

[[graph]] [[dp]] [[shortest path]]

There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

## Example 1

![](https://assets.leetcode.com/uploads/2020/01/16/find_the_city_01.png)

```text
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
```

## Example 2

![](https://assets.leetcode.com/uploads/2020/01/16/find_the_city_02.png)

```text
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
```

## Constraints

```
2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.
```

Explanation

Becasue O(N^3) is accepted in this problem, we don't need a very fast solution.
we can simply use Floyd algorithm to find the minium distance any two cities.

Reference [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm)

I first saw @awice using it long time ago.
It's really easy and makes a lot sense.

Iterate all point middle point k,
iterate all pairs (i,j).
If it go through the middle point k,
`dis[i][j] = dis[i][k] + dis[k][j]`.

Complexity

Time O(N^3)
Space O(N^2)

```python
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= distanceThreshold for d in dis[i]): i for i in range(n)}
        return res[min(res)]        
```

虽然是解决了，再来一个速度快的：

```python
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for i in range(n)]
        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, w))
        minCnt = n
        res = -1
        for i in range(n):
            pq = [(0, i)]
            dist = [float("inf")] * n
            dist[i] = 0
            reach = set()
            while pq:
                d, node = heapq.heappop(pq)
                reach.add(node)
                if d > dist[node]:
                    continue
                for neighbor, cost in graph[node]:
                    new_dist = d + cost
                    if new_dist < dist[neighbor] and new_dist <= distanceThreshold:
                        dist[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))
            cnt = len(reach)
            if cnt <= minCnt:
                minCnt = cnt
                res = i
        return res
```

然后来几个能够实现的算法合集：

All the sp algorithms works:
Floyd: 14ms
Dijkstra: 32ms
SPFA: 64ms
Bellman: 251ms

```java
class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int INF = (int) 1e9 + 7;
        List<int[]>[] adj = new List[n];
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }
        for (int i = 0; i < n; i++) {adj[i] = new ArrayList<>();}
        for (int[] e : edges) {
            int u = e[0];
            int v = e[1];
            int d = e[2];
            
            adj[u].add(new int[]{v, d});
            adj[v].add(new int[]{u, d});

            // disable two line below when not using floyd algorithm.
            dist[u][v] = d;
            dist[v][u] = d;
        }
        
        floyd(n, adj, dist);
        // for (int i = 0; i < n; i++) {
            // dijkstra(n, adj, dist[i], i);
            // bellman(n, edges, dist[i], i);
            // spfa(n, adj, dist[i], i);
        // }
        
        int minCity = -1;
        int minCount = n;
        
        for (int i = 0; i < n; i++) {
            int curCount = 0;
            for (int j = 0; j < n; j++) {
                if (i == j) {continue;}
                if (dist[i][j] <= distanceThreshold) {curCount++;}
            }
            if (curCount <= minCount) {
                minCount = curCount;
                minCity = i;
            }
        }
        
        return minCity;
    }
    
    void spfa(int n, List<int[]>[] adj, int[] dist, int src) {
        Deque<Integer> q = new ArrayDeque<>();
        int[] updateTimes = new int[n];
        q.add(src);
        
        while (!q.isEmpty()) {
            int u = q.removeFirst();
            for (int[] next : adj[u]) {
                int v = next[0];
                int duv = next[1];
                
                if (dist[v] > dist[u] + duv) {
                    dist[v] = dist[u] + duv;
                    updateTimes[v]++;
                    q.add(v);
                    if (updateTimes[v] > n) {System.out.println("wrong");}
                }
            }
        }
    }
    
    void bellman(int n, int[][] edges, int[] dist, int src) {
        for (int k = 1; k < n; k++) {
            for (int[] e : edges) {
                int u = e[0];
                int v = e[1];
                int duv = e[2];
                
                if (dist[u] > dist[v] + duv) {
                    dist[u] = dist[v] + duv;
                }
                
                if (dist[v] > dist[u] + duv) {
                    dist[v] = dist[u] + duv;
                }
            }
        }
    }
    
    void dijkstra(int n, List<int[]>[] adj, int[] dist, int src) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (a[1] - b[1]));
        pq.add(new int[]{src, 0});
        while (!pq.isEmpty()) {
            int[] cur = pq.remove();
            int u = cur[0];
            int du = cur[1];
            if (du > dist[u]) {continue;}
            
            for (int[] nb : adj[u]) {
                int v = nb[0];
                int duv = nb[1];
                if (dist[v] > du + duv) {
                    dist[v] = du + duv;
                    pq.add(new int[]{v, dist[v]});
                }
            }
        }
    }
    
    void floyd(int n, List<int[]>[] adj, int[][] dist) {
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        } 
    }
}
```

再来一个速度最快的方法, 5ms:

```java
class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] dist = new int[n][n];
        for(int i = 0; i < n; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
            dist[i][i] = 0;
        }
        
        for(int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int distance = edge[2];
            if(distance <= distanceThreshold) {
                dist[u][v] = distance;
                dist[v][u] = distance;
            }
        }
        
        for(int k = 0; k < n; k++) {
            for(int i = 0; i < n; i++) {
                if(dist[i][k] == Integer.MAX_VALUE) {
                    continue;
                }
                
                for(int j = i; j < n; j++) {
                    if (dist[k][j] < Integer.MAX_VALUE && dist[i][j] > dist[i][k] + dist[k][j]) {
                        dist[j][i] = dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        
        int minCount = Integer.MAX_VALUE;
        int city = 0;
        for(int i = 0; i < n; i++) {
            int count = 0;
            for(int j = 0; j < dist[i].length; j++) {
                if(dist[i][j] <= distanceThreshold) {
                    count++;
                }
            }
            
            if(count <= minCount) {
                minCount = count;
                city = i;
            }
            
        }
        
        return city;
    }
    
    
}
```
