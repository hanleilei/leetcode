# 2154. Keep Multiplying Found Values by Two

## 问题描述

You are given an array of integers `nums`. You are also given an
integer `original` which is the first number that needs to be
searched for in `nums`.

You then do the following steps:

1. If `original` is found in `nums`, multiply it by two
   (i.e., set `original = 2 * original`).
2. Otherwise, stop the process.
3. Repeat this process with the new number as long as you keep
   finding the number.

Return the final value of `original`.

## 示例

**Example 1:**

```text
Input: nums = [5,3,6,1,12], original = 3
Output: 24

Explanation:
- 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.
```

**Example 2:**

```text
Input: nums = [2,7,9], original = 4
Output: 4

Explanation:
- 4 is not found in nums. Thus, 4 is returned.
```

## 约束条件

- 1 <= nums.length <= 1000
- 1 <= nums[i], original <= 1000

## 解法

### 方法1：哈希集合（推荐）

核心思想：使用集合存储所有数字，不断查找并翻倍。

```python
from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        
        while original in num_set:
            original *= 2
        
        return original
```

### 方法2：数组标记法

利用数值范围小的特点，使用数组标记存在性。

```python
from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # 创建标记数组，范围是[0, 1000]
        exists = [False] * 1001
        for num in nums:
            exists[num] = True
        
        # 不断翻倍直到不存在或超出范围
        while original <= 1000 and exists[original]:
            original *= 2
        
        return original
```

### 方法3：排序后遍历

先排序，然后依次检查。

```python
from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        
        for num in nums:
            if num == original:
                original *= 2
        
        return original
```

### 方法4：位运算优化（数学方法）

利用位运算特性，找出最大的倍数。

```python
from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        
        # 找出original能翻倍到的最大值
        # 每次翻倍相当于左移1位
        while original in num_set and original <= 1000:
            original <<= 1  # 等价于 original *= 2
        
        return original
```

## 算法分析

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 哈希集合 | O(n + log k) | O(n) | k是最终值，log k是翻倍次数 |
| 数组标记 | O(n + log k) | O(1) | 固定1001大小的数组 |
| 排序 | O(n log n) | O(1) | 排序开销大 |
| 位运算 | O(n + log k) | O(n) | 与方法1等价 |

其中 n 是数组长度，k 是最终结果。

翻倍次数分析：

由于 original <= 1000，最多翻倍约10次（$2^{10} = 1024$）就会超出范围。
所以循环次数是 O(log k)，实际不超过10次。

### 执行过程示例

以 nums = [5,3,6,1,12], original = 3 为例。

方法1：哈希集合

```text
num_set = {1, 3, 5, 6, 12}

Step 1: original = 3
  3 in num_set? Yes
  original = 3 * 2 = 6

Step 2: original = 6
  6 in num_set? Yes
  original = 6 * 2 = 12

Step 3: original = 12
  12 in num_set? Yes
  original = 12 * 2 = 24

Step 4: original = 24
  24 in num_set? No
  返回 24
```

方法2：数组标记

```text
exists[1] = True
exists[3] = True
exists[5] = True
exists[6] = True
exists[12] = True

original = 3:
  exists[3] = True, original = 6
original = 6:
  exists[6] = True, original = 12
original = 12:
  exists[12] = True, original = 24
original = 24:
  exists[24] = False (未标记)
  返回 24
```

方法3：排序

```text
nums.sort() = [1, 3, 5, 6, 12]
original = 3

遍历：
- num = 1: 1 != 3, 跳过
- num = 3: 3 == 3, original = 6
- num = 5: 5 != 6, 跳过
- num = 6: 6 == 6, original = 12
- num = 12: 12 == 12, original = 24

返回 24
```

## 常见错误

### 错误1：忘记边界检查

```python
# 错误：可能无限循环或数组越界
while exists[original]:  # 当original > 1000时越界
    original *= 2
```

**问题：** original可能翻倍超过1000，导致数组越界。

正确做法：

```python
while original <= 1000 and exists[original]:
    original *= 2
```

### 错误2：使用列表而非集合

```python
# 错误：每次查找都是O(n)
while original in nums:  # 列表查找O(n)
    original *= 2
```

**问题：** 列表的in操作是O(n)，总复杂度变成O(n * log k)。

正确做法：使用set，查找O(1)。

### 错误3：排序后修改original但继续用旧值比较

```python
# 错误：逻辑混乱
for i, num in enumerate(nums):
    if num == original:
        original *= 2
        nums[i] = original  # 修改数组无意义
```

**问题：** 题目要求找到就翻倍，不需要修改原数组。

### 错误4：重复元素处理错误

```python
# 错误：重复处理同一个值
nums = [3, 3, 6]
original = 3

for num in nums:
    if num == original:
        original *= 2  # 会执行两次，变成12而非6
```

**问题：** 遇到重复的3会翻倍两次。

正确理解：题目是"找到后翻倍，再找新值"，不是"遇到就翻倍"。
方法1的集合法天然避免了这个问题。

## 优化技巧

### 技巧1：提前终止

```python
def findFinalValue(self, nums: List[int], original: int) -> int:
    num_set = set(nums)
    max_num = max(nums)
    
    # 如果original已经大于最大值，直接返回
    while original <= max_num and original in num_set:
        original *= 2
    
    return original
```

### 技巧2：位运算计数

```python
def findFinalValue(self, nums: List[int], original: int) -> int:
    num_set = set(nums)
    count = 0
    
    # 统计能翻倍多少次
    temp = original
    while temp in num_set and temp <= 1000:
        count += 1
        temp <<= 1
    
    # 一次性计算结果
    return original << count  # 等价于 original * (2 ** count)
```

### 技巧3：使用bisect优化排序方法

```python
import bisect

def findFinalValue(self, nums: List[int], original: int) -> int:
    nums.sort()
    
    while True:
        # 二分查找
        pos = bisect.bisect_left(nums, original)
        if pos < len(nums) and nums[pos] == original:
            original *= 2
        else:
            break
    
    return original
```

时间复杂度：O(n log n + log k * log n)

## 相关题目

- [0287. Find the Duplicate Number](./287_find_the_duplicate_number.md)
- [0268. Missing Number](./268_missing_number.md)
- [0136. Single Number](./136_single_number.md)
- [0349. Intersection of Two Arrays](./349_intersection_of_two_arrays.md)
- [1346. Check If N and Its Double Exist](./1346_check_if_n_and_its_double_exist.md)
