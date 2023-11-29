# Largest Submatrix With Rearrangements

You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

## Example 1

![](https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40536-pm.png)

```pythhon
Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
```

## Example 2

![](https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40852-pm.png)

```text
Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
```

## Example 3

```text
Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
```

## Constraints

```text
m == matrix.length
n == matrix[i].length
1 <= m * n <= 105
matrix[i][j] is either 0 or 1.
```

类似于85题：`https://leetcode.com/problems/maximal-rectangle/`

思路和步骤如下：

1. 修改一下二维数组
2. 每一行排序
3. 计算最大值

```python
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
		 [ [1, 0, 1, 1]                          [ [1, 0, 1, 1]  
		   [1, 0, 1, 0]           -->              [2, 0, 2, 0] 
		   [0, 1, 1, 0] ]                          [0, 1, 3, 0] ]
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = matrix[i-1][j] + 1
        res = 0
        for i in range(m):
            matrix[i].sort()
            for j in range(1, n+1):
                res = max(res, j * matrix[i][n - j])
        return res
```

其余所谓的各式各样的方法，都是上面的方法变化一下，比方说排序的时候是逆序之类的。
