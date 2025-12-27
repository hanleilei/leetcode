# Rotate Image

[[matrix]] [[math]]

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

## Examples

### Example 1

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

原矩阵:    旋转90°后:
1 2 3  →   7 4 1
4 5 6      8 5 2  
7 8 9      9 6 3
```

### Example 2

![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

```text
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

原矩阵:          旋转90°后:
5  1  9  11  →   15 13 2  5
2  4  8  10      14 3  4  1
13 3  6  7       12 6  8  9
15 14 12 16      16 7  10 11
```

## Constraints

- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

## 解题思路

90度顺时针旋转可以通过两步变换实现：

1. **转置矩阵**（沿主对角线翻转）
2. **水平翻转**（每行倒序）

或者：

1. **垂直翻转**（上下翻转）
2. **转置矩阵**（沿主对角线翻转）

## 解法一：转置 + 水平翻转（推荐）

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # 步骤1：转置矩阵（沿主对角线翻转）
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 步骤2：水平翻转每一行
        for row in matrix:
            self.reverse(row)
    
    def reverse(self, arr):
        """原地反转数组"""
        i, j = 0, len(arr) - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
```

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in matrix:
            i[:] = i[::-1]
        return matrix
```

**可视化过程**：

```text
原矩阵:     转置后:     水平翻转后:
1 2 3  →   1 4 7  →   7 4 1
4 5 6      2 5 8      8 5 2
7 8 9      3 6 9      9 6 3
```

## 解法二：垂直翻转 + 转置

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 步骤1：垂直翻转（上下翻转）
        matrix.reverse()
        
        # 步骤2：转置矩阵
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

**可视化过程**：

```text
原矩阵:     垂直翻转后:   转置后:
1 2 3  →   7 8 9    →   7 4 1
4 5 6      4 5 6        8 5 2
7 8 9      1 2 3        9 6 3
```

## 解法三：环形旋转（一次遍历）

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        四元素循环交换，一次性完成旋转
        """
        n = len(matrix)
        
        # 处理每一层（环）
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            
            # 在当前层中，处理每个需要旋转的位置
            for i in range(first, last):
                offset = i - first
                
                # 保存top元素
                top = matrix[first][i]
                
                # left → top
                matrix[first][i] = matrix[last - offset][first]
                
                # bottom → left  
                matrix[last - offset][first] = matrix[last][last - offset]
                
                # right → bottom
                matrix[last][last - offset] = matrix[i][last]
                
                # top → right
                matrix[i][last] = top
```

**算法说明**：

- 将矩阵分为多个同心环
- 每个环内的元素按照 top → right → bottom → left → top 的顺序循环交换

## 解法四：Python 特色解法

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        利用 Python 的 zip 和切片特性
        """
        # matrix[::-1] 垂直翻转
        # zip(*matrix[::-1]) 转置
        # matrix[:] = ... 原地修改
        matrix[:] = zip(*matrix[::-1])
```

**解释**：

- `matrix[::-1]`：垂直翻转矩阵
- `zip(*matrix[::-1])`：转置操作
- `matrix[:] = ...`：原地修改，不创建新矩阵

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 解法一 | O(n²) | O(1) | 思路清晰，两步完成 |
| 解法二 | O(n²) | O(1) | 利用内置函数，简洁 |
| 解法三 | O(n²) | O(1) | 一次遍历，最优效率 |
| 解法四 | O(n²) | O(1) | Python特色，代码最短 |

## 关键要点

1. **原地操作**：不能使用额外的 n×n 矩阵
2. **两步变换**：转置+翻转 或 翻转+转置
3. **环形思维**：将矩阵看作同心环，逐层处理
4. **数学关系**：`matrix[i][j] → matrix[j][n-1-i]`

## 相关题目

- [73. Set Matrix Zeroes](../073_set_matrix_zero.md)
- [54. Spiral Matrix](../054_spiral_matrix.md)
- [59. Spiral Matrix II](../059_spiral_matrix_ii.md)
