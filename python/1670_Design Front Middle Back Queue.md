# Design Front Middle Back Queue

[[queue]] [[design]] [[deque]]

## Problem Description

Design a queue that supports push and pop operations in the front, middle, and back.

Implement the `FrontMiddleBackQueue` class:

- `FrontMiddleBackQueue()` Initializes the queue.
- `void pushFront(int val)` Adds `val` to the **front** of the queue.
- `void pushMiddle(int val)` Adds `val` to the **middle** of the queue.
- `void pushBack(int val)` Adds `val` to the **back** of the queue.
- `int popFront()` Removes the **front** element of the queue and returns it. If the queue is empty, return `-1`.
- `int popMiddle()` Removes the **middle** element of the queue and returns it. If the queue is empty, return `-1`.
- `int popBack()` Removes the **back** element of the queue and returns it. If the queue is empty, return `-1`.

**Notice** that when there are **two middle position choices**, the operation is performed on the **frontmost middle position choice**. For example:

- Pushing `6` into the middle of `[1, 2, 3, 4, 5]` results in `[1, 2, 6, 3, 4, 5]`.
- Popping the middle from `[1, 2, 3, 4, 5, 6]` returns `3` and results in `[1, 2, 4, 5, 6]`.

## Examples

**Example 1:**

```text
Input
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
```

## Constraints

- `1 <= val <= 10^9`
- At most `1000` calls will be made to `pushFront`, `pushMiddle`, `pushBack`, `popFront`, `popMiddle`, and `popBack`.

## 解法一：双端队列 + 平衡策略（推荐）

```python
from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        """
        使用两个双端队列维护平衡
        left: 存储队列前半部分
        right: 存储队列后半部分
        保持不变式：len(right) == len(left) 或 len(right) == len(left) + 1
        """
        self.left = deque()   # 前半部分
        self.right = deque()  # 后半部分

    def pushFront(self, val: int) -> None:
        """
        从前端添加元素
        时间复杂度：O(1)
        """
        self.left.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        """
        从中间添加元素
        时间复杂度：O(1)
        """
        if len(self.left) == len(self.right):
            # 总长度为偶数，添加到right的前端
            self.right.appendleft(val)
        else:
            # 总长度为奇数，添加到left的后端
            self.left.append(val)

    def pushBack(self, val: int) -> None:
        """
        从后端添加元素
        时间复杂度：O(1)
        """
        self.right.append(val)
        self._rebalance()

    def popFront(self) -> int:
        """
        从前端弹出元素
        时间复杂度：O(1)
        """
        if not self.left and not self.right:
            return -1
        
        if self.left:
            val = self.left.popleft()
            self._rebalance()
            return val
        else:
            # left为空，从right弹出
            return self.right.popleft()

    def popMiddle(self) -> int:
        """
        从中间弹出元素
        时间复杂度：O(1)
        """
        if not self.left and not self.right:
            return -1
        
        if len(self.left) == len(self.right):
            # 总长度为偶数，弹出left的后端（更靠前的中间位置）
            return self.left.pop() if self.left else -1
        else:
            # 总长度为奇数，弹出right的前端
            return self.right.popleft()

    def popBack(self) -> int:
        """
        从后端弹出元素
        时间复杂度：O(1)
        """
        if not self.right:
            return -1
        
        val = self.right.pop()
        self._rebalance()
        return val

    def _rebalance(self) -> None:
        """
        维护两个队列的平衡
        保持：len(right) == len(left) 或 len(right) == len(left) + 1
        """
        if len(self.left) > len(self.right):
            # left太长，移动一个元素到right前端
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            # right太长，移动一个元素到left后端
            self.left.append(self.right.popleft())
```

**复杂度分析**：

- 时间复杂度：所有操作都是O(1)
- 空间复杂度：O(n) - 存储n个元素

## 解法二：单个列表（不推荐）

