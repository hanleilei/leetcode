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

```python
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def isValid(board, x, y):
            for i in range(9):
                if i != x and board[i][y] == board[x][y]:
                    return False
            for j in range(9):
                if j != y and board[x][j] == board[x][y]:
                    return False
            i = 3 * (x / 3)
            while i < 3 * (x / 3 + 1):
                j = 3 * (y / 3)
                while j < 3 * (y / 3 + 1):
                    if (i != x or j != y) and board[i][j] == board[x][y]:
                        return False
                    j += 1
                i += 1
            return True

        def solver(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if(board[i][j] == '.'):
                        for k in range(9):
                            board[i][j] = chr(ord('1') + k)
                            if isValid(board, i, j) and solver(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True

        solver(board)
```

下面是一个64ms的算法：

```Python
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.val = self.PossibleVals()
        self.Solver()

    def PossibleVals(self):
        a,d,val = "123456789",{},{}
        for i in xrange(9):
            for j in xrange(9):
                ele = self.board[i][j]
                if ele != ".":
                    d[("r", i)] = d.get(("r", i), []) + [ele]
                    d[("c", j)] = d.get(("c", j), []) + [ele]
                    d[(i//3, j//3)] = d.get((i//3, j//3), []) + [ele]
                else: val[(i,j)] = []
        for (i,j) in val.keys():
            inval = d.get(("r",i),[])+d.get(("c",j),[])+d.get((i/3,j/3),[])
            val[(i,j)] = [n for n in a if n not in inval ]
        return val

    def Solver(self):
        if len(self.val)==0:
            return True
        kee = min(self.val.keys(), key=lambda x: len(self.val[x]))
        nums = self.val[kee]
        for n in nums:
            update = {kee:self.val[kee]}
            if self.ValidOne(n, kee, update): # valid choice
                if self.Solver(): # keep solving
                    return True
            self.undo(kee, update) # invalid choice or didn't solve it => undo
        return False

    def ValidOne(self, n, kee, update):
        self.board[kee[0]][kee[1]] = n
        del self.val[kee]
        i, j = kee
        for ind in self.val.keys():
            if n in self.val[ind]:
                if ind[0]==i or ind[1]==j or (ind[0]/3,ind[1]/3)==(i/3,j/3):
                    update[ind] = n
                    self.val[ind].remove(n)
                    if len(self.val[ind])==0:
                        return False
        return True

    def undo(self, kee, update):
        self.board[kee[0]][kee[1]]="."
        for k in update:            
            if k not in self.val: self.val[k]= update[k]
            else: self.val[k].append(update[k])
        return None
```
