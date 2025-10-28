# Majority Element

[[array]] [[hashtable]] [[divide-and-conquer]] [[sorting]]

## Problem Description

Given an array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

## Examples

**Example 1:**

```text
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**

```text
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Constraints

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

## 解法一：摩尔投票法（最优解）

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        摩尔投票算法（Boyer-Moore Voting Algorithm）
        时间复杂度：O(n)，空间复杂度：O(1)
        """
        candidate = None
        count = 0
        
        # 第一阶段：找到候选者
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        # 由于题目保证存在众数，可以直接返回候选者
        # 如果不确定，需要第二阶段验证候选者是否真的是众数
        return candidate
```

### 算法思路

**摩尔投票法的核心思想**：

1. **对消思想**：不同的元素相互抵消，相同的元素累加
2. **候选者选择**：当计数为0时，选择当前元素作为新候选者
3. **计数更新**：遇到相同元素+1，不同元素-1
4. **最终结果**：由于众数占超过一半，最终剩下的必定是众数

### 算法图解

以数组 `[2,2,1,1,1,2,2]` 为例：

```text
数组: [2, 2, 1, 1, 1, 2, 2]
      ↓
candidate = 2, count = 1    (遇到2，候选者为2，计数+1)
      ↓
candidate = 2, count = 2    (遇到2，相同元素，计数+1)
      ↓
candidate = 2, count = 1    (遇到1，不同元素，计数-1)
      ↓
candidate = 2, count = 0    (遇到1，不同元素，计数-1)
      ↓
candidate = 1, count = 1    (计数为0，选择新候选者1)
      ↓
candidate = 1, count = 0    (遇到2，不同元素，计数-1)
      ↓
candidate = 2, count = 1    (计数为0，选择新候选者2)

最终返回: 2
```

**复杂度分析**：

- 时间复杂度：O(n) - 只需遍历数组一次
- 空间复杂度：O(1) - 只使用常数额外空间

## 解法二：排序取中位数

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        排序后取中位数
        时间复杂度：O(n log n)，空间复杂度：O(1)
        """
        nums.sort()
        return nums[len(nums) // 2]
```

### 核心思想

由于众数出现次数超过 `⌊n/2⌋`，排序后中位数位置必定是众数。

**复杂度分析**：

- 时间复杂度：O(n log n) - 排序的时间复杂度
- 空间复杂度：O(1) - 原地排序

## 解法三：哈希表计数

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        使用哈希表统计每个元素出现次数
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        from collections import Counter
        
        counter = Counter(nums)
        threshold = len(nums) // 2
        
        for num, count in counter.items():
            if count > threshold:
                return num
```

### 优化版本（提前返回）

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        哈希表计数，一旦发现众数立即返回
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        from collections import defaultdict
        
        count_map = defaultdict(int)
        threshold = len(nums) // 2
        
        for num in nums:
            count_map[num] += 1
            if count_map[num] > threshold:
                return num
```

**复杂度分析**：

- 时间复杂度：O(n) - 最坏情况遍历整个数组
- 空间复杂度：O(n) - 哈希表存储元素计数

## 解法四：分治法

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        分治算法
        时间复杂度：O(n log n)，空间复杂度：O(log n)
        """
        def majority_element_rec(left, right):
            # 基础情况
            if left == right:
                return nums[left]
            
            # 分治
            mid = (left + right) // 2
            left_majority = majority_element_rec(left, mid)
            right_majority = majority_element_rec(mid + 1, right)
            
            # 如果两边的众数相同，直接返回
            if left_majority == right_majority:
                return left_majority
            
            # 否则计算两个候选者在整个区间的出现次数
            left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_majority)
            right_count = sum(1 for i in range(left, right + 1) if nums[i] == right_majority)
            
            return left_majority if left_count > right_count else right_majority
        
        return majority_element_rec(0, len(nums) - 1)
```

**复杂度分析**：

- 时间复杂度：O(n log n) - 递归深度log n，每层需要O(n)时间
- 空间复杂度：O(log n) - 递归调用栈的深度

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 摩尔投票法 | O(n) | O(1) | 最优解，推荐 |
| 排序取中位数 | O(n log n) | O(1) | 简单直观 |
| 哈希表计数 | O(n) | O(n) | 容易理解 |
| 分治法 | O(n log n) | O(log n) | 体现分治思想 |

## 边界情况处理

1. **单个元素**：直接返回该元素
2. **全部相同**：任意元素都是众数
3. **刚好过半**：正确识别众数

## 关键要点

1. **摩尔投票法**：理解对消思想，是解决此类问题的经典算法
2. **中位数性质**：众数在排序数组中必定占据中位数位置
3. **提前返回**：在哈希表方法中，一旦发现众数可立即返回
4. **空间权衡**：根据具体需求选择时间和空间的平衡点

## 常见错误

1. **摩尔投票理解错误**：不理解为什么最后剩下的就是众数
2. **边界处理遗漏**：没有考虑单元素数组的情况
3. **阈值计算错误**：混淆"大于n/2"和"大于等于n/2"
4. **验证步骤缺失**：在不确定众数存在时，没有验证候选者

## 扩展思考

1. **如果众数不一定存在怎么办？** - 需要增加验证步骤
2. **如果要找出现次数前k多的元素？** - 可以使用堆或哈希表
3. **如果数组非常大，内存受限？** - 摩尔投票法是最佳选择

## 相关题目

- [229. Majority Element II](229_majority_element_II.md) - 求众数 II（寻找出现次数超过n/3的元素）
- [217. Contains Duplicate](217_contains_duplicate.md) - 存在重复元素
- [1207. Unique Number of Occurrences](1207_unique_number_of_occurrences.md) - 独一无二的出现次数

这道题是摩尔投票算法的经典应用，掌握这个算法对解决类似的"寻找特定频率元素"问题非常重要。
