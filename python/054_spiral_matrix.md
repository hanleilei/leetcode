# spiral matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

## Example 1

```text
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
```

## Example 2

```text
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

注意求矩阵转置的写法：
```[*zip(*matrix)][::-1]```

```python
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
        return res
```

然后看看stephan大神的写法，非常的飘逸

```python
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and matrix.pop(0) + self.spiralOrder([list(x) for x in zip(*matrix)][::-1])

```

来一个模拟题目含义的方法：

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return list()
        L,R,T,B,res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, list()
        while True:
            for i in range(L, R+1):
                res.append(matrix[T][i]) # left to right
            T += 1
            if T > B: break
            for i in range(T, B + 1): 
                res.append(matrix[i][R]) # top to down
            R -= 1
            if L > R: break
            for i in range(R, L -1, -1):
                res.append(matrix[B][i]) # right to left
            B -= 1
            if T > B:
                break
            for i in range(B, T-1, -1):
                res.append(matrix[i][L]) # bottom to top
            L += 1
            if L > R: break
        return res
```
