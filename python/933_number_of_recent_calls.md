# Number of Recent Calls

[[queue]] [[design]]

## Problem Description

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

- `RecentCounter()` Initializes the counter with zero recent requests.
- `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that has happened in the past `3000` milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is **guaranteed** that every call to `ping` uses a strictly larger value of `t` than the previous call.

## Examples

**Example 1:**

```text
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
```

## Constraints

- `1 <= t <= 10^9`
- Each test case will have at most `10^4` calls to `ping`.
- Each test case will call `ping` with strictly increasing values of `t`.

## 解法一：队列滑动窗口（推荐）

```python
from collections import deque

class RecentCounter:
    def __init__(self):
        """
        使用双端队列维护滑动窗口
        队列中存储所有请求的时间戳
        """
        self.requests = deque()

    def ping(self, t: int) -> int:
        """
        添加新请求并返回3000ms内的请求数量
        时间复杂度：O(1) 摊还，O(k) 最坏情况（k为需要移除的过期请求数）
        """
        # 添加当前请求时间
        self.requests.append(t)
        
        # 移除超出3000ms窗口的请求
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        # 返回当前窗口内的请求数量
        return len(self.requests)
```

**复杂度分析**：

- 时间复杂度：O(1) 摊还 - 每个元素最多被添加和删除一次
- 空间复杂度：O(W) - W为窗口大小，最多存储3000ms内的请求

## 解法二：列表模拟（不推荐）

```python
class RecentCounter:
    def __init__(self):
        """
        使用列表存储请求时间
        注意：效率较低，仅作对比
        """
        self.requests = []

    def ping(self, t: int) -> int:
        """
        使用列表实现，需要遍历移除过期请求
        时间复杂度：O(n) - 可能需要移除前面的多个元素
        """
        # 添加当前请求
        self.requests.append(t)
        
        # 移除过期请求（效率较低）
        self.requests = [time for time in self.requests if time >= t - 3000]
        
        return len(self.requests)
```

**复杂度分析**：

- 时间复杂度：O(n) - 每次需要重新创建列表
- 空间复杂度：O(W) - 存储窗口内的请求

## 解法三：二分查找优化（了解即可）

```python
import bisect

class RecentCounter:
    def __init__(self):
        """
        使用有序列表 + 二分查找
        """
        self.requests = []

    def ping(self, t: int) -> int:
        """
        利用时间戳单调递增的特性，使用二分查找
        时间复杂度：O(log n)
        """
        # 添加当前请求（保持有序）
        self.requests.append(t)
        
        # 使用二分查找找到t-3000的位置
        left_bound = t - 3000
        left_index = bisect.bisect_left(self.requests, left_bound)
        
        # 计算窗口内的请求数量
        return len(self.requests) - left_index
```

**复杂度分析**：

- 时间复杂度：O(log n) - 二分查找的时间复杂度
- 空间复杂度：O(n) - 存储所有历史请求

## 算法详解

### 核心思路

1. **滑动窗口**：维护一个大小为3000ms的时间窗口
2. **队列特性**：利用FIFO特性，过期请求总是在队列前端
3. **单调性**：由于时间戳严格递增，可以确保窗口的正确维护

### 算法流程

1. **添加请求**：将新的时间戳加入队列尾部
2. **清理过期**：从队列头部移除所有过期的请求
3. **统计数量**：返回队列当前长度

### 算法可视化

以示例为例，展示队列状态变化：

```text
初始状态: requests = []

1. ping(1):
   添加: requests = [1]
   窗口: [1-3000, 1] = [-2999, 1]
   清理: 无需清理
   返回: 1

2. ping(100):
   添加: requests = [1, 100]
   窗口: [100-3000, 100] = [-2900, 100]
   清理: 无需清理
   返回: 2

3. ping(3001):
   添加: requests = [1, 100, 3001]
   窗口: [3001-3000, 3001] = [1, 3001]
   清理: 无需清理（1 >= 1）
   返回: 3

4. ping(3002):
   添加: requests = [1, 100, 3001, 3002]
   窗口: [3002-3000, 3002] = [2, 3002]
   清理: 移除1（1 < 2），保留[100, 3001, 3002]
   返回: 3
```

### 为什么使用队列？

1. **FIFO特性**：最早的请求最先过期，符合队列的先进先出
2. **高效操作**：队列头尾操作都是O(1)
3. **自然顺序**：时间戳递增正好符合队列的入队顺序

## 边界情况

1. **首次请求**：队列为空，直接返回1
2. **所有请求都在窗口内**：无需移除任何请求
3. **需要移除多个过期请求**：循环移除直到队列头部请求在窗口内
4. **时间戳很大**：不影响算法逻辑，只影响窗口范围

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 队列滑动窗口 | O(1) 摊还 | O(W) | 最优解，推荐 |
| 列表模拟 | O(n) | O(W) | 简单但效率低 |
| 二分查找 | O(log n) | O(n) | 理论可行，空间浪费 |

## 关键要点

1. **滑动窗口思想**：维护固定时间范围内的数据
2. **队列的选择**：利用FIFO特性处理时间顺序
3. **摊还分析**：虽然单次可能O(k)，但总体是O(1)
4. **时间戳单调性**：题目保证的重要条件，简化了算法设计

## 相关题目

- [239. Sliding Window Maximum](239_sliding_window_maximum.md) - 滑动窗口最大值
- [346. Moving Average from Data Stream](346_moving_average_data_stream.md) - 数据流中的移动平均值
- [1429. First Unique Number](1429_first_unique_number.md) - 第一个唯一数字

这道题是滑动窗口和队列应用的经典例子，很好地展示了如何利用数据结构的特性解决实际问题。
