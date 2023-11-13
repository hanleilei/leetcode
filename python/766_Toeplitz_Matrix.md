# Toeplitz Matrix

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

## Example 1

```text
Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True

Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
```

## Example 2

```text
Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False

Explanation:
The diagonal "[1, 2]" has different elements.
```

## Note

1. matrix will be a 2D array of integers.
2. matrix will have a number of rows and columns in range [1, 20].
3. `matrix[i][j]` will be integers in range [0, 99].

## Follow up

1. What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
2. What if the matrix is so large that you can only load up a partial row into the memory at once?

其实整个题目的算法还是满直接的，对于每一行，直接忽略最后一个元素，第一行的前n-1个元素一定等于下一行的[1:n]，下面依次类推。最后忽略最后一行的第一个元素

```Python
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type m: List[List[int]]
        :rtype: bool
        """
        # return all(r1[:-1] == r2[1:] for r1,r2 in zip(m, m[1:]))
        # return all(m[i][j] == m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0])-1))
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        prev = matrix[0][:-1]
        for i in range(1, m):
            if prev != matrix[i][1:]:
                return False
            prev = matrix[i][:-1]
        return True
```

或者来一个更简洁的版本：

```python
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type m: List[List[int]]
        :rtype: bool
        """
        return all(r1[:-1] == r2[1:] for r1,r2 in zip(m, m[1:]))
        # return all(m[i][j] == m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0])-1))
```
