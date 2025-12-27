# 658. Find K Closest Elements

[[binarysearch]] [[2points]]

## 问题描述

Given a **sorted** integer array `arr`, two integers `k` and `x`, return
the `k` closest integers to `x` in the array. The result should also be
sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:
- `|a - x| < |b - x|`, or
- `|a - x| == |b - x|` and `a < b`

## 示例

**Example 1:**

```text
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
```

**Example 2:**

```text
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
```

**Example 3:**

```text
Input: arr = [1,1,2,2,2,2,2,3,3], k = 3, x = 3
Output: [2,3,3]
```

## 约束条件

- $1 \le k \le \text{arr.length}$
- $1 \le \text{arr.length} \le 10^4$
- `arr` is sorted in **ascending** order
- $-10^4 \le \text{arr}[i], x \le 10^4$

## 解法

### 方法1：二分查找窗口起点（推荐）

在 `[0, n-k]` 范围内二分查找长度为k的滑动窗口的最佳起始位置。

```python
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        二分查找窗口起点
        
        时间复杂度：O(log(n-k) + k)
        空间复杂度：O(1)
        """
        left, right = 0, len(arr) - k
        
        # 二分查找最佳窗口起点
        while left < right:
            mid = (left + right) // 2
            
            # 比较窗口两端与x的距离
            # 如果左端点距离更远，窗口应该右移
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left + k]
```

### 方法2：双指针收缩窗口

从两端向中间收缩，每次删除距离x较远的一端。

```python
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        双指针收缩窗口
        
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        left, right = 0, len(arr) - 1
        
        # 删除 n-k 个元素
        while right - left + 1 > k:
            # 比较两端距离，删除距离较远的一端
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1
        
        return arr[left:right + 1]
```

### 方法3：二分查找 + 双指针扩展

先二分找到最接近x的位置，然后双指针向两边扩展。

```python
from typing import List
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        二分查找 + 双指针扩展
        
        时间复杂度：O(log n + k)
        空间复杂度：O(1)
        """
        n = len(arr)
        
        # 二分查找插入位置（最接近x的位置）
        pos = bisect.bisect_left(arr, x)
        
        # 双指针初始化
        left, right = pos - 1, pos
        
        # 向两边扩展k个元素
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= n:
                left -= 1
            elif x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        
        return arr[left + 1:right]
```

### 方法4：排序法（不推荐）

自定义排序，按距离和值排序后取前k个。

```python
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        排序法
        
        时间复杂度：O(n log n)
        空间复杂度：O(n)
        """
        # 按距离和值排序
        sorted_arr = sorted(arr, key=lambda a: (abs(a - x), a))
        
        # 取前k个并排序
        return sorted(sorted_arr[:k])
```

## 算法分析

### 核心思想详解

**方法1：二分查找窗口起点**

关键思想：将问题转化为在 `[0, n-k]` 范围内寻找最佳窗口起点。

**判断条件解析**：

对于窗口 `[mid, mid+k-1]`，比较两端点与x的距离：

```text
左端距离：x - arr[mid]
右端后一个距离：arr[mid+k] - x

如果 x - arr[mid] > arr[mid+k] - x，说明：
- 左端点距离更远
- 窗口应该右移（删除左端点arr[mid]，加入arr[mid+k]）
- left = mid + 1
```

**为什么不能用绝对值？**

```python
# 错误：使用绝对值
if abs(x - arr[mid]) > abs(arr[mid+k] - x):
    ...

# 反例：arr = [1,1,2,2,2,2,2,3,3], x=3, k=2
# 期望输出：[2,3]（相等距离时选较小值）
# 绝对值会导致错误选择
```

**可视化示例**：

```text
arr = [1,2,3,4,5], k=4, x=3

初始：left=0, right=1
  窗口范围：[0, 1]

mid=0:
  比较 arr[0]=1 和 arr[4]=5 与x=3的距离
  3-1=2 > 5-3=2 ? 否
  right = 0

返回：arr[0:4] = [1,2,3,4]
```

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 二分窗口起点 | O(log(n-k) + k) | O(1) | 最优解 |
| 双指针收缩 | O(n) | O(1) | 简单直观 |
| 二分+扩展 | O(log n + k) | O(1) | 常数较大 |
| 排序法 | O(n log n) | O(n) | 不推荐 |

### 执行过程示例

以 `arr = [1,2,3,4,5]`, `k = 4`, `x = 3` 为例：

