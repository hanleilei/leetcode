# game of life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

## Example:
```
Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
```

## Follow up:

- Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?


花了半个小时，思路很简单：
1. 记录全部都是1的元素位置，初始化一个计数器，列表存储需要更新的元素位置，dead 和 alive
2. 遍历列表，然后更新其八个方位，确保这其中的八个方位的元素的1的个数
3. 条件判断，如果是小于2或者大于3，直接记录死亡；如果位置为0但是计数器是3，则变为1，如果位置为1且计数器为2或者3，则记录为1；重置计数器
4. 遍历dead 和 alive 列表，更新原数组。

完全遵照题意，应该还是有需要更新的地方。超过了83%，内存占用比较大。

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        ones = [(i, j) for i in range(row) for j in range(col) if board[i][j] == 1]

        alive = list()
        dead = list()

        for x in range(row):
            for y in range(col):
                count = 0
                for m, n in [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]:
                    if 0<=n<col and 0<=m<row :
                        if board[m][n] == 1:
                            count += 1

                if count < 2 or count > 3:
                    dead.append((x, y))
                else:
                    if board[x][y] == 0 and count == 3:
                        alive.append((x, y))
        for i, j in alive:
            board[i][j] = 1
        for i, j in dead:
            board[i][j] = 0
        return board

```
再来一个stefan大大的方法：

```python
class Solution:
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J)
                                  for i, j in live
                                  for I in range(i-1, i+2)
                                  for J in range(j-1, j+2)
                                  if I != i or J != j)
        return {ij
                for ij in ctr
                if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = self.gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)

```

再来一个stefan大大cpp版本的改写：

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m  = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                count = 0
                for I in range(max(i-1, 0), min(i+2, m)):
                    for J in range(max(j-1, 0), min(j+2, n)):
                        count += board[I][J] & 1
                if count == 3 or count - board[i][j] == 3:
                    board[i][j] |=2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
```
