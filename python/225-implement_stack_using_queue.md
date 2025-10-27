# Implement Stack using Queues

[[stack]] [[design]] [[queue]]

## Problem Description

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `pop`, `top`, and `empty`).

Implement the `MyStack` class:

- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

**Notes:**

- You must use **only** standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size` and `is empty` operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.

## Examples

**Example 1:**

```text
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
```

## Constraints

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.
- All the calls to `pop` and `top` are valid.

## 解法一：双队列法（推荐）

```python
from collections import deque

class MyStack:
    def __init__(self):
        """
        使用两个队列实现栈
        main_queue: 主队列，存储所有元素
        temp_queue: 临时队列，辅助实现栈操作
        """
        self.main_queue = deque()
        self.temp_queue = deque()

    def push(self, x: int) -> None:
        """
        入栈操作：直接加入主队列
        时间复杂度：O(1)
        """
        self.main_queue.append(x)

    def pop(self) -> int:
        """
        出栈操作：将除最后一个元素外的所有元素转移到临时队列
        然后弹出最后一个元素，再将元素转移回主队列
        时间复杂度：O(n)
        """
        # 将除最后一个元素外的所有元素转移到临时队列
        while len(self.main_queue) > 1:
            self.temp_queue.append(self.main_queue.popleft())
        
        # 弹出栈顶元素（队列中的最后一个元素）
        result = self.main_queue.popleft()
        
        # 交换两个队列的角色
        self.main_queue, self.temp_queue = self.temp_queue, self.main_queue
        
        return result

    def top(self) -> int:
        """
        查看栈顶元素：类似pop操作，但需要将元素重新放回
        时间复杂度：O(n)
        """
        # 将除最后一个元素外的所有元素转移到临时队列
        while len(self.main_queue) > 1:
            self.temp_queue.append(self.main_queue.popleft())
        
        # 获取栈顶元素
        result = self.main_queue[0]
        
        # 将栈顶元素也转移到临时队列
        self.temp_queue.append(self.main_queue.popleft())
        
        # 交换两个队列的角色
        self.main_queue, self.temp_queue = self.temp_queue, self.main_queue
        
        return result

    def empty(self) -> bool:
        """
        判断栈是否为空
        时间复杂度：O(1)
        """
        return len(self.main_queue) == 0
```

**复杂度分析**：

- 时间复杂度：
  - `push`: O(1)
  - `pop`, `top`: O(n)
  - `empty`: O(1)
- 空间复杂度：O(n) - 存储n个元素

## 解法二：单队列法（优化版本）这个最优！

```python
from collections import deque

class MyStack:
    def __init__(self):
        """
        使用单个队列实现栈
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        入栈操作：将新元素加入队列，然后将之前的所有元素重新排列
        使得新元素位于队列前端（模拟栈顶）
        时间复杂度：O(n)
        """
        self.queue.append(x)
        # 将新元素前面的所有元素重新排列到它后面
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        出栈操作：直接从队列前端弹出
        时间复杂度：O(1)
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        查看栈顶元素：返回队列前端元素
        时间复杂度：O(1)
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        判断栈是否为空
        时间复杂度：O(1)
        """
        return len(self.queue) == 0
```

**复杂度分析**：

- 时间复杂度：
  - `push`: O(n)
  - `pop`, `top`, `empty`: O(1)
- 空间复杂度：O(n) - 存储n个元素

## 解法三：使用 deque（不推荐，违背题意）

```python
from collections import deque

class MyStack:
    def __init__(self):
        """
        直接使用deque的栈操作
        注意：这种方法不符合题目要求，仅作参考
        """
        self.stack = deque()

    def push(self, x: int) -> None:
        """入栈到尾部"""
        self.stack.append(x)

    def pop(self) -> int:
        """从尾部出栈"""
        return self.stack.pop()

    def top(self) -> int:
        """查看尾部元素"""
        return self.stack[-1]

    def empty(self) -> bool:
        """判断是否为空"""
        return len(self.stack) == 0
```

## 算法详解

### 双队列法核心思路

1. **维护两个队列**：
   - `main_queue`：存储所有元素
   - `temp_queue`：临时存储，辅助操作

2. **栈顶元素位置**：
   - 栈顶元素始终是主队列的最后一个元素
   - 要访问最后一个元素，需要将前面的元素都转移走

3. **操作流程**：
   - `push`：直接加入主队列尾部
   - `pop/top`：将n-1个元素转移到临时队列，处理最后一个元素

### 单队列法核心思路

1. **重新排列策略**：
   - 每次`push`后，将新元素调整到队列前端
   - 这样栈顶元素始终在队列前端

2. **旋转操作**：
   - 新元素入队后，将它前面的所有元素依次出队再入队
   - 实现元素的重新排列

### 算法可视化

以操作序列 `push(1), push(2), top(), pop()` 为例：

**双队列法**：

```text
1. push(1):
   main_queue: [1]
   temp_queue: []

2. push(2):
   main_queue: [1, 2]
   temp_queue: []

3. top():
   转移: main_queue: [2], temp_queue: [1]
   结果: 2
   恢复: main_queue: [1, 2], temp_queue: []

4. pop():
   转移: main_queue: [2], temp_queue: [1]
   弹出: 2
   结果: main_queue: [1], temp_queue: []
```

**单队列法**：

```text
1. push(1):
   入队: [1]
   旋转0次: [1]

2. push(2):
   入队: [1, 2]
   旋转1次: [2, 1]

3. top():
   结果: 2

4. pop():
   弹出: 2
   结果: [1]
```

## 算法对比

| 解法 | push时间 | pop时间 | top时间 | 空间复杂度 | 特点 |
|------|----------|---------|---------|------------|------|
| 双队列法 | O(1) | O(n) | O(n) | O(n) | 入栈快，出栈慢 |
| 单队列法 | O(n) | O(1) | O(1) | O(n) | 入栈慢，出栈快 |
| deque直接 | O(1) | O(1) | O(1) | O(n) | 违背题意 |

## 关键要点

1. **队列FIFO vs 栈LIFO**：需要通过额外操作转换顺序
2. **权衡选择**：入栈快vs出栈快，根据使用场景选择
3. **队列操作限制**：只能使用标准队列操作
4. **空间换时间**：双队列法用额外空间简化某些操作

## 相关题目

- [232. Implement Queue using Stacks](232_implement_queue_using_stacks.md) - 用栈实现队列
- [155. Min Stack](155_min_stack.md) - 最小栈
- [716. Max Stack](716_max_stack.md) - 最大栈

这道题目展示了如何用一种数据结构模拟另一种数据结构的反向操作，是理解数据结构特性和转换技巧的好例子。
