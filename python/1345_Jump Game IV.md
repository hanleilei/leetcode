# Jump Game IV

[[bfs]] [[dijkstra]]

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

    i + 1 where: i + 1 < arr.length.
    i - 1 where: i - 1 >= 0.
    j where: arr[i] == arr[j] and i != j.

Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.

Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Constraints:

    1 <= arr.length <= 5 * 10^4
    -10^8 <= arr[i] <= 10^8

BFS:

```python
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = defaultdict(list)
        for i, v in enumerate(arr):
            d[v].append(i)
        
        queue = deque([0])
        seen = [False] * n
        seen[0] = True
        steps = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == n - 1:
                    return steps
                
                for i in (node + 1, node - 1):
                    if 0 <= i < n and not seen[i]:
                        seen[i] = True
                        queue.append(i)
                
                for v in d[arr[node]]:
                    if not seen[v]:
                        seen[v] = True
                        queue.append(v)
                d[arr[node]].clear()
            steps += 1
        return steps
```

dijkstra:

```python
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = defaultdict(list)
        for i, v in enumerate(arr):
            d[v].append(i)
        
        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]

        while heap:
            steps, node = heappop(heap)
            if steps > dist[node]:   # 过期条目，跳过
                continue
            if node == n - 1:
                return steps
            
            for i in (node + 1, node - 1):
                if 0 <= i < n and steps + 1 < dist[i]:
                    dist[i] = steps + 1
                    heappush(heap, (steps + 1, i))
            
            for v in d[arr[node]]:
                if steps + 1 < dist[v]:
                    dist[v] = steps + 1
                    heappush(heap, (steps + 1, v))
            d[arr[node]].clear()
        
        return -1
```
