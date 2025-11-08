# Subarray Product Less Than K

[[sliding window]] [[array]] [[2points]]

## Problem Description

Given an array of integers `nums` and an integer `k`, return the number of **contiguous subarrays** where the product of all the elements in the subarray is **strictly less than** `k`.

### Examples

**Example 1:**

```text
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```

**Example 2:**

```text
Input: nums = [1,2,3], k = 0
Output: 0
```

### Constraints

- `1 <= nums.length <= 3 * 10^4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10^6`

---

## 解法：滑动窗口（最优解）

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        left = 0
        prod = 1
        count = 0
        
        for right in range(len(nums)):
            # 扩大窗口，右指针右移
            prod *= nums[right]
            
            # 当乘积 >= k 时，收缩窗口，左指针右移
            while prod >= k:
                prod //= nums[left]
                left += 1
            
            # 以 right 结尾的满足条件的子数组个数
            # 即从 left 到 right 的所有子数组都满足条件
            count += right - left + 1
        
        return count
```

**核心思想：**

- 使用两个指针 left 和 right 维护一个滑动窗口
- 右指针扩大窗口，当乘积 >= k 时左指针收缩
- 对于每个右指针位置，满足条件的子数组个数为 `right - left + 1`

**时间复杂度：** O(n)（每个元素最多被访问两次）
**空间复杂度：** O(1)

---

## 算法分析

### 为什么用滑动窗口？

传统的暴力方法 O(n²) 会超时。滑动窗口利用了一个关键观察：

**如果 [left, right] 的乘积 < k，那么所有以 right 结尾、左端点 >= left 的子数组乘积都 < k。**

### 子数组计数解析

以 `[10, 5, 2, 6]，k = 100` 为例：

```text
right=0: window=[10], prod=10
         满足条件的子数组: [10]（1个）
         count = 0 - 0 + 1 = 1

right=1: window=[10,5], prod=50
         满足条件的子数组: [5], [10,5]（2个）
         count = 1 - 0 + 1 = 2

right=2: window=[10,5,2], prod=100
         prod >= k，需要收缩窗口
         移除 10: prod=10, left=1
         满足条件的子数组: [2], [5,2]（2个）
         count = 2 - 1 + 1 = 2

right=3: window=[5,2,6], prod=60
         满足条件的子数组: [6], [2,6], [5,2,6]（3个）
         count = 3 - 1 + 1 = 3

总计: 1 + 2 + 2 + 3 = 8
```

### 关键优化

1. **提前终止**：如果 k <= 1，直接返回 0（不可能有 product < k 的子数组）
2. **两指针移动**：虽然嵌套了 while 循环，但 left 指针整个算法只移动 n 次，总复杂度仍为 O(n)

---

## 相关题目

- [209. Minimum Size Subarray Sum](209_minimum_size_subarray_sum.md) - 最小子数组和
- [567. Permutation in String](567_permutation_in_string.md) - 字符串排列
- [76. Minimum Window Substring](076_minimum_windows_substring.md) - 最小窗口子串
