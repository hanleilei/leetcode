# Squares of a Sorted Array

[[array]] [[two-pointers]]

## Problem Description

Given an integer array `nums` sorted in **non-decreasing order**, return *an array of **the squares of each number** sorted in non-decreasing order*.

## Examples

**Example 1:**

```text
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

**Example 2:**

```text
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in **non-decreasing order**.

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

## 解法一：双指针法（最优解）

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        
        # 从后往前填充结果数组
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
        
        return result
```

**核心思想：**

- 由于数组已排序，最大的平方值一定出现在两端（最大正数或最小负数）
- 使用双指针从两端向中间收缩，每次选择绝对值较大的数字
- 从结果数组的末尾开始填充，确保大的平方值放在后面

**时间复杂度：** O(n) - 一次遍历
**空间复杂度：** O(n) - 结果数组空间

## 解法二：分割点优化

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 找到正负数分界点
        n = len(nums)
        negative_end = -1
        
        for i in range(n):
            if nums[i] < 0:
                negative_end = i
            else:
                break
        
        result = []
        positive_start = negative_end + 1
        
        # 合并两个部分的平方值
        while negative_end >= 0 and positive_start < n:
            neg_square = nums[negative_end] * nums[negative_end]
            pos_square = nums[positive_start] * nums[positive_start]
            
            if neg_square <= pos_square:
                result.append(neg_square)
                negative_end -= 1
            else:
                result.append(pos_square)
                positive_start += 1
        
        # 处理剩余元素
        while negative_end >= 0:
            result.append(nums[negative_end] * nums[negative_end])
            negative_end -= 1
        
        while positive_start < n:
            result.append(nums[positive_start] * nums[positive_start])
            positive_start += 1
        
        return result
```

先找到正负数分界点，然后类似归并排序的方式合并两部分。

## 算法分析

### 为什么双指针法最优？

```text
数组: [-4, -1, 0, 3, 10]
平方: [16,  1, 0, 9, 100]
              ↑
            最小值

关键观察：
- 最大平方值一定在两端
- 最小平方值可能在中间（0附近）
- 从大到小填充可以避免复杂的判断
```

### 复杂度对比

| 方法 | 时间复杂度 | 空间复杂度 | 优缺点 |
|------|------------|------------|--------|
| 双指针法 | O(n) | O(n) | ✅ 最优解 |
| 分割点法 | O(n) | O(n) | 逻辑复杂 |

## 相关题目

- [167. Two Sum II - Input Array Is Sorted](167_two_sum_ii_input_array_is_sorted.md) - 两数之和 II
- [88. Merge Sorted Array](088_merge_sorted_array.md) - 合并两个有序数组
- [283. Move Zeroes](283_move_zeroes.md) - 移动零

