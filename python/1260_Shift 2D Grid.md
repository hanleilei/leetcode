# Shift 2D Grid

[[simulation]]

## Problem Description

Given a 2D `grid` of size `m x n` and an integer `k`. You need to shift the grid `k` times.

In one shift operation:

- Element at `grid[i][j]` moves to `grid[i][j + 1]`.
- Element at `grid[i][n - 1]` moves to `grid[i + 1][0]`.
- Element at `grid[m - 1][n - 1]` moves to `grid[0][0]`.

Return the 2D grid after applying shift operation `k` times.

## Examples

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2019/11/05/e1.png)

```text
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
```

**Example 2:**

![Example 2](https://assets.leetcode.com/uploads/2019/11/05/e2.png)

```text
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
```

**Example 3:**

```text
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m <= 50`
- `1 <= n <= 50`
- `-1000 <= grid[i][j] <= 1000`
- `0 <= k <= 100`

## 解法一：一维化处理（最优解）

```python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        col, nums = len(grid[0]), sum(grid, [])
        k = k % len(nums)
        nums = nums[-k:] + nums[:-k]
        return [nums[i:i+col] for i in range(0, len(nums), col)]
```

**核心思想：**

- 使用`sum(grid, [])`将二维网格扁平化为一维数组
- 对一维数组进行循环移位：`nums[-k:] + nums[:-k]`
- 将移位后的一维数组重新分割为二维网格

**时间复杂度：** O(m × n)
**空间复杂度：** O(m × n)

## 解法二：直接计算新位置

```python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # 计算当前元素在一维数组中的位置
                pos = i * n + j
                # 移位后的新位置
                new_pos = (pos + k) % (m * n)
                # 转换回二维坐标
                new_i, new_j = new_pos // n, new_pos % n
                result[new_i][new_j] = grid[i][j]
        
        return result
```

直接计算每个元素移位后的新位置，避免了一维化的步骤，逻辑更直观。

## 解法三：simulation - 过于复杂，而且效率低下

```python
class Solution:
    def shiftGrid(self, g: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(g), len(g[0])
        mat = [[0] * m for _ in range(n)]
        
        for i in range(m):
            tcol = (i + k) % m
            trow = ((i + k) // m) % n
            idx = 0
            while idx != n:
                mat[trow % n][tcol] = g[idx][i]
                trow += 1
                idx += 1
```

## 算法原理

这道题的关键是理解移位规律：

1. 把二维网格看作一维数组的折叠形式
2. 每次移位相当于在一维数组中向右移动一位
3. 移位k次等于向右移动k位，超出边界则循环

**优化要点：**

- 使用`k % (m * n)`避免不必要的重复移位
- `sum(grid, [])`是Python中扁平化二维列表的简洁写法

## 相关题目

- [189. Rotate Array](189_rotate_array.md) - 旋转数组
- [48. Rotate Image](048_rotate_image.md) - 旋转图像
