# Kth Smallest Element in a Sorted Matrix

[[binary-search]] [[heap]] [[matrix]]

## Problem Description

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n²).

### Examples

**Example 1:**

```text
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13

Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
```

**Example 2:**

```text
Input: matrix = [[-5]], k = 1
Output: -5
```

### Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All rows and columns are sorted in non-decreasing order
- `1 <= k <= n^2`

---

## 解法一：二分查找+两指针计数（最优）

```python
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        使用二分查找目标值范围，结合两指针计数验证
        
        思路：
        1. 目标值必定在 [matrix[0][0], matrix[-1][-1]] 范围内
        2. 二分查找满足"有至少k个元素<=它"的最小值
        3. 计数使用两指针（从左下到右上），时间O(n)
        """
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        
        def count_less_or_equal(target):
            """计算矩阵中<=target的元素个数（O(n)算法）"""
            count = 0
            row, col = n - 1, 0  # 从左下角开始
            
            # 指针移动：往右上角走
            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    # 当前列中，从行0到row的所有元素都<=target
                    count += row + 1
                    col += 1  # 向右移动
                else:
                    # 当前元素>target，向上移动
                    row -= 1
            
            return count
        
        # 二分查找满足条件的最小值
        while left < right:
            mid = left + (right - left) // 2
            count = count_less_or_equal(mid)
            
            if count < k:
                # 还需要找更大的值
                left = mid + 1
            else:
                # mid可能就是答案，继续搜索左半边
                right = mid
        
        return left
```

**算法分析：**

- **两指针计数的关键**：从左下角 (n-1, 0) 开始
  - 若 `matrix[row][col] <= target`：说明当前列中 rows 0-row 的所有元素都 ≤ target（因为每行递增），加 row+1，向右
  - 若 `matrix[row][col] > target`：当前元素太大，向上移动
  - 这样遍历整个矩阵只需要 O(n) 时间

- **二分查找的意义**：直接在矩阵值域上二分，而非数组下标

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n log(max - min)) |
| 空间复杂度 | O(1) |

---

## 解法二：最小堆（参考）

```python
import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        使用最小堆：每次弹出最小元素，并将其右邻和下邻加入堆
        （类似Dijkstra算法的思想）
        """
        n = len(matrix)
        # (value, row, col)
        min_heap = [(matrix[0][0], 0, 0)]
        visited = {(0, 0)}
        
        for _ in range(k - 1):
            val, row, col = heapq.heappop(min_heap)
            
            # 尝试添加右邻和下邻
            if row + 1 < n and (row + 1, col) not in visited:
                heapq.heappush(min_heap, (matrix[row + 1][col], row + 1, col))
                visited.add((row + 1, col))
            
            if col + 1 < n and (row, col + 1) not in visited:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
                visited.add((row, col + 1))
        
        return heapq.heappop(min_heap)[0]
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(k log k) |
| 空间复杂度 | O(k) |

---

## 解法三：简单扁平化排序（不推荐）

```python
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        直接扁平化并排序
        
        注意：虽然简单易懂，但时间复杂度O(n²logn)
        不符合题目要求的"内存优于O(n²)"
        """
        # 扁平化
        flat = []
        for row in matrix:
            flat.extend(row)
        
        # 排序后取第k个
        flat.sort()
        return flat[k - 1]
        
        # 一行解法
        # return sorted(sum(matrix, []))[k - 1]
        # return nsmallest(k, sum(matrix, []))[-1]
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n² log n²) |
| 空间复杂度 | O(n²) |

---

## 算法对比

| 方法 | 时间复杂度 | 空间复杂度 | 优势 |
|------|-----------|-----------|------|
| 二分+两指针 | O(n log(max-min)) | O(1) | **最优，满足题目要求** |
| 最小堆 | O(k log k) | O(k) | k较小时较快 |
| 扁平排序 | O(n² log n²) | O(n²) | 代码简单但不满足要求 |

---

## 相关题目

- [373. Find K Pairs with Smallest Sums](373_find_k_pairs_with_smallest_sums.md) - 找最小和的k对数字
- [295. Find Median from Data Stream](295_find_median_from_data_stream.md) - 数据流的中位数
- [4. Median of Two Sorted Arrays](004-median_of_two_sorted_arrays.md) - 两个有序数组的中位数
