# Determine Whether Matrix Can Be Obtained By Rotation

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

Example 1:

![](https://assets.leetcode.com/uploads/2021/05/20/grid3.png)

Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:

![](https://assets.leetcode.com/uploads/2021/05/20/grid4.png)

Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:

![](https://assets.leetcode.com/uploads/2021/05/26/grid4.png)

Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

Constraints:

    n == mat.length == target.length
    n == mat[i].length == target[i].length
    1 <= n <= 10
    mat[i][j] and target[i][j] are either 0 or 1.

枚举 mat 旋转 0,1,2,3 次，判断旋转后的 mat 是否等于 target。旋转算法来自 48. Rotate Image。

```python
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            self.rotate(mat)
        return False
    
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i, row in enumerate(matrix):
            for j in range(i + 1, n):
                row[j], matrix[j][i] = matrix[j][i], row[j]
            row.reverse()
        
```
