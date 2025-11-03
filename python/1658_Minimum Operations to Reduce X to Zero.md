
# Minimum Operations to Reduce X to Zero

[[slidingWindow]] [[prefixSum]]

## Problem Description

You are given an integer array `nums` and an integer `x`. In one operation, you can either remove the leftmost or the rightmost element from the array `nums` and subtract its value from `x`. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce `x` to exactly 0 if it is possible, otherwise, return -1.

## Examples

**Example 1:**

```text
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: Remove the last two elements to reduce x to zero.
```

**Example 2:**

```text
Input: nums = [5,6,7,8,9], x = 4
Output: -1
```

**Example 3:**

```text
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: Remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`
- `1 <= x <= 10^9`

---

## 解法一：滑动窗口（最优解）

**核心思想：**
将问题转化为：在数组中找一个最长的连续子数组，其和为 `sum(nums) - x`，剩下的元素就是不被移除的部分。

```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        if total < x:
            return -1
        target = total - x
        n = len(nums)
        
        # 特殊情况：如果 target 为 0，说明需要移除整个数组
        if target == 0:
            return n
        
        left = 0
        window_sum = 0
        max_len = -1  # 记录和为 target 的最长子数组长度
        
        for right in range(n):
            window_sum += nums[right]  # 扩张右边界
            # 当窗口和超过 target 时，收缩左边界
            while window_sum > target and left <= right:
                window_sum -= nums[left]
                left += 1
            # 检查是否找到目标子数组
            if window_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return n - max_len if max_len != -1 else -1
```

**时间复杂度：** O(n)
**空间复杂度：** O(1)

---

## 解法二：前缀和+哈希表

```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        prefix = {0: -1}
        curr_sum = 0
        max_len = -1
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum - target in prefix:
                max_len = max(max_len, i - prefix[curr_sum - target])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return len(nums) - max_len if max_len != -1 else -1
```

**思路说明：**

- 用哈希表记录前缀和第一次出现的位置
- 检查当前前缀和与target的差是否出现过

**时间复杂度：** O(n)
**空间复杂度：** O(n)

---

## 解法三：双指针（不推荐）

主要问题:

1. 前缀和数组的构造有点冗余
2. 双指针滑动窗口实现不够简洁
    其实可以直接用滑动窗口，不需要构造前缀和数组
    只需维护一个窗口的和，窗口右端不断扩展，左端根据情况收缩
3. 变量命名和边界处理略显复杂

```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        if total < x:return -1
        pre_sum = [0] * (len(nums) + 1)
        pre_sum[0] = 0
        for i in range(1, len(pre_sum)):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        left, right = 0, 1
        res = float("-inf")
        while right < len(pre_sum):
            # right += 1
            if pre_sum[right] - pre_sum[left] == total - x:
                res = max(res, right - left)
                left += 1
                right += 1
            elif pre_sum[right] - pre_sum[left] < total - x:
                right += 1
            else:
                left += 1
        return len(nums) - res if res != float("-inf") else -1
```

**时间复杂度：** O(n^2)
**空间复杂度：** O(1)

---

## 算法分析

### 为什么可以转化为滑动窗口？

每次只能从两端移除元素，等价于保留一段连续的中间子数组，其和为 `sum(nums) - x`。

### 复杂度对比

| 方法 | 时间复杂度 | 空间复杂度 | 优缺点 |
|------|------------|------------|--------|
| 滑动窗口 | O(n) | O(1) | ✅ 最优解 |
| 前缀和哈希 | O(n) | O(n) | 代码简洁 |

---

## 相关题目

- [560. Subarray Sum Equals K](560_subarray_sum_equals_k.md) - 和为K的子数组
- [325. Maximum Size Subarray Sum Equals k](325_maximum_size_subarray_sum_equals_k.md) - 和为k的最大子数组
- [1248. Count Number of Nice Subarrays](1248_count_number_of_nice_subarrays.md) - 统计优美子数组
