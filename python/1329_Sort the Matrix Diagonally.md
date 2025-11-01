# Sort the Matrix Diagonally

[[array]] [[matrix]] [[sorting]]

## Problem Description

A **matrix diagonal** is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from `mat[2][0]`, where `mat` is a 6 x 3 matrix, includes cells `mat[2][0]`, `mat[3][1]`, and `mat[4][2]`.

Given an `m x n` matrix `mat` of integers, sort each matrix diagonal in **ascending order** and return *the resulting matrix*.

## Examples

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2020/01/21/1482_example_1_2.png)

```text
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
```

**Example 2:**

```text
Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
```

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `1 <= mat[i][j] <= 100`

## 解法一：哈希表分组（最优解）

```python
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        
        # 收集每条对角线的元素
        for i in range(m):
            for j in range(n):
                # 关键洞察：同一对角线上的点满足 i-j 相等
                diagonals[i - j].append(mat[i][j])
        
        # 对每条对角线排序（逆序，便于后续pop操作）
        for diagonal in diagonals.values():
            diagonal.sort(reverse=True)
        
        # 将排序后的元素重新填回矩阵
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()
        
        return mat
```

**核心思想：**

- **对角线识别**：同一条对角线上的点满足 `i - j = 常数`
- **分组排序**：用哈希表按 `i - j` 值分组收集元素
- **逆序排序**：方便后续使用 `pop()` 从末尾取元素
- **重新填充**：按原位置将排序后的元素填回

**时间复杂度：** O(m × n × log(min(m,n))) - 排序的复杂度
**空间复杂度：** O(m × n) - 存储所有元素

## 解法二：直接对角线处理

```python
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        # 处理从第一行开始的对角线
        for start_col in range(n):
            diagonal = []
            i, j = 0, start_col
            
            # 收集对角线元素
            while i < m and j < n:
                diagonal.append(mat[i][j])
                i += 1
                j += 1
            
            # 排序
            diagonal.sort()
            
            # 重新填回
            i, j = 0, start_col
            for val in diagonal:
                mat[i][j] = val
                i += 1
                j += 1
        
        # 处理从第一列开始的对角线（跳过[0,0]）
        for start_row in range(1, m):
            diagonal = []
            i, j = start_row, 0
            
            # 收集对角线元素
            while i < m and j < n:
                diagonal.append(mat[i][j])
                i += 1
                j += 1
            
            # 排序
            diagonal.sort()
            
            # 重新填回
            i, j = start_row, 0
            for val in diagonal:
                mat[i][j] = val
                i += 1
                j += 1
        
        return mat
```

更直观的方法，分别处理从第一行和第一列开始的对角线。

## 解法三：原地排序优化

```python
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        def sort_diagonal(start_i, start_j):
            """对从(start_i, start_j)开始的对角线进行排序"""
            diagonal = []
            i, j = start_i, start_j
            
            # 收集对角线元素
            while i < m and j < n:
                diagonal.append(mat[i][j])
                i += 1
                j += 1
            
            # 排序
            diagonal.sort()
            
            # 重新填回
            i, j = start_i, start_j
            for val in diagonal:
                mat[i][j] = val
                i += 1
                j += 1
        
        # 处理所有对角线
        # 从第一行开始的对角线
        for j in range(n):
            sort_diagonal(0, j)
        
        # 从第一列开始的对角线（跳过[0,0]）
        for i in range(1, m):
            sort_diagonal(i, 0)
        
        return mat
```

将对角线排序逻辑封装成函数，代码更清晰。

## 算法分析

### 对角线的数学性质

```text
矩阵示例：
0 1 2
3 4 5
6 7 8

对角线分组（按 i-j 值）：
i-j = -2: [2]
i-j = -1: [1, 5] 
i-j =  0: [0, 4, 8]
i-j =  1: [3, 7]
i-j =  2: [6]
```

### 为什么使用 i-j 作为键？

- **唯一性**：同一对角线上的所有点都有相同的 `i-j` 值
- **完整性**：不同对角线有不同的 `i-j` 值
- **简洁性**：一个简单的数学表达式就能标识对角线

### 复杂度对比

| 方法 | 时间复杂度 | 空间复杂度 | 优缺点 |
|------|------------|------------|--------|
| 哈希表分组 | O(mn log(min(m,n))) | O(mn) | ✅ 最简洁 |
| 直接处理 | O(mn log(min(m,n))) | O(min(m,n)) | 空间优化 |
| 函数封装 | O(mn log(min(m,n))) | O(min(m,n)) | 代码清晰 |

## 相关题目

- [48. Rotate Image](048_rotate_image.md) - 旋转图像
- [54. Spiral Matrix](054_spiral_matrix.md) - 螺旋矩阵
- [498. Diagonal Traverse](498_diagonal_traverse.md) - 对角线遍历
