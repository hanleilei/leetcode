# n queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![](https://leetcode.com/static/images/problemset/8-queens.png)

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:
```
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
