# Implement Queue using Stacks

[[stack]] [[design]] [[queue]]

## Problem Description

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `pop`, `peek`, and `empty`).

Implement the `MyQueue` class:

- `void push(int x)` Pushes element x to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

**Notes:**

- You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.

## Examples

**Example 1:**

```text
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
```

## Constraints

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.
- All the calls to `pop` and `peek` are valid.

## 解法一：双栈法（推荐）

```python
class MyQueue:
    def __init__(self):
        """
        使用两个栈实现队列
        input_stack: 用于入队操作
        output_stack: 用于出队操作
        """
        self.input_stack = []   # 负责入队
        self.output_stack = []  # 负责出队

    def push(self, x: int) -> None:
        """
        入队操作：直接加入input_stack
        时间复杂度：O(1)
        """
        self.input_stack.append(x)

    def pop(self) -> int:
        """
        出队操作：从output_stack弹出
        如果output_stack为空，将input_stack全部转移过来
        时间复杂度：摊还O(1)
        """
        self._transfer_if_needed()
        return self.output_stack.pop()

    def peek(self) -> int:
        """
        查看队头元素：返回output_stack栈顶
        时间复杂度：摊还O(1)
        """
        self._transfer_if_needed()
        return self.output_stack[-1]

    def empty(self) -> bool:
        """
        判断队列是否为空：两个栈都为空
        时间复杂度：O(1)
        """
        return len(self.input_stack) == 0 and len(self.output_stack) == 0
    
    def _transfer_if_needed(self) -> None:
        """
        辅助方法：需要时将input_stack的元素转移到output_stack
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
```

**复杂度分析**：

- 时间复杂度：
  - `push`: O(1)
  - `pop`, `peek`: 摊还O(1)，最坏情况O(n)
- 空间复杂度：O(n) - 存储n个元素

## 解法二：使用 deque（简单但不符合题意）

```python
from collections import deque

class MyQueue:
    def __init__(self):
        """
        使用deque直接实现队列
        注意：这种方法不符合题目要求，仅作参考
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """入队到尾部"""
        self.queue.append(x)

    def pop(self) -> int:
        """从头部出队"""
        return self.queue.popleft()

    def peek(self) -> int:
        """查看头部元素"""
        return self.queue[0]

    def empty(self) -> bool:
        """判断是否为空"""
        return len(self.queue) == 0
```

## 解法三：单栈 + 递归（了解即可）

```python
class MyQueue:
    def __init__(self):
        """
        只使用一个栈，通过递归实现队列操作
        """
        self.stack = []

    def push(self, x: int) -> None:
        """直接入栈"""
        self.stack.append(x)

    def pop(self) -> int:
        """递归实现从底部取元素"""
        if len(self.stack) == 1:
            return self.stack.pop()
        
        # 递归取出栈顶元素
        top = self.stack.pop()
        result = self.pop()  # 递归调用
        self.stack.append(top)  # 恢复栈顶元素
        return result

    def peek(self) -> int:
        """递归实现查看底部元素"""
        if len(self.stack) == 1:
            return self.stack[-1]
        
        top = self.stack.pop()
        result = self.peek()  # 递归调用
        self.stack.append(top)
        return result

    def empty(self) -> bool:
        """判断栈是否为空"""
        return len(self.stack) == 0
```

## 算法详解

### 双栈法核心思路

1. **两个栈的分工**：
   - `input_stack`：专门负责入队操作
   - `output_stack`：专门负责出队操作

2. **转移时机**：
   - 只有当 `output_stack` 为空且需要出队时，才进行转移
   - 一次性将 `input_stack` 的所有元素转移到 `output_stack`

3. **FIFO特性实现**：
   - 通过两次"翻转"实现先进先出
   - 第一次翻转：从 `input_stack` 到 `output_stack`
   - 第二次翻转：从 `output_stack` 弹出（相当于再次翻转）

### 算法可视化

以操作序列 `push(1), push(2), pop(), push(3), pop(), pop()` 为例：

```text
初始状态：
input_stack: []
output_stack: []

1. push(1):
input_stack: [1]
output_stack: []

2. push(2):
input_stack: [1, 2]
output_stack: []

3. pop(): 需要转移
转移后：
input_stack: []
output_stack: [2, 1]  # 注意顺序翻转
弹出: 1

4. push(3):
input_stack: [3]
output_stack: [2]

5. pop(): output_stack非空，直接弹出
弹出: 2
output_stack: []

6. pop(): output_stack为空，需要转移
转移后：
input_stack: []
output_stack: [3]
弹出: 3
```

## 时间复杂度分析

### 摊还分析

虽然单次 `pop` 或 `peek` 操作可能需要O(n)时间（转移所有元素），但：

- 每个元素最多被转移一次
- n次操作的总时间复杂度为O(n)
- 摊还时间复杂度为O(1)

### 具体分析

| 操作 | 最好情况 | 最坏情况 | 摊还复杂度 |
|------|----------|----------|------------|
| push | O(1) | O(1) | O(1) |
| pop | O(1) | O(n) | O(1) |
| peek | O(1) | O(n) | O(1) |
| empty | O(1) | O(1) | O(1) |

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 双栈法 | 摊还O(1) | O(n) | 符合题意，最优解 |
| deque | O(1) | O(n) | 简单但违背题意 |
| 单栈递归 | O(n) | O(n) | 理论可行，效率低 |

## 关键要点

1. **懒惰转移**：只有在必要时才进行栈间转移，提高效率
2. **摊还分析**：理解为什么平均时间复杂度是O(1)
3. **栈的LIFO特性**：通过两次翻转实现FIFO
4. **边界处理**：转移前检查output_stack是否为空

## 相关题目

- [225. Implement Stack using Queues](225_implement_stack_using_queues.md) - 用队列实现栈
- [155. Min Stack](155_min_stack.md) - 最小栈
- [716. Max Stack](716_max_stack.md) - 最大栈

这道题目很好地展示了如何用一种数据结构模拟另一种数据结构，是理解栈和队列特性的经典题目。
