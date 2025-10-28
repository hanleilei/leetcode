# Longest Consecutive Sequence

[[hashtable]] [[array]]

## Problem Description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

## Examples

**Example 1:**

```text
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

**Example 2:**

```text
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## 解法一：哈希集合（最优解）

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        使用哈希集合找最长连续序列
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        s = set(nums)
        res = 0
        # 将遍历对象从 nums 改为去重后的 s
        for i in s: 
            if i - 1 not in s:
                y = i + 1
                while y in s:
                    y += 1
                res = max(res, y - i)
        return res
```

### 算法思路

1. **集合转换**：将数组转换为哈希集合，实现O(1)的查找时间
2. **序列起点识别**：只有当`num-1`不在集合中时，`num`才是序列的起点
3. **长度计算**：从起点开始，连续查找`num+1, num+2, ...`直到不存在
4. **结果更新**：记录找到的最长序列长度

### 关键优化

**避免重复计算**：只从序列的起点开始计算，避免从序列中间开始重复计算。

例如对于序列[1,2,3,4]：

- 当遍历到1时，发现0不在集合中，所以1是起点，计算长度4
- 当遍历到2时，发现1在集合中，所以2不是起点，跳过
- 当遍历到3时，发现2在集合中，所以3不是起点，跳过
- 当遍历到4时，发现3在集合中，所以4不是起点，跳过

**复杂度分析**：

- 时间复杂度：O(n) - 虽然有嵌套循环，但每个数字最多被访问2次
- 空间复杂度：O(n) - 需要额外的哈希集合存储所有数字

## 解法二：排序后遍历

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        先排序再遍历找连续序列
        时间复杂度：O(n log n)，空间复杂度：O(1)
        """
        if not nums:
            return 0
        
        nums.sort()
        max_length = 1
        current_length = 1
        
        for i in range(1, len(nums)):
            # 跳过重复元素
            if nums[i] == nums[i-1]:
                continue
            # 连续序列
            elif nums[i] == nums[i-1] + 1:
                current_length += 1
            # 序列断开，重新开始
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        
        return max(max_length, current_length)
```

**复杂度分析**：

- 时间复杂度：O(n log n) - 主要是排序的时间复杂度
- 空间复杂度：O(1) - 只使用常数额外空间

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 哈希集合 | O(n) | O(n) | 最优时间复杂度，推荐 |
| 排序后遍历 | O(n log n) | O(1) | 空间效率高，但时间较慢 |

## 边界情况处理

1. **空数组**：直接返回0
2. **单个元素**：返回1
3. **重复元素**：需要去重处理
4. **负数**：算法同样适用

## 关键要点

1. **哈希集合的妙用**：O(1)查找时间是解决此题的关键
2. **序列起点识别**：避免重复计算的核心优化
3. **边界处理**：空数组和重复元素的特殊情况
4. **时间复杂度分析**：理解为什么嵌套循环仍是O(n)

## 常见错误

1. **重复计算**：从每个数字开始都尝试构建序列
2. **忽略重复元素**：没有正确处理数组中的重复数字
3. **边界遗漏**：空数组和单元素数组的特殊情况
4. **复杂度误解**：错误理解嵌套循环的实际时间复杂度

## 相关题目

- [217. Contains Duplicate](217_contains_duplicate.md) - 存在重复元素
- [41. First Missing Positive](041_first_missing_positive.md) - 缺失的第一个正数
- [442. Find All Duplicates in an Array](442_find_all_duplicates_in_array.md) - 数组中重复的数据

这道题是哈希表应用的经典题目，展示了如何用空间换时间来优化算法效率。
