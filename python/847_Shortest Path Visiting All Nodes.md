# Shortest Path Visiting All Nodes

[[bfs]]

You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

## Example 1

![](https://assets.leetcode.com/uploads/2021/05/12/shortest1-graph.jpg)

```python
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
```

## Example 2

![](https://assets.leetcode.com/uploads/2021/05/12/shortest2-graph.jpg)

```text
Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
```

## Constraints

- n == graph.length
- 1 <= n <= 12
- 0 <= graph[i].length < n
- graph[i] does not contain i.
- If graph[a] contains b, then graph[b] contains a.
- The input graph is always connected.

BFS + bitmap

```python
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # 1 <= graph.length <= 12
        # 0 <= graph[i].length < graph.length

        nodeCount = len(graph)
        
        # NOTE
        # We are using BFS here because it's better suited for 'shortest path'
        # types of problems. DFS solution is also viable though.

        # Thoughts:
        # 1. start at each node, do BFS to try reaching all other nodes.
        # 2. Must keep track of visited nodes, else infinite loop may happen.
        # 3. But each node may have to be visited multiple times, as described in the problem
        #    statement. So we cannot be too strict in limiting searches
        # 4. We must describe the state during a search, we need:
        #    - The current node we are on
        #    - Nodes we have visited (Notice the order does not matter in this case, that's a key)

        # each search is described by (currentNode, visited)
        # same search does _not_ have to be repeated, since if re-visited with
        # the same state, it would yield the same result.
        # NOTE this does not prevent revisiting the same node again,
        # it just prevents revisiting it with the same STATE!

        # Since the input size is restricted, we can use a number to encode
        # which nodes have been visited -- the i-th bit is on iff node i has been visited

        # conceptually masks[k] indicates that only node k has been visited
        masks = [1 << i for i in range(nodeCount)]
        # used to check whether all nodes have been visited (11111...111)
        allVisited = (1 << nodeCount) - 1
        queue = deque([(i, masks[i]) for i in range(nodeCount)])
        steps = 0

        # encoded_visited in visited_states[node] iff
        # (node, encoded_visited) has been pushed onto the queue
        visited_states = [{masks[i]} for i in range(nodeCount)]
        # states in visited_states will never be pushed onto queue again

        while queue:
            # number of nodes to be popped off for current steps size
            # this avoids having to store steps along with the state
            # which consumes both time and memory
            count = len(queue)

            while count:
                currentNode, visited = queue.popleft()
                if visited == allVisited:
                    return steps

                # start bfs from each neighbor
                for nb in graph[currentNode]:
                    new_visited = visited | masks[nb]
                    # pre-check here to for efficiency, as each steps increment may results
                    # in huge # of nodes being added into queue
                    if new_visited == allVisited:
                        return steps + 1
                    if new_visited not in visited_states[nb]:
                        visited_states[nb].add(new_visited)
                        queue.append((nb, new_visited))

                count -= 1
            steps += 1
        # no path which explores every node
        return inf
```

TODO 这个图的bfs，确实要再搞一下

heapq

```python
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        memo, final, q = set(), (1 << len(graph)) - 1, [(0, i, 1 << i) for i in range(len(graph))]
        while q:
            steps, node, state = heapq.heappop(q)
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    heapq.heappush(q, (steps + 1, v, state | 1 << v))
                    memo.add((state | 1 << v, v))
```

BFS

```python
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        memo, final, q, steps = set(), (1 << len(graph)) - 1, [(i, 1 << i) for i in range(len(graph))], 0
        while True:
            new = []
            for node, state in q:
                if state == final: return steps
                for v in graph[node]:
                    if (state | 1 << v, v) not in memo:
                        new.append((v, state | 1 << v))
                        memo.add((state | 1 << v, v))
            q = new
            steps += 1
```

DFS

```python
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        memo, final, q = set(), (1 << len(graph)) - 1, collections.deque([(i, 0, 1 << i) for i in range(len(graph))])
        while q:
            node, steps, state = q.popleft()
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    q.append((v, steps + 1, state | 1 << v))
                    memo.add((state | 1 << v, v))
```
