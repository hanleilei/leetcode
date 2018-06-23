# N queens II

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![](https://leetcode.com/static/images/problemset/8-queens.png)

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
```
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```

和N Queens的方法一模一样，不过就是计数。

```Python
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        for i in range(n):
            self._n_queens(n, [i], res)
        return len(res)

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
