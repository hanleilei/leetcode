# Surrounded Regions

[[bfs]] [[union-find]] [[dfs]]

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:

![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.

思路:

这道题可以使用BFS和DFS两种方法来解决。从边上开始搜索，如果是'O'，那么搜索'O'周围的元素，并将'O'置换为'D'，这样每条边都DFS或者BFS一遍。而内部的'O'是不会改变的。这样下来，没有被围住的'O'全都被置换成了'D'，被围住的'O'还是'O'，没有改变。然后遍历一遍，将'O'置换为'X'，将'D'置换为'O'。

```python
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        queue = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                queue.append((r-1, c)); queue.append((r+1, c))
                queue.append((r, c-1)); queue.append((r, c+1))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"        
```

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        q = deque()

        # 把边界上的 'O' 加入队列
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = '#'
                q.append((i, 0))
            if board[i][n - 1] == 'O':
                board[i][n - 1] = '#'
                q.append((i, n - 1))

        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = '#'
                q.append((0, j))
            if board[m - 1][j] == 'O':
                board[m - 1][j] = '#'
                q.append((m - 1, j))

        # BFS 扩散
        while q:
            x, y = q.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    board[nx][ny] = '#'
                    q.append((nx, ny))

        # 最终替换
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
```

dfs:

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        m, n = len(board), len(board[0])

        def dfs(i, j):
            # 递归终止条件
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if board[i][j] == "X" or board[i][j] == "#":
                return

            # 标记当前位置为已访问
            board[i][j] = "#"

            # 递归四个方向
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # 从边界的 O 开始 DFS
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == "O":
                    dfs(i, j)

        # 最终处理
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
```

再来一个union find的解法：

```python
class UnionFind:

    def __init__(self, total_nodes):
        self.parents = [i for i in range(total_nodes)]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.parents[root2] = root1

    def find(self, node):
        while self.parents[node] != node:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node
    def isConnect(self, node1, node2):
        return self.find(node1) == self.find(node2)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def node (i, j): 
            return i * cols + j
        if not board:
            return
        
        rows = len(board)
        cols = len(board[0])

        uf = UnionFind(rows * cols + 1)
        dummyNode = rows * cols

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                        uf.union(node(i, j), dummyNode)
                    else:
                        if i > 0 and board[i - 1][j] == "O":
                            uf.union(node(i, j), node(i - 1, j))
                        if i < rows - 1 and board[i+1][j] == "O":
                            uf.union(node(i, j), node(i + 1, j))
                        if j > 0 and board[i][j - 1] == "O":
                            uf.union(node(i, j), node(i, j - 1))
                        if j < cols - 1 and board[i][j + 1] == "O":
                            uf.union(node(i, j), node(i, j + 1))
        for i in range(rows):
            for j in range(cols):
                if uf.isConnect(node(i, j), dummyNode):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        
```
