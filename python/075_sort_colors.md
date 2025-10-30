# Sort Colors

[[array]]

## Problem Description

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem **without using the library's sort function**.

## Examples

**Example 1:**

```text
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Example 2:**

```text
Input: nums = [2,0,1]
Output: [0,1,2]
```

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

**Follow up:** Could you come up with a one-pass algorithm using only constant extra space?

## 解法一：三路快排（荷兰国旗问题）

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0
        
        while i <= right:
            if nums[i] == 0:
                # 将0换到左边，两个指针都前进
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                # 将2换到右边，i不动(因为换来的元素还未检查)
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                # 注意：i不增加
            else:  # nums[i] == 1
                # 1已经在正确位置，继续
                i += 1
```

**核心思想：**

这是经典的荷兰国旗问题，使用三个指针：

- `left`: 指向下一个0应该放置的位置
- `right`: 指向下一个2应该放置的位置  
- `i`: 当前检查的元素位置

**关键要点：**

- 遇到0：与left位置交换，两指针都前进
- 遇到2：与right位置交换，i不动（换来的元素需要重新检查）
- 遇到1：直接前进

**时间复杂度：** O(n) - 一次遍历
**空间复杂度：** O(1) - 原地排序

## 解法二：计数排序

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        from collections import Counter
        c = Counter(nums)
        nums[:] = [0] * c[0] + [1] * c[1] + [2] * c[2]
```

使用计数器统计各颜色数量，然后重新构造数组。简洁但需要两次遍历。

## 解法三：原地重写技巧

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i0 = i1 = i2 = -1
        for val in nums:
            nums[i2 := i2 + 1] = 2
            if val < 2:
                nums[i1 := i1 + 1] = 1
                if val < 1:
                    nums[i0 := i0 + 1] = 0
```

巧妙的原地重写方法，从右到左依次放置2、1、0。

## 算法可视化

```text
目标状态：[0, 0, ..., 1, 1, ..., 2, 2]
          ↑        ↑           ↑
        left       i         right

不变式：
- [0, left) 都是0
- [left, i) 都是1  
- (right, len-1] 都是2
- [i, right] 是待处理区域
```

## 相关题目

- [215. Kth Largest Element in an Array](215_kth_largest_element_in_an_array.md) - 数组中的第K个最大元素
- [324. Wiggle Sort II](324_wiggle_sort_ii.md) - 摆动排序 II

