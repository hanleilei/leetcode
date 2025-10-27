# Spiral Matrix

[[matrix]] [[simulation]]

Given an `m x n` matrix, return all elements of the matrix in spiral order.

## Examples

### Example 1

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

可视化螺旋路径：
1 → 2 → 3
        ↓
4 → 5   6
↑       ↓
7 ← 8 ← 9
```

### Example 2

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

```text
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

可视化螺旋路径：
1 → 2 → 3 → 4
            ↓
5 → 6 → 7   8
↑           ↓
9 ← 10← 11← 12
```

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## 解题思路

螺旋遍历的核心是维护四个边界，按照 **右→下→左→上** 的顺序循环遍历，每次遍历完一条边就收缩对应边界。

### 算法步骤

1. **初始化边界**：`top=0, bottom=m-1, left=0, right=n-1`
2. **循环遍历**：
   - 向右：遍历 `[left, right]`，然后 `top++`
   - 向下：遍历 `[top, bottom]`，然后 `right--`
   - 向左：遍历 `[right, left]`，然后 `bottom--`
   - 向上：遍历 `[bottom, top]`，然后 `left++`
3. **边界检查**：每次遍历后检查是否越界

## 解法一：边界模拟法（推荐）

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 向右遍历上边界
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            
            # 向下遍历右边界
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            
            # 向左遍历下边界（需要检查是否还有行）
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            
            # 向上遍历左边界（需要检查是否还有列）
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
        
        return res
```

**复杂度分析**：
- 时间复杂度：O(m × n) - 每个元素访问一次
- 空间复杂度：O(1) - 除输出数组外只使用常数空间

## 解法二：矩阵旋转法（巧妙）

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            # 取第一行
            res.extend(matrix.pop(0))
            # 矩阵逆时针旋转90度：转置 + 翻转
            matrix = [*zip(*matrix)][::-1]
        return res
```

**核心思想**：每次取第一行，然后将矩阵逆时针旋转90度，重复直到矩阵为空。

**矩阵旋转原理**：
- `zip(*matrix)`：转置矩阵
- `[::-1]`：垂直翻转
- 组合效果：逆时针旋转90度

## 解法三：递归法（Stephan大神风格）

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and matrix.pop(0) + self.spiralOrder([*zip(*matrix)][::-1])
```

**一行代码解法**：
- `matrix and`：短路求值，矩阵为空时返回空列表
- `matrix.pop(0)`：取第一行
- 递归处理旋转后的矩阵

## 解法四：方向向量法

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        
        # 方向向量：右、下、左、上
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        
        row = col = 0
        res = []
        
        for _ in range(m * n):
            res.append(matrix[row][col])
            visited[row][col] = True
            
            # 计算下一个位置
            next_row = row + directions[direction_idx][0]
            next_col = col + directions[direction_idx][1]
            
            # 检查是否需要转向
            if (next_row < 0 or next_row >= m or 
                next_col < 0 or next_col >= n or 
                visited[next_row][next_col]):
                direction_idx = (direction_idx + 1) % 4
                next_row = row + directions[direction_idx][0]
                next_col = col + directions[direction_idx][1]
            
            row, col = next_row, next_col
        
        return res
```

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 边界模拟 | O(m×n) | O(1) | 直观易懂，推荐面试使用 |
| 矩阵旋转 | O(m×n) | O(min(m,n)) | 代码简洁，思路巧妙 |
| 递归法 | O(m×n) | O(min(m,n)) | 一行代码，函数式风格 |
| 方向向量 | O(m×n) | O(m×n) | 通用模板，适用类似问题 |

## 关键要点

1. **边界处理**：注意向左和向上遍历时的边界检查
2. **循环条件**：使用 `while top <= bottom and left <= right`
3. **矩阵旋转**：`[*zip(*matrix)][::-1]` 实现逆时针旋转90度
4. **方向控制**：按照固定顺序（右→下→左→上）遍历

## 相关题目

- [48. Rotate Image](048_rotate_image.md) - 矩阵旋转
- [59. Spiral Matrix II](059_spiral_matrix_ii.md) - 螺旋矩阵生成
- [885. Spiral Matrix III](885_spiral_matrix_iii.md) - 扩展螺旋遍历

经典的矩阵遍历问题，推荐掌握边界模拟法和矩阵旋转法两种思路。
