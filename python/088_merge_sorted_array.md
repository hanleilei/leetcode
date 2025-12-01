# Merge Sorted Array

[[two-pointers]]

## Problem Description

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

## Examples

**Example 1:**

```text
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

**Example 2:**

```text
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```

**Example 3:**

```text
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```

## Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## 解法一：从后向前双指针（最优解）

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        while n > 0:
            if m > 0 and nums1[m-1] > nums2[n - 1]:
                nums1[index] = nums1[m - 1]
                m -= 1
            else:
                nums1[index] = nums2[n - 1]
                n -= 1
            index -= 1
```

**核心思想：**

- 从两个数组的末尾开始比较，将较大值放到nums1的末尾
- 由于nums1末尾有足够空间，避免了覆盖问题
- 只需要考虑nums2是否处理完，因为nums1剩余元素已经在正确位置

**为什么从后向前？**

- 避免覆盖nums1中未处理的元素
- 不需要额外空间存储nums1的副本

**时间复杂度：** O(m + n)
**空间复杂度：** O(1)

## 解法二：额外空间法

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 保存nums1的副本
        nums1_copy = nums1[:m]

        i = j = k = 0

        # 合并两个数组
        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        # 处理剩余元素
        while i < m:
            nums1[k] = nums1_copy[i]
            i += 1
            k += 1

        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
```

经典的归并排序思路，但需要额外空间存储nums1的副本。

## 解法三：Python内置方法

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
```

最简洁的写法，但时间复杂度为O((m+n)log(m+n))。

## 算法可视化

```text
从后向前合并过程：
nums1 = [1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3

步骤1: 比较3和6，6更大
nums1 = [1,2,3,0,0,6]
        ↑     ↑   ↑
        i     j   k

步骤2: 比较3和5，5更大  
nums1 = [1,2,3,0,5,6]
        ↑   ↑ ↑
        i   j k

步骤3: 比较3和2，3更大
nums1 = [1,2,3,3,5,6]
      ↑   ↑
      i   k

继续此过程...
最终: [1,2,2,3,5,6]
```

## 复杂度对比

| 方法 | 时间复杂度 | 空间复杂度 | 优缺点 |
|------|------------|------------|--------|
| 从后向前 | O(m+n) | O(1) | ✅ 最优解 |
| 额外空间 | O(m+n) | O(m) | 逻辑清晰 |
| 内置排序 | O((m+n)log(m+n)) | O(1) | 代码简洁 |

## 相关题目

- [21. Merge Two Sorted Lists](021_merge_two_sorted_lists.md) - 合并两个有序链表
- [977. Squares of a Sorted Array](977_square_of_a_sorted_array.md) - 有序数组的平方
- [4. Median of Two Sorted Arrays](004_median_of_two_sorted_arrays.md) - 寻找两个正序数组的中位数
