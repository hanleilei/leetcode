# Search a 2D Matrix II

[[binarysearch]]

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:

![](https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg)

Input: matrix = `[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]`, target = 5
Output: true
Example 2:

![](https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg)

Input: matrix = `[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]`, target = 20
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
$-10^9 <= matrix[i][j] <= 10^9$
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
$-10^9 <= target <= 10^9$

解法一：

这个思路很巧妙，从右上角开始，如果当前元素大于目标值，那么说明目标值不可能在当前列，直接往左走；如果当前元素小于目标值，那么说明目标值不可能在当前行，直接往下走；如果当前元素等于目标值，那么就找到了。

```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n=len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while 0 <= i < m and 0 <= j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
```

解法二：

这个思路和解法一类似，不过是从左下角开始，如果当前元素大于目标值，那么说明目标值不可能在当前行，直接往上走；如果当前元素小于目标值，那么说明目标值不可能在当前列，直接往右走；如果当前元素等于目标值，那么就找到了。

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False
```
