# 239. Sliding Window Maximum

## 问题描述

You are given an array of integers `nums`, there is a sliding window
of size `k` which is moving from the very left of the array to the
very right. You can only see the `k` numbers in the sliding window.
Each time the sliding window moves right by one position.

Return the max sliding window.

## 示例

**Example 1:**

```text
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

Explanation:

```text
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Example 2:**

```text
Input: nums = [1], k = 1
Output: [1]
```

## 约束条件

- $1 \le \text{nums.length} \le 10^5$
- $-10^4 \le \text{nums}[i] \le 10^4$
- $1 \le k \le \text{nums.length}$

## 解法

### 方法1：单调双端队列 推荐

维护一个单调递减的双端队列，队列中存储数组索引，使得队首始终
是当前窗口的最大值索引。

```python
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        单调双端队列

        时间复杂度：O(n)
        空间复杂度：O(k)
        """
        # 初始化结果数组
        res = [0] * (len(nums) - k + 1)

        # 双端队列存储索引（不是值）
        q = deque()

        for i, x in enumerate(nums):
            # 维护单调性：移除队尾所有小于等于当前元素的索引
            while q and nums[q[-1]] <= x:
                q.pop()

            # 当前索引入队
            q.append(i)

            # 计算当前窗口的左边界
            left = i - k + 1

            # 移除窗口外的元素（队首元素过期）
            if q[0] < left:
                q.popleft()

            # 当窗口形成时，记录最大值
            if left >= 0:
                res[left] = nums[q[0]]

        return res
```

### 方法2：简洁版单调队列

Stefan Pochmann 的简洁实现。

```python
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        简洁版单调队列

        时间复杂度：O(n)
        空间复杂度：O(k)
        """
        d = deque()
        out = []

        for i, n in enumerate(nums):
            # 移除队尾较小元素
            while d and nums[d[-1]] < n:
                d.pop()

            # 当前索引入队
            d.append(i)

            # 移除窗口外元素
            if d[0] == i - k:
                d.popleft()

            # 窗口形成后记录最大值
            if i >= k - 1:
                out.append(nums[d[0]])

        return out
```

### 方法3：分阶段处理

先处理前 k 个元素形成初始窗口，再滑动窗口。

```python
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        分阶段处理

        时间复杂度：O(n)
        空间复杂度：O(k)
        """
        if not nums or k == 0:
            return []

        deq = deque()
        result = []

        # 第一阶段：处理前 k 个元素
        for i in range(k):
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)

        # 第二阶段：滑动窗口
        for i in range(k, len(nums)):
            result.append(nums[deq[0]])

            # 移除窗口外元素
            if deq[0] < i - k + 1:
                deq.popleft()

            # 维护单调性
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

            deq.append(i)

        # 添加最后一个窗口的最大值
        result.append(nums[deq[0]])

        return result
```

## 算法分析

### 核心思想详解

单调双端队列的三大核心操作：

**维护单调性**：移除队尾所有小于等于当前元素的索引

当新元素更大时，队尾较小元素永远不可能成为最大值（因为新元素
更晚进入且更大），可以直接丢弃。

```python
while q and nums[q[-1]] <= x:
    q.pop()
```

**移除过期元素**：检查队首是否在窗口内

```python
left = i - k + 1  # 窗口左边界
if q[0] < left:   # 队首过期
    q.popleft()
```

**查询最大值**：队首就是当前窗口最大值

因为队列维护单调递减序列，队首对应的值最大。

```python
res[left] = nums[q[0]]
```

### 为什么队列存储索引而不是值？

因为需要判断元素是否过期（是否还在窗口内）：

- 存储索引：可以通过 `q[0] < left` 判断是否过期
- 存储值：无法判断该值对应的位置

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 单调队列 | O(n) | O(k) | 最优解 |
| 简洁版 | O(n) | O(k) | 代码更短 |
| 分阶段 | O(n) | O(k) | 逻辑清晰 |

时间复杂度为 O(n) 的原因：虽然有 while 循环，但每个元素最多
入队和出队各一次，总操作数为 2n，均摊 O(1)。

### 执行过程示例

以 `nums = [1,3,-1,-3,5,3,6,7], k = 3` 为例：

| i | x | 操作 | 队列q | 队列值 | left | res |
|---|---|------|-------|--------|------|-----|
| 0 | 1 | 入队 | [0] | [1] | -2 | - |
| 1 | 3 | 3>1,弹0,入1 | [1] | [3] | -1 | - |
| 2 | -1 | -1<3,入2 | [1,2] | [3,-1] | 0 | [3] |
| 3 | -3 | -3<-1,入3 | [1,2,3] | [3,-1,-3] | 1 | [3,3] |
| 4 | 5 | 5>all,清空,入4 | [4] | [5] | 2 | [3,3,5] |
| 5 | 3 | 3<5,入5 | [4,5] | [5,3] | 3 | [3,3,5,5] |
| 6 | 6 | 6>all,清空,入6 | [6] | [6] | 4 | [3,3,5,5,6] |
| 7 | 7 | 7>6,弹6,入7 | [7] | [7] | 5 | [3,3,5,5,6,7] |

关键步骤：

Step 4：当 `x=5` 时，5 大于队列中所有值（3, -1, -3），全部弹出，
队列变为 `[4]`（只有索引4）。

Step 6：当 `x=6` 时，6 大于队列中所有值（5, 3），全部弹出。

## 常见错误

### 错误1：队列存储值而不是索引

```python
# 错误：无法判断是否过期
q.append(x)

# 正确：用索引判断
q.append(i)
if q[0] < left:  # 检查是否在窗口内
    q.popleft()
```

### 错误2：判断条件用 `<` 而不是 `<=`

```python
# 错误：相等的值也要移除
while q and nums[q[-1]] < x:
    q.pop()

# 正确：保证严格单调递减
while q and nums[q[-1]] <= x:
    q.pop()
```

### 错误3：忘记移除过期元素

```python
# 错误：没有检查队首是否过期
res[left] = nums[q[0]]

# 正确：先移除过期
if q[0] < left:
    q.popleft()
res[left] = nums[q[0]]
```

### 错误4：窗口未形成就记录答案

```python
# 错误：left 可能是负数
res[left] = nums[q[0]]

# 正确：检查窗口是否形成
if left >= 0:
    res[left] = nums[q[0]]
```

### 错误5：误用 max() 函数（超时）

```python
# 错误：暴力法 O(nk) 超时
for i in range(len(nums) - k + 1):
    res.append(max(nums[i:i+k]))

# 正确：单调队列 O(n)
```

## 相关题目

- [0239. Sliding Window Maximum](./239_sliding_window_maximum.md)
- [0862. Shortest Subarray with Sum at Least K](./862_shortest_subarray_with_sum_at_least_k.md) - 单调队列求最小值
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](./1438_longest_continuous_subarray.md) - 双单调队列
- [1696. Jump Game VI](./1696_jump_game_vi.md) - 单调队列DP优化
- [0739. Daily Temperatures](./739_daily_temperatures.md)
- [1499. Max Value of Equation](./1499_max_value_of_equation.md) - 单调队列维护最优解

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]]
        return out
```

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        window, res = deque(), []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.popleft()
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
```
