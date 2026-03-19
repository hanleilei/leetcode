# Count Submatrices with Top-Left Element and Sum Less Than k

[[prefixsum]]

You are given a 0-indexed integer matrix grid and an integer k.

Return the number of that contain the top-left element of the grid, and have a sum less than or equal to k.

Example 1:

![](https://assets.leetcode.com/uploads/2024/01/01/example1.png)

Input: grid = [[7,6,3],[6,6,1]], k = 18
Output: 4
Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.

Example 2:

![](https://assets.leetcode.com/uploads/2024/01/01/example2.png)

Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
Output: 6
Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.

Constraints:

    m == grid.length 
    n == grid[i].length
    1 <= n, m <= 1000 
    0 <= grid[i][j] <= 1000
    1 <= k <= 10^9

```python
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        if m == 0 or n == 0:
            return 0
        # 构造前缀和矩阵
        self.preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 计算每个矩阵 [0, 0, i, j] 的元素和
                self.preSum[i][j] = (self.preSum[i - 1][j] + self.preSum[i][j - 1] +
                                     grid[i - 1][j - 1] - self.preSum[i - 1][j - 1])
                if self.preSum[i][j] <= k:
                    res += 1
        return res
```

或者维护一个列前缀和数组，遍历每一行时更新列前缀和，并计算当前行的子矩阵和：

```python
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        col_sum = [0] * len(grid[0])
        ans = 0
        for row in grid:
            s = 0
            for j, x in enumerate(row):
                col_sum[j] += x
                s += col_sum[j]
                if s > k:
                    break
                ans += 1
        return ans
```

这种二维转换成一维的方式可以减少空间复杂度，同时在每一行更新列前缀和时，直接计算当前行的子矩阵和，避免了构造完整的前缀和矩阵。