```python
class FrontMiddleBackQueue:
    def __init__(self):
        """
        使用单个列表实现
        注意：中间操作的时间复杂度较高
        """
        self.queue = []

    def pushFront(self, val: int) -> None:
        """O(n) - 需要移动所有元素"""
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        """O(n) - 需要移动部分元素"""
        n = len(self.queue)
        mid = n // 2
        self.queue.insert(mid, val)

    def pushBack(self, val: int) -> None:
        """O(1) - 直接添加到末尾"""
        self.queue.append(val)

    def popFront(self) -> int:
        """O(n) - 需要移动所有元素"""
        if not self.queue:
            return -1
        return self.queue.pop(0)

    def popMiddle(self) -> int:
        """O(n) - 需要移动部分元素"""
        if not self.queue:
            return -1
        n = len(self.queue)
        mid = (n - 1) // 2  # 选择前面的中间位置
        return self.queue.pop(mid)

    def popBack(self) -> int:
        """O(1) - 直接从末尾弹出"""
        if not self.queue:
            return -1
        return self.queue.pop()
```

## 算法详解

### 双端队列方案核心思路

1. **分割策略**：
   - 将整个队列分为两部分：`left` 和 `right`
   - `left` 存储前半部分，`right` 存储后半部分

2. **平衡不变式**：
   - 始终保持：`len(right) == len(left)` 或 `len(right) == len(left) + 1`
   - 这确保中间位置始终在两个队列的边界处

3. **中间位置定义**：
   - 总长度为偶数：中间位置是 `left` 的末尾
   - 总长度为奇数：中间位置是 `right` 的开头

### 算法可视化

以示例操作为例，展示队列状态变化：

```text
初始状态：
left: [], right: []

1. pushFront(1):
   操作前: left=[], right=[]
   添加到left前端: left=[1], right=[]
   平衡后: left=[], right=[1]
   逻辑队列: [1]

2. pushBack(2):
   操作前: left=[], right=[1]
   添加到right后端: left=[], right=[1,2]
   平衡后: left=[1], right=[2] (right太长了)
   逻辑队列: [1,2]

3. pushMiddle(3):
   操作前: left=[1], right=[2] (长度相等)
   添加到right前端: left=[1], right=[3,2]
   无需平衡
   逻辑队列: [1,3,2]

4. pushMiddle(4):
   操作前: left=[1], right=[3,2] (right比left长1)
   添加到left后端: left=[1,4], right=[3,2]
   无需平衡
   逻辑队列: [1,4,3,2]

5. popFront():
   操作前: left=[1,4], right=[3,2]
   从left前端弹出: val=1, left=[4], right=[3,2]
   平衡后: left=[4], right=[3,2] (符合要求)
   返回: 1, 逻辑队列: [4,3,2]
```

### 平衡策略详解

**为什么需要平衡？**

- 保证中间位置的操作能在O(1)时间内完成
- 确保中间位置总是在两个队列的边界处

**平衡规则：**

1. 如果 `len(left) > len(right)`：移动 `left` 的末尾元素到 `right` 的开头
2. 如果 `len(right) > len(left) + 1`：移动 `right` 的开头元素到 `left` 的末尾

## 中间位置的处理

### 推入中间

- **偶数长度**：推入到 `right` 的前端（成为新的中间偏后位置）
- **奇数长度**：推入到 `left` 的后端（成为新的中间偏前位置）

### 弹出中间

- **偶数长度**：弹出 `left` 的后端（前面的中间位置）
- **奇数长度**：弹出 `right` 的前端（唯一的中间位置）

## 算法对比

| 解法 | pushFront | pushMiddle | pushBack | popFront | popMiddle | popBack |
|------|-----------|------------|----------|----------|-----------|---------|
| 双端队列 | O(1) | O(1) | O(1) | O(1) | O(1) | O(1) |
| 单列表 | O(n) | O(n) | O(1) | O(n) | O(n) | O(1) |

## 关键要点

1. **数据结构选择**：双端队列支持两端的高效操作
2. **平衡维护**：通过rebalance函数简化逻辑
3. **中间位置理解**：根据总长度奇偶性确定中间位置
4. **边界处理**：空队列时返回-1

## 相关题目

- [232. Implement Queue using Stacks](232_implement_queue_using_stacks.md) - 用栈实现队列
- [225. Implement Stack using Queues](225_implement_stack_using_queue.md) - 用队列实现栈
- [933. Number of Recent Calls](933_number_of_recent_calls.md) - 最近的请求次数

这道题考查了对双端队列的深入理解和复杂数据结构的设计能力，关键在于维护两个队列之间的平衡关系。
