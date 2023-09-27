#  Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where `isConnected[i][j] = 1` if the ith city and the jth city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return the total number of provinces.

## Example 1

![](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

```text
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

## Example 2

![](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)

```text
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

## Constraints

- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j] is 1 or 0.`
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`

直接上BFS的方案：

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * (len(isConnected) + 1)
        count = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                count += 1
                queue = [i]
                visited[i] = True
                while queue:
                    vertex = queue.pop(0)
                    for j in range(len(isConnected[0])):
                        if not visited[j] and isConnected[vertex][j] == 1:
                            queue.append(j)
                            visited[j] = True
        return count
```

再来dfs方案：

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()

        def dfs(node):
            for i, v in enumerate(isConnected[node]):
                if v and i not in seen:
                    seen.add(i)
                    dfs(i)

        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
```

再来union find：

```python
class UnionFind:
    def __init__(self, n):
        self.parents = [x for x in range(n)]
        self.count = [1 for _ in range(n)]
        self.groups = n

    def find(self, a):
        while a != self.parents[a]:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a

    def union(self, a, b):
        a_root, b_root = self.find(a), self.find(b)

        if a_root == b_root:
            return True

        if self.count[a_root] > self.count[b_root]:
            self.parents[b_root] = a_root
            self.count[a_root] += self.count[b_root]
        else:
            self.parents[a_root] = b_root
            self.count[b_root] += self.count[a_root]
        self.groups -= 1

        return False

class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n < 1 or len(grid[0]) != n:
            return 0

        union = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    union.union(i,j)

        return union.groups
```
