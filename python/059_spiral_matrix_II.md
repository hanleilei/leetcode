# Spiral Matrix II

[[matrix]] [[simulation]]

Given a positive integer `n`, generate an `n x n` matrix filled with elements from 1 to n² in spiral order.

## Examples

### Example 1

![](https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg)

```text
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

可视化螺旋填充：
1 → 2 → 3
        ↓
8 → 9   4
↑       ↓
7 ← 6 ← 5
```

### Example 2

```text
Input: n = 1
Output: [[1]]
```

## Constraints

- `1 <= n <= 20`

## 解题思路

螺旋矩阵生成是螺旋矩阵遍历的逆向过程。核心思想是维护四个边界，按照 **右→下→左→上** 的顺序循环填充，每填充完一条边就收缩对应边界。

### 算法步骤

1. **初始化**：创建 n×n 零矩阵，设定边界和计数器
2. **循环填充**：
   - 向右：填充上边界，然后上边界下移
   - 向下：填充右边界，然后右边界左移  
   - 向左：填充下边界，然后下边界上移
   - 向上：填充左边界，然后左边界右移
3. **边界检查**：每次填充后检查是否完成

## 解法一：边界模拟法（推荐）

和54类似，但是，不用做边界

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        upper, lower = 0, n
        left, right = 0, n
        c = 1

        while c <= n * n:
            # 向右遍历上边界
            for i in range(left, right):
                matrix[upper][i] = c
                c += 1
            upper += 1
            # if upper >= lower:  # 添加边界检查
            #     break

            # 向下遍历右边界
            for j in range(upper, lower):
                matrix[j][right - 1] = c
                c += 1
            right -= 1
            # if left >= right:  # 添加边界检查
            #     break

            # 向左遍历下边界
            for k in range(right - 1, left - 1, -1):
                matrix[lower - 1][k] = c
                c += 1
            lower -= 1
            # if upper >= lower:  # 添加边界检查
            #     break

            # 向上遍历左边界
            for t in range(lower - 1, upper - 1, -1):
                matrix[t][left] = c
                c += 1
            left += 1
            # if left >= right:  # 添加边界检查
            #     break

        return matrix
```

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        
        while top <= bottom and left <= right:
            # 向右填充上边界
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            # 向下填充右边界
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            # 向左填充下边界
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1
            
            # 向上填充左边界
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1
        
        return matrix
```

**复杂度分析**：

- 时间复杂度：O(n²) - 填充 n² 个位置
- 空间复杂度：O(1) - 除输出矩阵外只使用常数空间

## 解法二：方向向量法

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        # 方向向量：右、下、左、上
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        
        row = col = 0
        
        for num in range(1, n * n + 1):
            matrix[row][col] = num
            
            # 计算下一个位置
            next_row = row + directions[direction_idx][0]
            next_col = col + directions[direction_idx][1]
            
            # 检查是否需要转向
            if (next_row < 0 or next_row >= n or 
                next_col < 0 or next_col >= n or 
                matrix[next_row][next_col] != 0):
                direction_idx = (direction_idx + 1) % 4
                next_row = row + directions[direction_idx][0]
                next_col = col + directions[direction_idx][1]
            
            row, col = next_row, next_col
        
        return matrix
```

**核心思想**：使用方向向量控制移动方向，遇到边界或已填充位置时转向。

## 解法三：Stefan大神的方向控制法

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1  # 初始位置(0,0)，初始方向向右
        
        for k in range(n * n):
            matrix[i][j] = k + 1
            
            # 检查下一个位置是否需要转向
            if matrix[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di  # 顺时针转向：(0,1)→(1,0)→(0,-1)→(-1,0)
            
            i += di
            j += dj
        
        return matrix
```

**巧妙之处**：

- 使用取模运算处理边界
- 通过 `(di, dj) = (dj, -di)` 实现顺时针转向
- 检测已填充位置来判断转向时机

## 解法四：逆向构造法（Stefan的另一个思路）

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix, lo = [], n * n + 1
        
        while lo > 1:
            lo, hi = lo - len(matrix), lo
            matrix = [list(range(lo, hi))] + [list(row) for row in zip(*matrix[::-1])]
        
        return matrix
```

**构造过程可视化**：

```text
n = 3 的构造过程：
||  =>  |9|  =>  |8 9|  =>  |6 7|  =>  |1 2 3|
               |9|     |9 8|     |9 6|     |8 9 4|
                               |8 7|     |7 6 5|
```

**核心思想**：

- 从内向外逆向构造
- 每次添加一行，然后将矩阵逆时针旋转90度
- `zip(*matrix[::-1])` 实现逆时针旋转

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 边界模拟 | O(n²) | O(1) | 直观易懂，推荐面试使用 |
| 方向向量 | O(n²) | O(1) | 通用模板，适用类似问题 |
| 方向控制 | O(n²) | O(1) | 代码简洁，巧用取模 |
| 逆向构造 | O(n²) | O(n²) | 思路独特，函数式风格 |

## 关键要点

1. **边界处理**：注意 n=1 的特殊情况
2. **转向条件**：遇到边界或已填充位置时转向
3. **方向控制**：掌握 `(di, dj) = (dj, -di)` 的转向技巧
4. **矩阵旋转**：`zip(*matrix[::-1])` 实现逆时针旋转90度

## 相关题目

- [54. Spiral Matrix](054_spiral_matrix.md) - 螺旋遍历矩阵
- [48. Rotate Image](048_rotated_image.md) - 矩阵旋转
- [885. Spiral Matrix III](885_spiral_matrix_iii.md) - 扩展螺旋问题

这是螺旋矩阵的经典生成问题，推荐掌握边界模拟法和方向向量法两种核心思路。
