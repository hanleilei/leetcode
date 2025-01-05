# Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

![1](https://assets.leetcode.com/uploads/2018/10/12/diagonal_traverse.png)

Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:

- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 104
- 1 <= m * n <= 104
- `-10**5 <= mat[i][j] <= 10**5`

```python
from collections import deque, defaultdict
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        Property for the diagonals is that: row + col = constant. This constant varies from 0 to M+N-2.
        The direction of the diagonal is top to bottom or bottom to top. The direction depends if constant is even or odd.
        Iterate the matrix. Maintain a dictionary with key as integer and value as a deque.
        The key will be row+col and deque will have all elements which have the same row +col. Depending whether row+col is even or odd, we will either append or appendleft.
        """
        if matrix == []:
            return []
        M, N = len(matrix), len(matrix[0])
        result = defaultdict(deque)
        max_sum, top_down = M+N-2, True
        for i in range(M):
            for j in range(N):
                s = i+j
                if s&1:
                    result[s].append(matrix[i][j])
                else:
                    result[s].appendleft(matrix[i][j])
        output = []
        for s in range(max_sum+1):
            output.extend(result[s])
        return output
```
