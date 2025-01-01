# Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

Follow up: Could you find an O(n + m) solution?

对于O(n*m)的解法，直接遍历即可。

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([1 for g in grid for i in g if i < 0])
```

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i = len(grid) - 1
        j = 0
        count = 0
        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                count += len(grid[0]) - j
                i -= 1
            else:
                j += 1
        return count
```

阅读理解：which is sorted in non-increasing order both row-wise and column-wise,

这个条件是什么意思？

如果当前元素 grid[i][j] 是负数，则说明当前行从 j 到最后一列的所有元素都是负数（因为矩阵按行和列都按非递增顺序排列）。

所以也可以有二分法的解法。

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bin(row):
            start, end = 0, len(row)
            while start<end:
                mid = start +(end -start) // 2
                if row[mid]<0:
                    end = mid
                else:
                    start = mid+1
            return len(row)- start
        
        count = 0
        for row in grid:
            count += bin(row)
        return(count)            
```

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            # 创建一个反转行的视图
            reversed_row = [row[~i] for i in range(len(row))]
            # 使用二分法查找第一个小于 0 的索引
            neg_index = bisect_left(reversed_row, 0)
            count += neg_index  # 负数个数等于从反转数组的开头到 `neg_index`
        return count
```

来自lee215的解法：

```python
class Solution:
    def countNegatives(self, A: List[List[int]]) -> int:
        return sum(bisect_left(type('', (), {'__getitem__': lambda _, i: r[~i]})(), 0, 0, len(r)) for r in A)
```
