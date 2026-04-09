# keys and rooms

[[bfs]] [[dfs]]

There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

```
Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
```

Example 2:

```
Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
```

## Note

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.

这个是很巧妙dfs的算法：

```python
class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * n
        self.dfs(rooms, 0, visited)
        for v in visited:
            if not v:
                return False
        return True

    # 图的遍历框架
    def dfs(self, rooms: List[List[int]], room: int, visited: List[bool]) -> None:
        if visited[room]:
            return
        # 前序位置，标记房间已访问
        visited[room] = True

        for nextRoom in rooms[room]:
            self.dfs(rooms, nextRoom, visited)
```

迭代形式（用栈模拟递归 DFS）：

```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        stack = [0]
        visited[0] = True

        while stack:
            room = stack.pop()
            for nextRoom in rooms[room]:
                if not visited[nextRoom]:
                    visited[nextRoom] = True
                    stack.append(nextRoom)

        return all(visited)
```

```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        # 记录访问过的房间
        visited = [False] * n
        queue = collections.deque([0])
        # 在队列中加入起点，启动 BFS
        visited[0] = True

        while queue:
            room = queue.popleft()
            for nextRoom in rooms[room]:
                if not visited[nextRoom]:
                    visited[nextRoom] = True
                    queue.append(nextRoom)

        for v in visited:
            if not v:
                return False
        return True
```
