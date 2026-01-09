# N queens II

[[backtracking]] [[bitManipulation]]

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

用bit位运算优化：

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int, hills: int, next_row: int, dales: int) -> int:
            if row >= n:
                return 1
            count = 0

            # determine free columns
            free_columns = columns & ~(hills | next_row | dales)
            while free_columns:

                # pick the rightmost free column
                curr_column = -free_columns & free_columns

                # place the queen
                free_columns ^= curr_column

                # move to the next row
                count += backtrack(row + 1,
                                   (hills | curr_column) << 1,
                                   next_row | curr_column,
                                   (dales | curr_column) >> 1)
            return count
        
        # all columns are free at the beginning
        columns = (1 << n) - 1
        return backtrack(0, 0, 0, 0)
```

这里有一个细微的差别：

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int, hills: int, next_row: int, dales: int) -> int:
            if row >= n:
                return 1
            count = 0

            # determine free columns
            free_columns = columns & ~(hills | next_row | dales)
            while free_columns:

                # pick the rightmost free column
                curr_column = -free_columns & free_columns

                # place the queen
                # free_columns ^= curr_column

                # move to the next row
                count += backtrack(row + 1,
                                   (hills | curr_column) << 1,
                                   next_row | curr_column,
                                   (dales | curr_column) >> 1)
                free_columns &= free_columns - 1
            return count
        
        # all columns are free at the beginning
        columns = (1 << n) - 1
        return backtrack(0, 0, 0, 0)
```

cpp的版本：

```cpp
class Solution {
    int count = 0;
    int sizeMask;

public:
    int totalNQueens(int n) {
        count = 0;

        // all columns are free at the beginning
        sizeMask = (1 << n) - 1; 
        backtrack(0, 0, 0);
        return count;        
    }
    void backtrack(int col, int ld, int rd) {
        if (col == sizeMask) { 
            count++;
            return;
        }

        // determine free columns
        int pos = sizeMask & (~(col | ld | rd));

        while (pos > 0) {

            // pick the rightmost free column
            int p = pos & -pos;

            // place the queen
            pos -= p;
            // move to the next row
            backtrack(col | p, (ld | p) << 1, (rd | p) >> 1);
        }
    }
};
```
