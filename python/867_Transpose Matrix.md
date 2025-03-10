# Transpose Matrix

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

![](https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png)

## Example 1

```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

## Example 2

```text
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

## Constraints

```text
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
```

问题是leetcode 48 题目的简化版。

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)
```


转置矩阵就是把 M 行 N 列的矩阵，转成 N 行 M 列的矩阵，原来矩阵中 matrix[i][j] 的位置，会交换到新矩阵的 res[j][i] 位置。

矩阵的行列数可能不等，因此不能做原地操作，需要新建数组。

对角线翻转，只需要从头模拟一遍即可。

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0] * m for i in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res
```

来个速度快的：

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        count = len(matrix[0])
        for j in range(count):
            tmp = []
            for i in range(len(matrix)):
                tmp.append(matrix[i][j])
            result.append(tmp)
        return result
```

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        import numpy as np
        return np.transpose(matrix).tolist()
```
