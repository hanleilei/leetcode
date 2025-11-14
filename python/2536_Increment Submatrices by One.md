# 2536. Increment Submatrices by One

[[二维差分数组]]

## 问题描述

You are given a positive integer n, indicating that we initially have
an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query\[i\] =
\[row1i, col1i, row2i, col2i\], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner
(row1i, col1i) and the bottom right corner (row2i, col2i). That is,
add 1 to mat\[x\]\[y\] for all row1i <= x <= row2i and
col1i <= y <= col2i.

Return the matrix mat after performing every query.

## 示例

**Example 1:**

```text
Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
```

Explanation: The diagram above shows the initial matrix, the matrix
after the first query, and the matrix after the second query.

- In the first query, we add 1 to every element in the submatrix with
  the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with
  the top left corner (0, 0) and bottom right corner (1, 1).

**Example 2:**

```text
Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
```

Explanation: In the first query we add 1 to every element in the
matrix.

## 约束条件

- 1 <= n <= 500
- 1 <= queries.length <= 10^4
- 0 <= row1i <= row2i < n
- 0 <= col1i <= col2i < n

## 解法

### 方法1：二维差分数组（推荐）

使用二维差分数组来高效处理多次区间更新操作。

核心思想：二维差分数组允许在 O(1) 时间内标记一个矩形区域的增量，
最后通过前缀和还原得到实际的值。对于矩形区域 (r1,c1) 到
(r2,c2)，在差分数组中做四次操作：

- diff\[r1\]\[c1\] += 1 (左上角加1)
- diff\[r1\]\[c2+1\] -= 1 (右边界外减1)
- diff\[r2+1\]\[c1\] -= 1 (下边界外减1)
- diff\[r2+1\]\[c2+1\] += 1 (右下角外加1，抵消重复减)

```python
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # 创建 (n+2) x (n+2) 的差分数组，避免边界判断
        diff = [[0] * (n + 2) for _ in range(n + 2)]

        # 对每个查询，在差分数组中标记
        for r1, c1, r2, c2 in queries:
            # 注意：索引+1是因为diff数组多了一圈边界
            diff[r1 + 1][c1 + 1] += 1        # 左上角
            diff[r1 + 1][c2 + 2] -= 1        # 右边界外
            diff[r2 + 2][c1 + 1] -= 1        # 下边界外
            diff[r2 + 2][c2 + 2] += 1        # 右下角外

        # 通过二维前缀和还原实际值
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # 二维前缀和公式
                diff[i + 1][j + 1] += (
                    diff[i + 1][j] + 
                    diff[i][j + 1] - 
                    diff[i][j]
                )
                res[i][j] = diff[i + 1][j + 1]

        return res
```

### 方法2：朴素方法（不推荐，会超时）

直接对每个查询更新矩形区域内的所有元素。

```python
class Solution:
    def rangeAddQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]

        # 对每个查询，遍历矩形区域内所有元素
        for r1, c1, r2, c2 in queries:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    res[i][j] += 1

        return res
```

## 算法分析

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 二维差分数组 | O(q + n²) | O(n²) | q为查询数，标记O(q)，还原O(n²) |
| 朴素方法 | O(q·n²) | O(n²) | 每次查询遍历矩形区域 |

二维差分数组详细分析：

- 标记阶段：每个查询只需4次操作，总共 O(4q) = O(q)
- 还原阶段：遍历整个矩阵计算前缀和，O(n²)
- 总时间：O(q + n²)
- 空间：差分数组 O((n+2)²) ≈ O(n²)

### 执行过程示例

以 n=3, queries=\[\[1,1,2,2\],\[0,0,1,1\]\] 为例。

初始差分数组（5x5，全0）：

```text
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

处理查询\[1,1,2,2\]后：

```text
0 0 0 0 0
0 1 0 -1 0
0 0 0 0 0
0 -1 0 1 0
0 0 0 0 0
```

处理查询\[0,0,1,1\]后：

```text
0 1 0 -1 0
0 1 0 -1 0
0 -1 0 1 0
0 -1 0 1 0
0 0 0 0 0
```

计算前缀和还原（取中间3x3）：

```text
1 1 0
1 2 1
0 1 1
```

## 常见错误

### 错误1：索引偏移错误

```python
# 错误：直接使用原始索引
diff[r1][c1] += 1  # 应该是 diff[r1+1][c1+1]
```

**原因：** 差分数组比原矩阵大一圈，需要索引+1

### 错误2：边界处理遗漏

```python
# 错误：未考虑边界情况
diff = [[0] * n for _ in range(n)]  # 应该是 (n+2) x (n+2)
```

**原因：** 需要额外的边界空间来避免越界检查

### 错误3：前缀和公式错误

```python
# 错误：漏掉减去重复部分
diff[i+1][j+1] += diff[i+1][j] + diff[i][j+1]  
# 正确：
# diff[i+1][j+1] += diff[i+1][j] + diff[i][j+1] - diff[i][j]
```

**原因：** 二维前缀和中 diff\[i\]\[j\] 被加了两次，需要减去

### 错误4：四个角点标记错误

```python
# 错误：遗漏右下角的补偿
diff[r1+1][c1+1] += 1
diff[r1+1][c2+2] -= 1
diff[r2+2][c1+1] -= 1
# 缺少：diff[r2+2][c2+2] += 1
```

**原因：** 右下角需要+1来抵消双重减法

## 相关题目

- [0304. Range Sum Query 2D - Immutable](./304_range_sum_query_2d_immutable.md)
- [1314. Matrix Block Sum](./1314_matrix_block_sum.md)
- [1738. Find Kth Largest XOR Coordinate Value](./1738_find_kth_largest_xor_coordinate_value.md)
- [2132. Stamping the Grid](./2132_stamping_the_grid.md)
- [0370. Range Addition](./370_range_addition.md)
