# transpose matrix

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Example 1:

```
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

Example 2:

```
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

就是一个小坑，怎么在Python中构建二维数组，使用 [[0] *m ]* n 是不行的。

```python
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        c = len(A)
        r = len(A[0])
        res = [([0] * c) for i in range(r)]
        for i in range(c):
            for j in range(r):
                res[j][i] = A[i][j]
        return res
```

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        index = [i for i, v in enumerate(bin(n)) if v == '1']
        return max([b - a for a, b in zip(index, index[1:])] or [0])
```

bit manipulation:

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        n //= (n & -n) * 2  # 去掉 n 末尾的 100..0
        while n > 0:
            gap = (n & -n).bit_length()  # n 的尾零个数加一
            ans = max(ans, gap)
            n >>= gap  # 去掉 n 末尾的 100..0
        return ans
```
