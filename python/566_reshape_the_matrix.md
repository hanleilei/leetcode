# reshape the matrix

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

```
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

```
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
There is no way to reshape a 2 _ 2 matrix to a 2 _ 4 matrix. So output the original matrix.
Note:

```
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

网上找到的 bumpy 的方法实现：

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
        rows = len(mat)
        cols = len(mat[0])
        T = rows * cols

        if r*c != T:
            return mat

        res = [[0 for _ in range(c)]for _ in range(r)]

        k = 0
        for i in range(rows):
            for j in range(cols):
                res[k//c][k%c] = mat[i][j]
                k+=1

        return res
```
