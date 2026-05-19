# Jump Game III

[[bfs]] [[dfs]]

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3

Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
One possible way to reach at index 3 with value 0 is:
index 0 -> index 4 -> index 1 -> index 3

Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.

Constraints:

1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length

bfs:

```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        queue = deque()
        queue.append(start)

        while queue:
            size = len(queue)
            for _ in range(size):
                i = queue.popleft()
                for node in (i + arr[i], i - arr[i]):
                    if node < 0 or node > n - 1 or node in visited:
                        continue
                    if arr[node] == 0: return True
                    queue.append(node)
                    visited.add(node)
        return False
```

dfs iteratively:

```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            for i in (node + arr[node], node - arr[node]):
                if i < 0 or i >= n or i in visited:
                    continue
                if arr[i] == 0: return True
                visited.add(i)
                stack.append(i)
        return False
```

dfs recursively:

```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [False] * n

        def dfs(i: int) -> bool:
            if not 0 <= i < n or vis[i]:  # 出界，或者之前访问过（没找到）
                return False
            if arr[i] == 0:  # 找到了
                return True
            vis[i] = True  # 避免重复访问
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)
```
