# 3Sum Closest

[2points]]

## Problem Description

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

Return *the sum of the three integers*.

You may assume that each input would have exactly one solution.

## Examples

**Example 1:**

```text
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

**Example 2:**

```text
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
```

## Constraints

- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`

## 解法一：双指针法（最优解）

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')
        
        for i in range(n - 2):
            # 跳过重复元素，虽然题目保证唯一解，但可以优化性能
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, n - 1
            
            while left < right:
                closest = nums[i] + nums[left] + nums[right]
                
                # 如果找到完全匹配，直接返回
                if closest == target:
                    return target
                
                # 更新最接近的和
                if abs(closest - target) < abs(closest - target):
                    closest = closest
                
                # 移动指针
                if closest < target:
                    left += 1
                else:
                    right -= 1
        
        return closest
```

**核心思想：**

- 固定第一个数，用双指针寻找另外两个数
- 维护当前最接近target的和
- 根据当前和与target的关系移动指针

**时间复杂度：** O(n²) - 外层循环O(n)，内层双指针O(n)
**空间复杂度：** O(1) - 只使用常量额外空间

## 解法二：优化的双指针法

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = sum(nums[:3])  # 初始化为前三个数的和
        
        for i in range(n - 2):
            # 跳过重复元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, n - 1
            
            # 边界情况优化：最小可能和
            min_sum = nums[i] + nums[left] + nums[left + 1]
            if min_sum >= target:
                if abs(min_sum - target) < abs(result - target):
                    result = min_sum
                continue
            
            # 边界情况优化：最大可能和
            max_sum = nums[i] + nums[right - 1] + nums[right]
            if max_sum <= target:
                if abs(max_sum - target) < abs(result - target):
                    result = max_sum
                continue
            
            # 双指针搜索
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return target
                
                if abs(current_sum - target) < abs(result - target):
                    result = current_sum
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result
```

通过预先计算边界情况，可以提前跳过一些不必要的搜索，进一步优化性能。

## 解法三：暴力法（参考）


## 算法分析

### 与3Sum的区别

| 方面 | 3Sum | 3Sum Closest |
|------|------|--------------|
| **目标** | 找和为0的三元组 | 找和最接近target的三元组 |
| **去重** | 需要避免重复解 | 题目保证唯一解 |
| **返回值** | 所有符合条件的三元组 | 最接近的和 |
| **优化** | 跳过重复元素 | 边界情况剪枝 |

### 算法优化技巧

1. **排序预处理**：使双指针法成为可能
2. **重复元素跳过**：虽然题目保证唯一解，但可以提升性能
3. **边界情况判断**：预先计算最小/最大可能和
4. **早期退出**：找到完全匹配时立即返回

## 复杂度对比

| 方法 | 时间复杂度 | 空间复杂度 | 优缺点 |
|------|------------|------------|--------|
| 双指针法 | O(n²) | O(1) | ✅ 最优解 |
| 优化双指针 | O(n²) | O(1) | 实际运行更快 |


## 相关题目

- [15. 3Sum](015_3sum.md) - 三数之和
- [18. 4Sum](018_4sum.md) - 四数之和
- [1. Two Sum](001_two_sum.md) - 两数之和
