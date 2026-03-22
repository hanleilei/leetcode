# reshape the matrix

[[binarysearch]]

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

```text
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4

Output:
[[1,2,3,4]]
```

Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 \* 4 matrix, fill it row by row by using the previous list.
Example 2:

```text
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
```

Explanation:
There is no way to reshape a 2 _2 matrix to a 2_ 4 matrix. So output the original matrix.
Note:

```text
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive
```

最简单可以想到的版本就是用 itertools 的 islice 方法实现了。

```Python
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        import itertools
        it = itertools.chain(*nums)
        return [list(itertools.islice(it, c)) for _ in range(r)]
```

numpy 的方法实现：

```Python
import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums
```

还有恶心的 oneline 方法。。

```Python
def matrixReshape(self, nums, r, c):
    return nums if len(sum(nums, [])) != r * c else map(list, zip(*([iter(sum(nums, []))]*c)))
```

用 map，iter，zip 的这个方法很巧妙：

```Python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = sum(nums, [])
        if len(flat) != r * c:
            return nums
        tuples = zip(*([iter(flat)] * c))
        return map(list, tuples)
```

按照题目意思，直接来实现：

```python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # 如果矩阵的总元素数与目标矩阵的元素数不匹配，返回原矩阵
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        res = [mat[i][j] for i in range(m) for j in range(n)]
        return [res[i : i + c] for i in range(0, len(res), c)]
```

最朴素的方法，还是不要玩花里胡哨的东西，直接按题意实现就好。

```python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # 如果矩阵的总元素数与目标矩阵的元素数不匹配，返回原矩阵
        if len(mat) * len(mat[0]) != r * c:
            return mat

        # 将矩阵拉平成一维数组
        matrix = sum(mat, []) # 这个sum操作好骚

        # 构造目标矩阵
        res = [[0] * c for _ in range(r)]

        # 填充目标矩阵
        for i in range(len(matrix)):
            res[i // c][i % c] = matrix[i]

        return res
```

labuladong

```python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # 如果想成功 reshape，元素个数应该相同
        if r * c != m * n:
            return mat

        res = [[0] * c for _ in range(r)]
        for i in range(m * n):
            self.set(res, i, self.get(mat, i))
        return res

    # 通过一维坐标访问二维数组中的元素
    def get(self, matrix: List[List[int]], index: int) -> int:
        m, n = len(matrix), len(matrix[0])
        # 计算二维中的横纵坐标
        i, j = divmod(index, n)
        return matrix[i][j]

    # 通过一维坐标设置二维数组中的元素
    def set(self, matrix: List[List[int]], index: int, value: int) -> None:
        m, n = len(matrix), len(matrix[0])
        # 计算二维中的横纵坐标
        i, j = divmod(index, n)
        matrix[i][j] = value
```
