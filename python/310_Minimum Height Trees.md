# Minimum Height Trees

[[bfs]] [[topologicalsort]] [[graph]]

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:

![](https://assets.leetcode.com/uploads/2020/09/01/e1.jpg)

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:

![](https://assets.leetcode.com/uploads/2020/09/01/e2.jpg)

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

Constraints:

    1 <= n <= 2 * 104
    edges.length == n - 1
    0 <= ai, bi < n
    ai != bi
    All the pairs (ai, bi) are distinct.
    The given input is guaranteed to be a tree and there will be no repeated edges.

```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree, connect = [0] * n, defaultdict(list)
        for a, b in edges:
            in_degree[a] += 1
            in_degree[b] += 1
            connect[a].append(b)
            connect[b].append(a)
        nodes = [i for i, v in enumerate(in_degree) if v <= 1]
        while n > 2:
            n -= len(nodes)
            nxt = []
            for node in nodes:
                for other in connect[node]:
                    in_degree[other] -= 1
                    if in_degree[other] == 1:
                        nxt.append(other)
            nodes = nxt
        return nodes
```

```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            # base case，只有一个节点 0 的话，无法形成边，所以直接返回节点 0
            return [0]
        
        # 1、构建邻接表
        graph = [[] for _ in range(n)]
        for edge in edges:
            # 无向图，等同于双向图
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        # 2、找到所有的叶子节点
        q = collections.deque()
        for i in range(n):
            if len(graph[i]) == 1:
                q.append(i)
        
        # 3、不断删除叶子节点，直到剩下的节点数小于等于 2 个
        nodeCount = n
        while nodeCount > 2:
            sz = len(q)
            nodeCount -= sz
            for _ in range(sz):
                # 删除当前叶子节点
                cur = q.popleft()
                
                # 找到与当前叶子节点相连的节点
                for neighbor in graph[cur]:
                    # 将被删除的叶子节点的邻接节点的度减 1
                    graph[neighbor].remove(cur)
                    # 如果删除后，相连节点的度为 1，说明它也变成了叶子节点
                    if len(graph[neighbor]) == 1:
                        q.append(neighbor)
        
        # 4、最后剩下的节点就是根节点
        return list(q)
```

最快的：

```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        deg = [0] * n
        mix = [0] * n
        for u,v in edges:
            deg[u] += 1
            deg[v] += 1
            mix[u] ^= v
            mix[v] ^= u
        queue = [i for i,u in enumerate(deg) if u == 1]
        while True:
            nextQueue = []
            for u in queue:
                v = mix[u]
                mix[v] ^= u
                deg[v] -= 1
                if deg[v] == 1:
                    nextQueue.append(v)
            if not nextQueue:
                return queue
            queue = nextQueue
```
