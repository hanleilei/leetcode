# Maximum Score From Grid Operations

[[dp]]

You are given a 2D matrix grid of size n x n. Initially, all cells of the grid are colored white. In one operation, you can select any cell of indices (i, j), and color black all the cells of the jth column starting from the top row down to the ith row.

The grid score is the sum of all grid[i][j] such that cell (i, j) is white and it has a horizontally adjacent black cell.

Return the maximum score that can be achieved after some number of operations.

Example 1:

Input: grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]

Output: 11

Explanation:

![](https://assets.leetcode.com/uploads/2024/05/11/one.png)

In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is grid[3][0] + grid[1][2] + grid[3][3] which is equal to 11.

Example 2:

Input: grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]

Output: 94

Explanation:

![](https://assets.leetcode.com/uploads/2024/05/11/two-1.png)

We perform operations on 1, 2, and 3 down to rows 1, 4, and 0, respectively. The score of the resulting grid is grid[0][0] + grid[1][0] + grid[2][1] + grid[4][1] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] + grid[0][4] which is equal to 94.

Constraints:

    1 <= n == grid.length <= 100
    n == grid[i].length
    0 <= grid[i][j] <= 10^9

这个题目，从第一列的任意行开始，到最后一列的任意行结束，每一步可以向右、右上、右下移动，路径分数是所有经过单元格值的和，求最大分数。

```python
class Solution:
    def maximumScore(self, grid) -> int:
        """
        计算矩阵中的最大分数路径
        规则：从第一列的任意行开始，到最后一列的任意行结束
        每一步可以向右、右上、右下移动
        路径分数是所有经过单元格值的和
        """
        n = len(grid)
        if n < 2:
            return 0
        if n == 2:
            return max(grid[0][0] + grid[1][0], grid[0][1] + grid[1][1])

        # 计算列的前缀和，便于快速计算垂直方向的分数
        prefix_grid = [[0] * n] + [row[:] for row in grid]
        for r in range(1, n + 1):
            prev_row = prefix_grid[r - 1]
            curr_row = prefix_grid[r]
            for c in range(n):
                curr_row[c] += prev_row[c]

        # dp数组：保存前一列的分数
        prev_up = [0] * (n + 1)  # 从上方到达当前列的分数
        prev_down = [0] * (n + 1)  # 从下方到达当前列的分数
        
        # 临时数组：计算当前列的分数
        curr_up = [0] * (n + 1)
        curr_down = [0] * (n + 1)

        # 动态规划：从左到右处理每一列
        for col in range(1, n):
            # 计算从上方来的最优路径分数
            best_from_up = prev_up[0] - prefix_grid[0][col - 1]
            for row in range(n + 1):
                # 从上方到达(row, col)的分数
                curr_up[row] = prefix_grid[row][col - 1] + best_from_up
                
                # 更新从上方来的最优分数
                up_diff = prev_up[row] - prefix_grid[row][col - 1]
                if up_diff > best_from_up:
                    best_from_up = up_diff
            
            # 与从下方来的路径比较
            if prev_down[0] > curr_up[0]:
                curr_up[0] = prev_down[0]
            if prev_down[0] > curr_up[n]:
                curr_up[n] = prev_down[0]

            # 计算从下方来的最优路径分数
            best_from_down = prev_down[n] + prefix_grid[n][col]
            for row in range(n, -1, -1):
                # 从下方到达(row, col)的分数
                curr_down[row] = best_from_down - prefix_grid[row][col]
                
                # 更新从下方来的最优分数
                down_diff = prev_down[row] + prefix_grid[row][col]
                if down_diff > best_from_down:
                    best_from_down = down_diff
            
            # 与从上方来的路径比较
            if curr_up[n] > curr_down[n]:
                curr_down[n] = curr_up[n]

            # 为下一列做准备
            prev_up, prev_down, curr_up, curr_down = curr_up, curr_down, prev_up, prev_down

        # 返回最大分数
        return max(max(prev_up), max(prev_down))
```
