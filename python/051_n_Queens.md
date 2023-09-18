# n queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![](https://leetcode.com/static/images/problemset/8-queens.png)

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

## Example

```text
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
```

```python
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                res.append(queens)
                return
            for i in range(n):
                if i not in queens and p - i not in xy_dif and p + i not in xy_sum:
                    dfs(queens + [i], xy_dif + [p - i], xy_sum + [p + i])
        res = []                    
        dfs([], [], [])
        return [["." * i + "Q"  + '.' * (n - i - 1) for i in sol] for sol in res]
```

```python
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        for i in range(n):
            self._n_queens(n, [i], res)
        return res

    def _n_queens(self, n, cols, res):
        m = len(cols)
        if m == n:
            res.append([''.join(['Q' if j == col else '.' for j in range(n)]) for col in cols ])
        else:
            for j in range(n):
                for row, col in enumerate(cols):
                    if abs(col-j) == m-row or j == col:
                        break
                else:
                    cols.append(j)
                    self._n_queens(n, cols, res)
                    cols.pop()
        return res
        
```

caikehe 的方法：

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.backtrack([-1]*n, 0, [], res)
        return res

    def backtrack(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return  # backtracking
        for i in range(len(nums)):
            nums[index] = i
            if self.isValid(nums, index):  # pruning
                tmp = "."*len(nums)
                self.backtrack(nums, index+1, path+[tmp[:i]+"Q"+tmp[i+1:]], res)

    def isValid(self, nums: List[List[str]], n: int) -> bool:
        for i in range(n):
            if abs(nums[i]-nums[n]) == n -i or nums[i] == nums[n]:
                return False
        return True 
```

caikehe 的方法，比labuladong，尤其是在isvalid函数的判断上，简洁太多了。

下面，参考一下labuladong的方案：

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = []
        for i in range(n):
            board.append(['.'] * n)

        def isValid(row, col):
            # 检查列是否有皇后
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            
            # 检查右上方是否有皇后
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            # 检查左上方是否有皇后
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            return True

        def backtrack(row):
            # 超出左后一行
            if row == n:
                result.append([''.join(b) for b in board])
                return
            
            for col in range(n):
                # 排除不合法选择
                if not isValid(row, col):
                    continue
                # 做选择
                board[row][col] = 'Q'
                # 进入下一秒决策
                backtrack(row + 1)
                # 撤销选择
                board[row][col] = '.'
        
        backtrack(0)
        return result
```
