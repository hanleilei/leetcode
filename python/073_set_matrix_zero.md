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
有点追求，将运算时间提高了一下，可以看得出来：enumerate是一个很消耗时间的函数，最好别用。

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
