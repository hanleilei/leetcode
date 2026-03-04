# Special Positions in a Binary Matrix

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

## Example 1

![](https://assets.leetcode.com/uploads/2021/12/23/special1.jpg)

```text
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
```

## Example 2

![](https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg)

```text
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
```

## Constraints

```text
m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
```

完全阅读理解问题。。

```python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(i) for i in mat]
        cols = [sum(j) for j in zip(*mat)]
        res = 0
        ones = [(i, j) for i in range(len(mat)) for j in range(len(mat[i])) if mat[i][j] == 1]
        for i, j in ones:
            if rows[i] == 1 and cols[j] == 1:
                res += 1
        return res
```

```python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        for row in mat:
            col = -1
            for j, x in enumerate(row):
                if x == 0:
                    continue
                if col >= 0:  # 这一行有多个 1
                    col = -1
                    break  # 检查下一行
                col = j  # 记录 1 的列号
            if col < 0:
                continue

            seen1 = 0
            for r in mat:
                if r[col] == 0:
                    continue
                if seen1:  # 这一列有多个 1
                    seen1 = 0
                    break  # 检查下一行
                seen1 = 1  # 这一列有 1
            ans += seen1
        return ans
```

```python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        for r in mat:
            if sum(r) != 1:
                continue
            j = r.index(1)
            if sum(r[j] for r in mat) == 1:
                res += 1
        return res
```
