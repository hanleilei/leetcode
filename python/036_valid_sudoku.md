# valid sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

## Example 1:
```
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
```
## Example 2:
```
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
```
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
## Note:

* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.
* The given board contain only digits 1-9 and the character '.'.
* The given board size is always 9x9.

难点还是在于怎么取到3*3的小格子里面的数据，

```Python
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter

        for i in board:
            xc = Counter(i)
            for k, v in xc.items():
                if v > 1 and k != '.':
                    return False

        for i in range(0, 9):
            xc = Counter([j[i] for j in board])
            for k, v in xc.items():
                if v > 1 and k != '.':
                    return False

        for i in range(0, 3):
            for j in range(0, 3):
                list_of_list = [k[3*i:3*i+3] for k in board][3*j:3*j+3]
                xc = Counter([item for items in list_of_list for item in items])
                for k, v in xc.items():
                    if v > 1 and k != '.':
                        return False

        return True
```

下面看看stephan大神的解法，纯粹Python2的，碉堡了。。
```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return 1 == max(collections.Counter(
                        x
                        for i, row in enumerate(board)
                        for j, c in enumerate(row)
                        if c != '.'
                        for x in ((c, i), (j, c), (i/3, j/3, c))
                    ).values() + [1])
```
