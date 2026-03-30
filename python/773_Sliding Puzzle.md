# Sliding Puzzle

[[bfs]] [[backtracking]]

On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Example 1:

![](https://assets.leetcode.com/uploads/2021/06/29/slide1-grid.jpg)

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Example 2:

![](https://assets.leetcode.com/uploads/2021/06/29/slide2-grid.jpg)

Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Example 3:

![](https://assets.leetcode.com/uploads/2021/06/29/slide3-grid.jpg)

Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Constraints:

    board.length == 2
    board[i].length == 3
    0 <= board[i][j] <= 5
    Each value board[i][j] is unique.

BFS

```python
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = 2, 3
        sb = ""
        target = "123450"
        # 将 2x3 的数组转化成字符串作为 BFS 的起点
        for i in range(m):
            for j in range(n):
                sb += str(board[i][j])
        start = sb

        # 记录一维字符串的相邻索引
        neighbor = [
            [1, 3],
            [0, 4, 2],
            [1, 5],
            [0, 4],
            [3, 1, 5],
            [4, 2]
        ] 

        # ******* BFS 算法框架开始 *******
        q = deque([start])
        visited = {start}

        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                # 判断是否达到目标局面
                if target == cur:
                    return step
                # 找到数字 0 的索引
                idx = 0
                while cur[idx] != '0':
                    idx += 1
                # 将数字 0 和相邻的数字交换位置
                for adj in neighbor[idx]:
                    new_board = self.swap(list(cur), adj, idx)
                    # 防止走回头路
                    if new_board not in visited:
                        q.append(new_board)
                        visited.add(new_board)
            step += 1
        # ******* BFS 算法框架结束 *******
        return -1

    def swap(self, chars, i, j):
        chars[i], chars[j] = chars[j], chars[i]
        return "".join(chars)
```

```python
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        #把最终形态定义为“123450”
        #找到起点
        target="123450"
        start="".join(str(num) for row in board for num in row)
        if start==target:
            return 0
        
        #找到0的初始位置
        start_idx=start.index('0')
        
        #BFS队列：(当前状态字符串，0的索引，当前步数)
        queue=deque([(start,start_idx,0)])
        #集合去重
        visited={start}

        #建立邻接表
        neighbos={
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }

        #启动BFS
        while queue:
            #当前状态，当前位置，当前步数
            state,idx,step=queue.popleft()
            for next_idx in neighbos[idx]:
                new_state_list=list(state)
                new_state_list[idx],new_state_list[next_idx]=new_state_list[next_idx],new_state_list[idx]
                new_state="".join(new_state_list)

                #如果没有访问过这个状态
                if new_state not in visited:
                    if new_state==target:
                        return step+1

                    visited.add(new_state)
                    queue.append((new_state,next_idx,step+1))
        
        return -1
```

```python
class Solution:
    def slidingPuzzle(self, board):
        start = ""
        for row in board:
            for val in row:
                start += str(val)
        target = "123450"
        neighbors = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4]
        ]

        queue = [(start, 0)]
        visited = {start}

        while queue:
            new_queue = []
            for state, steps in queue:
                if state == target:
                    return steps
                zero_idx = state.index("0")
                for nei in neighbors[zero_idx]:
                    lst = list(state)
                    lst[zero_idx], lst[nei] = lst[nei], lst[zero_idx]
                    new_state = "".join(lst)
                    if new_state not in visited:
                        visited.add(new_state)
                        new_queue.append((new_state, steps + 1))
            queue = new_queue
        return -1
```

dfs:

```python
class Solution:
    def __init__(self):
        self.map = {}  # 存储状态到步数的映射
        self.myBoard = [[1, 2, 3], [4, 5, 0]]  # 初始状态
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右移动
        if not self.map:  # 预计算所有可达状态
            self.dfs(1, 2, 0)  # 从目标状态(0在右下角)开始DFS
        
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        key = self.get_key(board)
        return self.map.get(key, -1)
    
    def get_key(self, board: List[List[int]]) -> int:
        """将2x3棋盘转换为整数key"""
        key = 0
        for row in board:
            for num in row:
                key = key * 10 + num
        return key
    
    def swap(self, x: int, y: int, nx: int, ny: int, board: List[List[int]]) -> None:
        """交换两个位置的值"""
        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
    
    def dfs(self, x: int, y: int, step: int) -> None:
        """深度优先搜索所有可达状态"""
        key = self.get_key(self.myBoard)
        old_step = self.map.get(key)
        
        # 如果当前状态未记录，或找到更短的步数，则更新
        if old_step is None or old_step > step:
            self.map[key] = step
            
            # 尝试四个方向的移动
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                
                # 检查边界
                if nx < 0 or nx > 1 or ny < 0 or ny > 2:
                    continue
                
                # 移动空块
                self.swap(x, y, nx, ny, self.myBoard)
                self.dfs(nx, ny, step + 1)
                # 回溯
                self.swap(x, y, nx, ny, self.myBoard)
```
