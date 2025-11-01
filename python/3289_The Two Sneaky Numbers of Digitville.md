# The Two Sneaky Numbers of Digitville

[[array]] [[hash-table]]

## Problem Description

In the town of Digitville, there was a list of numbers called `nums` containing integers from `0` to `n - 1`. Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.

## Examples

**Example 1:**

```text
Input: nums = [0,1,1,0]
Output: [0,1]
Explanation: The numbers 0 and 1 each appear twice in the array.
```

**Example 2:**

```text
Input: nums = [0,3,2,1,3,2]
Output: [2,3]
Explanation: The numbers 2 and 3 each appear twice in the array.
```

**Example 3:**

```text
Input: nums = [7,1,5,4,3,4,6,0,9,5,8,2]
Output: [4,5]
Explanation: The numbers 4 and 5 each appear twice in the array.
```

## Constraints

- `2 <= n <= 100`
- `nums.length == n + 2`
- `0 <= nums[i] < n`
- The input is generated such that `nums` contains exactly two repeated elements.

## 解法一：哈希集合（最优解）

```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []
        
        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)
        
        return result
```

**核心思想：**

- 使用哈希集合记录已见过的数字
- 第一次遇到某数字时加入集合，第二次遇到时加入结果
- 由于题目保证只有两个重复数字，找到两个即可返回

**时间复杂度：** O(n)
**空间复杂度：** O(n)

## 解法二：计数器法

```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        return [num for num, freq in count.items() if freq == 2]
```

使用Counter统计频次，然后筛选出现2次的数字。

## 解法三：数组标记法

```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2  # 原本应该有n个不同数字
        count = [0] * n
        result = []
        
        for num in nums:
            count[num] += 1
            if count[num] == 2:
                result.append(num)
        
        return result
```

利用数字范围有限的特点，使用数组代替哈希表进行计数。

## 解法四：一行Python

```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        return [k for k, v in Counter(nums).items() if v > 1]
```

最简洁的Python写法。

## 解法五：数学方法（位运算）

```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # 计算期望的总和（0到n-1）
        n = len(nums) - 2
        expected_sum = n * (n - 1) // 2
        actual_sum = sum(nums)
        
        # 两个重复数字的和
        duplicate_sum = actual_sum - expected_sum
        
        # 这种方法需要额外信息来分离两个数字
        # 实际应用中不如哈希表方法直接
        seen = set()
        result = []
        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)
        return result
```

## 算法分析

### 复杂度对比

| 方法 | 时间复杂度 | 空间复杂度 | 优缺点 |
|------|------------|------------|--------|
| 哈希集合 | O(n) | O(n) | ✅ 最直接高效 |
| 计数器 | O(n) | O(n) | 代码简洁 |
| 数组标记 | O(n) | O(n) | 空间常数较小 |
| 一行解法 | O(n) | O(n) | 极简代码 |

### 为什么哈希集合最优？

- **直接性**：一次遍历即可找到答案
- **效率**：平均O(1)的查找和插入时间
- **清晰性**：逻辑简单易懂
- **稳定性**：性能稳定，不依赖输入特征

## 相关题目

- [287. Find the Duplicate Number](287_find_the_duplicate_number.md) - 寻找重复数
- [442. Find All Duplicates in an Array](442_find_all_duplicates_in_an_array.md) - 数组中重复的数据
- [448. Find All Numbers Disappeared in an Array](448_find_all_nums_disappered_in_an_array.md) - 找到所有数组中消失的数字
