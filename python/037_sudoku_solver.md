# sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

A sudoku puzzle...

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)

...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.

似乎是一个标准套路了，回溯算法，DFS，剪枝。

```Python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        # 初始化
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[i//3 * 3 + j//3].add(num)
                else:
                    empty.append((i, j))

        def backtrack(idx):
            if idx == len(empty):
                return True

            i, j = empty[idx]
            box_id = i // 3 * 3 + j // 3

            for num in "123456789":
                if num in rows[i] or num in cols[j] or num in boxes[box_id]:
                    continue

                board[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_id].add(num)

                if backtrack(idx + 1):
                    return True

                # 回溯
                board[i][j] = "."
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[box_id].remove(num)

            return False

        backtrack(0)
```

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.row = [[False] * 9 for _ in range(9)]
        self.column = [[False] * 9 for _ in range(9)]
        self.block = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        self.valid_found = False
        
        spaces = set() # 使用集合方便删除和添加

        # 1. 初始化状态 
        for x in range(9):
            for y in range(9):
                if board[x][y] != ".":
                    num = int(board[x][y]) - 1
                    self.row[x][num] = True
                    self.column[y][num] = True
                    self.block[x//3][y//3][num] = True
                else:
                    spaces.add((x, y))
        
        self.dfs(spaces)

    def get_options(self, x, y):
        """返回坐标 (x, y) 当前所有可填数字的列表"""
        opts = []
        for digit in range(9):
            if not (self.row[x][digit] or self.column[y][digit] or self.block[x//3][y//3][digit]):
                opts.append(digit)
        return opts

    def dfs(self, spaces):
        if not spaces:
            self.valid_found = True
            return

        # --- 动态 MRV 核心逻辑 ---
        # 在当前所有空格中，找出一个可选数字数量最少的
        min_options = None
        best_pos = None
        
        for x, y in spaces:
            opts = self.get_options(x, y)
            # 如果某个空格一个数字都填不了，说明这条路走死了，直接回溯
            if not opts: return 
            
            if best_pos is None or len(opts) < len(min_options):
                min_options = opts
                best_pos = (x, y)
                if len(opts) == 1: # 剪枝优化：如果发现唯一解，直接选它，不用再找了
                    break
        
        # -----------------------
        
        x, y = best_pos
        spaces.remove(best_pos) # 尝试填这个格
        
        for digit in min_options:
            self.board[x][y] = str(digit + 1)
            self.row[x][digit] = self.column[y][digit] = self.block[x//3][y//3][digit] = True
            
            self.dfs(spaces)
            
            if self.valid_found: return
            
            # 回溯状态
            self.row[x][digit] = self.column[y][digit] = self.block[x//3][y//3][digit] = False
            
        spaces.add(best_pos) # 恢复现场
```

最容易理解的，似乎和第一个没差别。

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3)*3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            b = (i // 3)*3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter+1):
                    return True
                row[i].add(val)  # 回溯
                col[j].add(val)
                block[b].add(val)
            return False
        backtrack()
```

类似 36. 有效的数独，用三组哈希表（布尔数组）维护：

    rowSet[i] 维护第 i 行填入的数字。
    colSet[j] 维护第 j 列填入的数字。
    subBoxSet[i′][j′] 维护 (i′,j′) 宫填入的数字。其中 board[i][j] 在 (⌊3i​⌋,⌊3j​⌋) 这个宫。

为了快速找到待定数字最少的空格子，用一个最小堆维护三元组 (candidates,i,j)，其中 candidates 等于 (i,j) 这个空格子可以填入的数字个数。那么堆顶就是 candidates 最少的空格子。

然而，当我们把数字填入一个空格子时，同一行、同一列、同一宫的其余空格子的 candidates 都会减少 1。难道要动态修改堆中元素？

我们采取一个简单的折中方案：在枚举填入数字的循环中，重新统计当前格子 (i,j) 的实际待定数字个数 candidates′。在恢复现场的时候，把三元组 (candidates′,i,j) 入堆。

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_set = [set() for _ in range(9)]  # 每行填入的数字
        col_set = [set() for _ in range(9)]  # 每列填入的数字
        sub_box_set = [[set() for _ in range(3)] for _ in range(3)]  # 每宫填入的数字
        empty_pos = []  # 空格子的位置

        for i, row in enumerate(board):
            for j, b in enumerate(row):
                if b == '.':
                    empty_pos.append((i, j))  # 记录空格子的位置
                else:
                    x = int(b)
                    # 标记行、列、宫包含数字 x
                    row_set[i].add(x)
                    col_set[j].add(x)
                    sub_box_set[i // 3][j // 3].add(x)

        # get_candidates(i, j) 计算 (i, j) 这个空格子的待定数字个数，最小的在堆顶
        get_candidates = lambda i, j: 9 - len(row_set[i] | col_set[j] | sub_box_set[i // 3][j // 3])
        empty_heap = [(get_candidates(i, j), i, j) for i, j in empty_pos]
        heapify(empty_heap)

        # 每次递归，选一个空格子，枚举填入的数字
        def dfs() -> bool:
            if not empty_heap:  # 所有格子都已填入数字
                return True  # 完成数独

            # 数独玩法：优先考虑待定数字个数最少的空格子
            _, i, j = heappop(empty_heap)

            candidates = 0  # 受之前填入的数字影响，实际待定数字个数可能比入堆时的少，需要重新计算
            # 枚举 1~9 中没填过的数字 x，填入 board[i][j]
            for x in range(1, 10):
                if x in row_set[i] or x in col_set[j] or x in sub_box_set[i // 3][j // 3]:
                    continue  # x 填过了

                # 把数字 x 转成字符，填入 board[i][j]
                board[i][j] = digits[x]
                # 标记行、列、宫包含数字 x
                row_set[i].add(x)
                col_set[j].add(x)
                sub_box_set[i // 3][j // 3].add(x)

                # 填下一个空格子
                if dfs():
                    return True  # 完成数独

                # 恢复现场（撤销）
                # 注意 board[i][j] 无需恢复现场，因为我们会直接覆盖掉之前填入的数字
                row_set[i].remove(x)
                col_set[j].remove(x)
                sub_box_set[i // 3][j // 3].remove(x)

                # 统计待定数字个数
                candidates += 1

            # 恢复现场（撤销）
            heappush(empty_heap, (candidates, i, j))  # 重新入堆（更新待定数字个数）
            # 所有填法都不行，说明之前（祖先节点）的填法是错的
            return False

        dfs()
```

```python

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.row = [[False] * 9 for _ in range(9)]
        self.column = [[False] * 9 for _ in range(9)]
        self.block = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        
        spaces = set() # 使用集合方便删除和添加

        # 1. 初始化状态 
        for x in range(9):
            for y in range(9):
                if board[x][y] != ".":
                    num = int(board[x][y]) - 1
                    self.row[x][num] = True
                    self.column[y][num] = True
                    self.block[x//3][y//3][num] = True
                else:
                    spaces.add((x, y))
        
        self.dfs(spaces)

    def get_options(self, x, y):
        """返回坐标 (x, y) 当前所有可填数字的列表"""
        opts = []
        for digit in range(9):
            if not (self.row[x][digit] or self.column[y][digit] or self.block[x//3][y//3][digit]):
                opts.append(digit)
        return opts

    def dfs(self, spaces):
        if not spaces:
            return True

        best_pos = min(
            spaces,
            key=lambda p: len(self.get_options(p[0], p[1]))
        )

        x, y = best_pos
        spaces.remove(best_pos)

        for digit in self.get_options(x, y):
            self.board[x][y] = str(digit + 1)
            self.row[x][digit] = self.column[y][digit] = self.block[x//3][y//3][digit] = True

            if self.dfs(spaces):
                return True

            self.row[x][digit] = self.column[y][digit] = self.block[x//3][y//3][digit] = False

        spaces.add(best_pos)
        return False
```
