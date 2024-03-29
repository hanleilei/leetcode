# set matrix zero

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col_index=list()
        row_index = list()
        for i, m in enumerate(matrix):
            for j, n in enumerate(m):
                if n == 0:
                    col_index.append(j)
                    row_index.append(i)
        for i, m in enumerate(matrix):
            for j, n in enumerate(m):
                if i in row_index or j in col_index:
                    matrix[i][j] = 0
```

有点追求，将运算时间提高了一下，可以看得出来：enumerate 是一个很消耗时间的函数，最好别用。

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col_index=set()
        row_index = set()
        for m in range(len(matrix)):
            for n in range(len(matrix[m])):
                if matrix[m][n] == 0:
                    col_index.add(n)
                    row_index.add(m)
        for m in range(len(matrix)):
            for n in range(len(matrix[m])):
                if m in row_index or n in col_index:
                    matrix[m][n] = 0

```

自己撸出来的一个算法，有点参考岛屿数量的问题：

```Python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        m = [(i, j) for i, row in enumerate(matrix) for j, col in enumerate(row) if matrix[i][j] == 0]

        for i, j in m:
            matrix[i] = [0] * cols
            for x in range(rows):
                matrix[x][j] = 0
```

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = [[i, j] for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == 0]
        cols = set([i[1] for i in zeros])
        rows = set([i[0] for i in zeros])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
```
