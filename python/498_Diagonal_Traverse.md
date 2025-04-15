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

![1](https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg)

Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:

- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 104
- 1 <= m * n <= 104
- `-10**5 <= mat[i][j] <= 10**5`

问题的关键：
1. 找到元素的索引和
2. 判断索引和的奇偶性，来决定元素的方向。


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
                if s&1:  # 这个写法，有点迷惑。。
                    result[s].append(matrix[i][j])
                else:
                    result[s].appendleft(matrix[i][j])
        output = []
        for s in range(max_sum+1):
            output.extend(result[s])
        return output
```

```python
class Solution:
    
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Check for an empty matrix
        if not matrix or not matrix[0]:
            return []
        
        # The dimensions of the matrix
        N, M = len(matrix), len(matrix[0])
        
        # Incides that will help us progress through 
        # the matrix, one element at a time.
        row, column = 0, 0
        
        # As explained in the article, this is the variable
        # that helps us keep track of what direction we are
        # processing the current diaonal
        direction = 1
        
        # Final result array that will contain all the elements
        # of the matrix
        result = []
        
        # The uber while loop which will help us iterate over all
        # the elements in the array.
        while row < N and column < M:
            
            # First and foremost, add the current element to 
            # the result matrix. 
            result.append(matrix[row][column])
            
            # Move along in the current diagonal depending upon
            # the current direction.[i, j] -> [i - 1, j + 1] if 
            # going up and [i, j] -> [i + 1][j - 1] if going down.
            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)
            
            # Checking if the next element in the diagonal is within the
            # bounds of the matrix or not. If it's not within the bounds,
            # we have to find the next head. 
            if new_row < 0 or new_row == N or new_column < 0 or new_column == M:
                
                # If the current diagonal was going in the upwards
                # direction.
                if direction:
                    
                    # For an upwards going diagonal having [i, j] as its tail
                    # If [i, j + 1] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i + 1, j] becomes the next head
                    row += (column == M - 1)
                    column += (column < M - 1)
                else:
                    
                    # For a downwards going diagonal having [i, j] as its tail
                    # if [i + 1, j] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i, j + 1] becomes the next head
                    column += (row == N - 1)
                    row += (row < N - 1)
                    
                # Flip the direction
                direction = 1 - direction        
            else:
                row = new_row
                column = new_column
                        
        return result
```

再来一个简洁的：

```python
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        res = list()
        d = defaultdict(list)
        if not matrix: return res
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                d[i + j + 1].append(matrix[i][j])
        for k in sorted(d.keys()):
            if k % 2 == 1: d[k].reverse()
            res += d[k]
        return res
```

```python
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        d = defaultdict(deque)
        
        for i in range(m):
            for j in range(n):
                if (i + j) % 2 == 0:  # 偶数对角线，从下往上遍历
                    d[i + j].appendleft(matrix[i][j])
                else:  # 奇数对角线，从上往下遍历
                    d[i + j].append(matrix[i][j])
        
        # 按对角线顺序拼接结果
        res = []
        for diagonal in range(m + n - 1):
            res.extend(d[diagonal])
        
        return res
```
