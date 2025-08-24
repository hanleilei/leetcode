# Find the Minimum Area to Cover All Ones I

You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

Example 1:

Input: grid = [[0,1,0],[1,0,1]]

Output: 6

Explanation:

![0](https://assets.leetcode.com/uploads/2024/05/08/examplerect0.png)

The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

Example 2:

Input: grid = [[1,0],[0,0]]

Output: 1

Explanation:

![1](https://assets.leetcode.com/uploads/2024/05/08/examplerect1.png)

The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

Constraints:

```text
1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 0 or 1.
The input is generated such that there is at least one 1 in grid.
```

思路：
找到包含所有1的最小矩形的左、右、上、下边界，然后计算面积。

```python
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left, right, up, down = 1000, -1, 1000, -1
        for i in range(len(grid)): 
            for j in range(len(grid[i])):
                    if grid[i][j] == 1:
                        left = min(j, left)
                        right = max(j, right)
                        up = min(i, up)
                        down = max(i, down)
        return (down - up + 1) * (right - left + 1)
```
