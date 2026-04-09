# valid sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

## Example 1

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

## Example 2

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

## Note

* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.
* The given board contain only digits 1-9 and the character '.'.
* The given board size is always 9x9.

难点还是在于怎么取到3*3的小格子里面的数据，

```Python
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

我们需要满足三个规则：

1. 每行不能有相同数字。
2. 每列不能有相同数字。
3. 每宫不能有相同数字。注：宫是大小为 3×3 的子矩阵。

判断是否满足规则：

1. 对于每行，在遍历的同时，用二维布尔数组 rowHas 标记遍历过的数字，其中 rowHas[i][x]=true 表示第 i 行有数字 x。比如之前遍历到数字 6，标记 rowHas[i][6]=true；然后又遍历到数字 6，发现 rowHas[i][6]=true，则说明有两个 6，数独不是有效的，返回 false。
2. 对于每列，在遍历的同时，用二维布尔数组 colHas 标记遍历过的数字，其中 colHas[j][x]=true 表示第 j 列有数字 x。如果继续遍历，遍历到相同数字，即发现 colHas[j][x]=true，那么数独不是有效的，返回 false。
3. 对于每宫，在遍历的同时，用三维布尔数组 subBoxHas 标记遍历过的数字。设 $i′=⌊i/3⌋，j′=⌊j/3⌋$，定义 subBoxHas[i′][j′][x]=true 表示 (i′,j′) 宫有数字 x。如果继续遍历，遍历到相同数字，即发现 subBoxHas[i′][j′][x]=true，那么数独不是有效的，返回 false。

如果遍历过程中没有返回 false，那么数独是有效的，最终返回 true。

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_has = [[False] * 9 for _ in range(9)]  # row_has[i][x] 表示 i 行是否有数字 x
        col_has = [[False] * 9 for _ in range(9)]  # col_has[j][x] 表示 j 列是否有数字 x
        sub_box_has = [[[False] * 9 for _ in range(3)] for _ in range(3)]  # sub_box_has[i'][j'][x] 表示 (i',j') 宫是否有数字 x

        for i, row in enumerate(board):
            for j, b in enumerate(row):
                if b == '.':
                    continue
                x = int(b) - 1  # 字符 '1'~'9' 转成数字 0~8
                if row_has[i][x] or col_has[j][x] or sub_box_has[i // 3][j // 3][x]:  # 重复遇到数字 x
                    return False
                # 标记行、列、宫包含数字 x
                row_has[i][x] = col_has[j][x] = sub_box_has[i // 3][j // 3][x] = True

        return True
```

用哈希：

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_has = set()  # (i, x)
        col_has = set()  # (j, x)
        sub_box_has = set()  # (i // 3, j // 3, x)

        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == '.':
                    continue
                if (i, x) in row_has or (j, x) in col_has or (i // 3, j // 3, x) in sub_box_has:  # 重复遇到数字 x
                    return False
                # 标记行、列、宫包含数字 x
                row_has.add((i, x))
                col_has.add((j, x))
                sub_box_has.add((i // 3, j // 3, x))

        return True
```

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True
```
