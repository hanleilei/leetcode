# Sliding Window Median

[[heap]] [[sliding-window]] [[design]]

## Problem Description

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if `arr = [2,3,4]`, the median is `3`.
For examples, if `arr = [1,2,3,4]`, the median is `(2 + 3) / 2 = 2.5`.

You are given an integer array `nums` and an integer `k`. There is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. **Answers within 10^-5 of the actual value will be accepted.**

### Examples

**Example 1:**

```text
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]

Explanation:
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
```

**Example 2:**

```text
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
```

### Constraints

- `1 <= k <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## 解法一：SortedList（简洁推荐）

```python
from sortedcontainers import SortedList
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 使用 SortedList 自动维护有序性
        sl = SortedList()
        res = []
        
        for i in range(len(nums)):
            # 添加新元素到有序列表
            sl.add(nums[i])
            
            # 移除超出窗口的元素
            if len(sl) > k:
                sl.remove(nums[i - k])
            
            # 当窗口满时，计算中位数
            if len(sl) == k:
                if k % 2 == 1:
                    # 奇数个元素，取中间值
                    res.append(float(sl[k // 2]))
                else:
                    # 偶数个元素，取中间两个值的平均
                    res.append((sl[k // 2 - 1] + sl[k // 2]) / 2.0)
        
        return res
```

**优点：**

- 代码简洁，易于理解
- 自动维护有序性
- 时间复杂度 O(n log k)

**缺点：**

- 依赖第三方库 `sortedcontainers`

---

## 解法二：双堆（最优解，无外部库）

```python
import heapq
from collections import defaultdict
from typing import List

class DualHeap:
    """使用两个堆维护滑动窗口的中位数"""
    
    def __init__(self, k):
        self.small = []         # 大顶堆（存储较小的一半，用负数模拟）
        self.large = []         # 小顶堆（存储较大的一半）
        self.small_size = 0     # 大顶堆的实际大小
        self.large_size = 0     # 小顶堆的实际大小
        self.k = k
        self.delayed = defaultdict(int)  # 懒惰删除标记：值 -> 被标记删除次数

    def push(self, num):
        """向双堆中添加元素"""
        # 默认添加到 small（大顶堆）
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self._balance()

    def pop(self, num):
        """从双堆中删除元素（使用懒惰删除）"""
        # 标记为待删除，不实际删除
        self.delayed[num] += 1
        
        # 更新堆的大小
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self._prune_small()
        else:
            self.large_size -= 1
            if num == self.large[0]:
                self._prune_large()
        
        self._balance()

    def get_median(self):
        """获取当前中位数"""
        if self.k % 2 == 1:
            # 奇数个元素
            return float(-self.small[0])
        else:
            # 偶数个元素，返回中间两个的平均
            return (-self.small[0] + self.large[0]) / 2.0

    def _balance(self):
        """保持两个堆的大小平衡"""
        # 平衡条件：small_size = (k + 1) // 2
        if self.small_size > self.large_size + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
            self.small_size -= 1
            self.large_size += 1
            self._prune_small()
        elif self.small_size < self.large_size:
            heapq.heappush(self.small, -heapq.heappop(self.large))
            self.small_size += 1
            self.large_size -= 1
            self._prune_large()

    def _prune_small(self):
        """清理大顶堆的懒惰删除标记"""
        while self.small and self.delayed.get(-self.small[0], 0) > 0:
            num = -heapq.heappop(self.small)
            self.delayed[num] -= 1
            if self.delayed[num] == 0:
                del self.delayed[num]

    def _prune_large(self):
        """清理小顶堆的懒惰删除标记"""
        while self.large and self.delayed.get(self.large[0], 0) > 0:
            num = heapq.heappop(self.large)
            self.delayed[num] -= 1
            if self.delayed[num] == 0:
                del self.delayed[num]


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        res = []
        
        # 初始化第一个窗口
        for i in range(k):
            dh.push(nums[i])
        res.append(dh.get_median())
        
        # 滑动窗口处理
        for i in range(k, len(nums)):
            dh.pop(nums[i - k])  # 移除左边出窗口的元素
            dh.push(nums[i])     # 添加右边进窗口的元素
            res.append(dh.get_median())
        
        return res
```

**核心思想：**

- **堆分工**：维护两个堆
  - `small`（大顶堆）：存储较小的一半元素
  - `large`（小顶堆）：存储较大的一半元素

- **平衡条件**：
  - 当 k 为奇数：`small_size = (k + 1) // 2`，`large_size = k // 2`，中位数为 `small` 的堆顶
  - 当 k 为偶数：`small_size = large_size = k // 2`，中位数为两个堆顶的平均

- **懒惰删除策略**：
  - 标记待删除元素而不立即删除
  - 在平衡操作中遇到堆顶是已标记删除的元素时才清理
  - 避免了 O(k) 的删除操作

**时间复杂度：** O(n log k)
**空间复杂度：** O(k)

解法三：双堆 + 懒惰删除:

```python
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 0:
            return []
        
        # 小技巧：让max_heap始终多一个元素或相等
        max_heap, min_heap = [], []  # max_heap存较小一半（大顶堆），min_heap存较大一半（小顶堆）
        removed = defaultdict(int)
        result = []
        
        # 初始化第一个窗口
        for i in range(k):
            heapq.heappush(max_heap, -nums[i])
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        result.append(self._get_median(max_heap, min_heap, k))
        
        for i in range(k, len(nums)):
            out_num, in_num = nums[i-k], nums[i]
            removed[out_num] += 1
            
            # 判断出队元素在哪个堆中
            balance = -1 if out_num <= -max_heap[0] else 1
            
            # 入队新元素
            if in_num <= -max_heap[0]:
                heapq.heappush(max_heap, -in_num)
                balance += 1
            else:
                heapq.heappush(min_heap, in_num)
                balance -= 1
            
            # 调整平衡
            if balance < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            elif balance > 0:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            
            # 清理堆顶
            while max_heap and removed.get(-max_heap[0], 0) > 0:
                num = -heapq.heappop(max_heap)
                removed[num] -= 1
                if removed[num] == 0:
                    del removed[num]
            
            while min_heap and removed.get(min_heap[0], 0) > 0:
                num = heapq.heappop(min_heap)
                removed[num] -= 1
                if removed[num] == 0:
                    del removed[num]
            
            result.append(self._get_median(max_heap, min_heap, k))
        
        return result
    
    def _get_median(self, max_heap, min_heap, k):
        if k % 2 == 1:
            return -max_heap[0]
        return (-max_heap[0] + min_heap[0]) / 2
```

---

## 算法分析

### 方法对比

| 操作     | 排序数组 | 双堆     |
|----------|----------|----------|
| 插入     | O(k)     | O(log k) |
| 删除     | O(k)     | O(log k) |
| 查询中位数 | O(1)     | O(1)     |
| **总复杂度** | **O(nk)** | **O(n log k)** |

### 懒惰删除的优势

直接从堆中删除元素需要重新堆化，开销为 O(k)。而使用懒惰删除：

```text
时间线：
1. 删除时：记录 delayed[num]++，减小 size（O(1)）
2. 平衡时：如果堆顶是待删除元素，清理直到找到有效元素（O(log k)）
3. 结果：每个元素最多被清理一次，总开销 O(n log k)
```

---

## 相关题目

- [295. Find Median from Data Stream](295_find_median_from_data_stream.md) - 数据流的中位数
- [239. Sliding Window Maximum](239_sliding_window_maximum.md) - 滑动窗口最大值
- [76. Minimum Window Substring](076_minimum_windows_substring.md) - 最小窗口子串