**方法1：二分查找窗口起点**

```text
初始状态：
  arr = [1,2,3,4,5]
  left = 0, right = 5 - 4 = 1
  目标：在 [0,1] 中找窗口起点

迭代1：
  mid = (0 + 1) // 2 = 0
  比较：x - arr[0] vs arr[4] - x
       3 - 1 = 2 vs 5 - 3 = 2
  2 > 2 ? 否
  right = 0

left = right = 0，退出循环

返回：arr[0:4] = [1,2,3,4]
```

**方法2：双指针收缩窗口**

```text
初始状态：
  left = 0, right = 4
  窗口大小 = 5，需要删除 5-4=1 个元素

比较两端：
  |arr[0] - x| = |1 - 3| = 2
  |arr[4] - x| = |5 - 3| = 2
  2 <= 2，删除右端
  right = 3

窗口大小 = 4，满足条件

返回：arr[0:4] = [1,2,3,4]
```

**可视化表格（方法1）**：

| 步骤 | left | right | mid | arr[mid] | arr[mid+k] | x-arr[mid] | arr[mid+k]-x | 操作 |
|------|------|-------|-----|----------|------------|------------|--------------|------|
| 初始 | 0 | 1 | - | - | - | - | - | - |
| 1 | 0 | 1 | 0 | 1 | 5 | 2 | 2 | right=0 |
| 结束 | 0 | 0 | - | - | - | - | - | - |

**边界情况处理**：

```text
情况1：x在数组左侧
arr = [1,2,3,4,5], k=4, x=-1
窗口会停留在最左侧 [0,3]
输出：[1,2,3,4]

情况2：x在数组右侧
arr = [1,2,3,4,5], k=4, x=10
窗口会停留在最右侧 [1,4]
输出：[2,3,4,5]

情况3：重复元素
arr = [1,1,2,2,2,2,2,3,3], k=3, x=3
距离相等时，优先选择较小值
输出：[2,3,3]
```

## 常见错误

### 错误1：使用绝对值比较

```python
# 错误：忽略了相等距离时选较小值的规则
if abs(x - arr[mid]) > abs(arr[mid+k] - x):
    left = mid + 1

# 正确：直接比较差值（不取绝对值）
if x - arr[mid] > arr[mid + k] - x:
    left = mid + 1
```

### 错误2：二分范围错误

```python
# 错误：right初始化为len(arr)
left, right = 0, len(arr)
# 会导致arr[mid+k]越界

# 正确：right为len(arr) - k
left, right = 0, len(arr) - k
```

### 错误3：双指针比较条件错误

```python
# 错误：距离相等时删除左端
if abs(arr[left] - x) < abs(arr[right] - x):
    right -= 1
else:
    left += 1

# 正确：距离相等时保留左端（删除右端）
if abs(arr[left] - x) <= abs(arr[right] - x):
    right -= 1
else:
    left += 1
```

### 错误4：扩展方向判断错误

```python
# 错误：比较条件反了
if x - arr[left] < arr[right] - x:
    left -= 1
else:
    right += 1

# 正确
if x - arr[left] <= arr[right] - x:
    left -= 1
else:
    right += 1
```

### 错误5：忘记处理边界

```python
# 错误：没有检查left和right越界
for _ in range(k):
    if x - arr[left] <= arr[right] - x:
        left -= 1
    else:
        right += 1

# 正确：先检查边界
for _ in range(k):
    if left < 0:
        right += 1
    elif right >= n:
        left -= 1
    elif x - arr[left] <= arr[right] - x:
        left -= 1
    else:
        right += 1
```

### 错误6：返回区间错误

```python
# 错误：双指针方法返回的right已经是最后一个元素
return arr[left:right]  # 会少一个元素

# 正确
return arr[left:right + 1]
```

## 相关题目

- [0034. Find First and Last Position of Element in Sorted Array](./034_search_for_range.md) - 二分查找边界
- [0744. Find Smallest Letter Greater Than Target](./744_find_smallest_letter_greater_than_target.md) - 二分查找
- [1337. The K Weakest Rows in a Matrix](./1337_The_K_Weakest_Rows_in_a_Matrix.md) - 找k个最小元素
- [0215. Kth Largest Element in an Array](./215_Kth_Largest_element_in_a_array.md) - 第k大元素
- [0373. Find K Pairs with Smallest Sums](./373_find_k_pairs_with_smallest_sums.md) - 找k对最小和
