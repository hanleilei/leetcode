# Restore the Array From Adjacent Pairs

[[array]] [[hash]] [[bfs]] [[dfs]]

There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

## Example 1

```text
Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
```

## Example 2

```text
Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
```

## Example 3

```text
Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]
```

## Constraints

```text
nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 105
-105 <= nums[i], ui, vi <= 105
There exists some nums that has adjacentPairs as its pairs.
```

先上一个bfs：

```python
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for node in adjacentPairs:
            graph[node[0]].append(node[1])
            graph[node[1]].append(node[0])
        
        dq = deque()
        seen = set()
        res = list()
        for node in graph:
            if len(graph[node]) == 1:
                dq.append(node)
                break
        while dq:
            node = dq.popleft()
            res.append(node)
            seen.add(node)
            for ele in graph[node]:
                if ele not in seen:
                    dq.append(ele)
        return res
```

再来一个dfs的：

```python
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def dfs(u):
            res.append(u)
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
            
        adj = defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        vertices = [x for x in adj if len(adj[x]) == 1]
        visited = {x: False for x in adj}
        res = []
        dfs(vertices[0])
        return res
```

再来一个最快的：

```python
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Step 1: Construct a mapping from each number to its adjacent numbers
        adjacency_map = defaultdict(list)
        for u, v in adjacentPairs:
            adjacency_map[u].append(v)
            adjacency_map[v].append(u)
        
        # Step 2: Find the starting number (it will appear only once in the mapping)
        for num, adjacents in adjacency_map.items():
            if len(adjacents) == 1:  # A starting or ending number
                start = num
                break

        # Step 3: Construct the result by following the chain
        result = [start]
        while len(result) < len(adjacency_map):
            # Get the current number's adjacent numbers
            # result[-1] always gives the last appended number, and we search its adjacent numbers in our adjacency map
            current_adjacents = adjacency_map[result[-1]]

            # If we're at the start, pick the first adjacent number
            if len(result) == 1:
                next_num = current_adjacents[0]
            # Otherwise, pick the number that's not the one we just came from
            elif current_adjacents[0] == result[-2]:
                next_num = current_adjacents[1]
            else:
                next_num = current_adjacents[0]
            
            result.append(next_num)

        return result
```
