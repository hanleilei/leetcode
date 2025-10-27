# Design Circular Queue

[[design]] [[queue]] [[array]]

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

## Class Interface

Implement the `MyCircularQueue` class:

- **`MyCircularQueue(k)`** Initializes the object with the size of the queue to be k.
- **`int Front()`** Gets the front item from the queue. If the queue is empty, return -1.
- **`int Rear()`** Gets the last item from the queue. If the queue is empty, return -1.
- **`boolean enQueue(int value)`** Inserts an element into the circular queue. Return true if the operation is successful.
- **`boolean deQueue()`** Deletes an element from the circular queue. Return true if the operation is successful.
- **`boolean isEmpty()`** Checks whether the circular queue is empty or not.
- **`boolean isFull()`** Checks whether the circular queue is full or not.

**Note**: You must solve the problem without using the built-in queue data structure in your programming language.

## Example

```text
Input:
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

Output:
[null, true, true, true, false, 3, true, true, true, 4]

Explanation:
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False, queue is full
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
```

## Constraints

- `1 <= k <= 1000`
- `0 <= value <= 1000`
- At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

## 解题思路

环形队列的核心是使用**固定大小的数组**和**双指针**来模拟环形结构：

1. **数据结构设计**：
   - 使用固定大小的数组存储元素
   - 维护 `head` 指针指向队首
   - 维护 `count` 计数器记录当前元素个数

2. **环形逻辑**：
   - 通过取模运算 `(index) % k` 实现环形效果
   - 队尾位置：`(head + count) % k`
   - 避免使用单独的 `tail` 指针，防止判空判满的边界问题

3. **关键操作**：
   - **判空**：`count == 0`
   - **判满**：`count == k`
   - **入队**：在队尾添加元素，`count++`
   - **出队**：移动队首指针，`count--`

## 解法一：数组 + 计数器（推荐）

```python
class MyCircularQueue:
    def __init__(self, k: int):
        """初始化循环队列"""
        self.queue = [0] * k  # 固定大小的数组
        self.k = k           # 队列容量
        self.head = 0        # 队首指针
        self.count = 0       # 当前元素个数

    def enQueue(self, value: int) -> bool:
        """在队尾插入元素"""
        if self.isFull():
            return False
        
        # 计算队尾位置并插入
        tail = (self.head + self.count) % self.k
        self.queue[tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """从队首删除元素"""
        if self.isEmpty():
            return False
        
        # 移动队首指针
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        """获取队首元素"""
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """获取队尾元素"""
        if self.isEmpty():
            return -1
        
        # 计算队尾位置
        tail = (self.head + self.count - 1) % self.k
        return self.queue[tail]

    def isEmpty(self) -> bool:
        """检查队列是否为空"""
        return self.count == 0

    def isFull(self) -> bool:
        """检查队列是否已满"""
        return self.count == self.k
```

**复杂度分析**：

- 时间复杂度：所有操作均为 O(1)
- 空间复杂度：O(k)

## 解法二：数组 + 双指针

```python
class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * (k + 1)  # 多分配一个空间来区分空和满
        self.k = k + 1
        self.head = 0
        self.tail = 0
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = (self.head + 1) % self.k
        return True
    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]
    
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1) % self.k]
    
    def isEmpty(self) -> bool:
        return self.head == self.tail
    
    def isFull(self) -> bool:
        return (self.tail + 1) % self.k == self.head
```

**特点**：使用额外空间来区分空队列和满队列的状态。

## 解法三：使用 deque（不推荐，违背题意）

```python
from collections import deque

class MyCircularQueue:
    def __init__(self, k: int):
        self.dq = deque([])
        self.size = k

    def enQueue(self, value: int) -> bool:
        if len(self.dq) < self.size:
            self.dq.append(value)
            return True     
        return False   

    def deQueue(self) -> bool:
        if len(self.dq) > 0:
            self.dq.popleft()
            return True       
        return False

    def Front(self) -> int:
        if len(self.dq) > 0:
            return self.dq[0]
        return -1

    def Rear(self) -> int:
        if len(self.dq) > 0:
            return self.dq[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.dq) == 0

    def isFull(self) -> bool:
        return len(self.dq) == self.size
```

**注意**：此解法违背了题目要求（不能使用内置队列数据结构）。

## 可视化演示

以容量为3的循环队列为例：

```text
初始状态（空队列）：
[ _, _, _ ]  head=0, count=0
  ↑

enQueue(1)：
[ 1, _, _ ]  head=0, count=1
  ↑

enQueue(2)：
[ 1, 2, _ ]  head=0, count=2
  ↑

enQueue(3)：
[ 1, 2, 3 ]  head=0, count=3（队列满）
  ↑

deQueue()：
[ _, 2, 3 ]  head=1, count=2
     ↑

enQueue(4)：
[ 4, 2, 3 ]  head=1, count=3（环形特性）
     ↑
```

## 算法对比

| 解法 | 空间复杂度 | 判空/判满实现 | 特点 |
|------|------------|---------------|------|
| 计数器法 | O(k) | 使用count变量 | 简洁明了，推荐 |
| 双指针法 | O(k+1) | 预留一个空位 | 经典实现 |
| deque法 | O(k) | 使用len() | 违背题意 |

## 关键要点

1. **环形逻辑**：所有位置计算都要使用 `% k` 取模运算
2. **边界处理**：正确区分空队列和满队列的状态
3. **指针维护**：队首指针和队尾位置的正确计算
4. **设计选择**：推荐使用计数器法，代码更简洁易懂

## 相关题目

- [641. Design Circular Deque](641_design_circular_deque.md) - 双端循环队列
- [346. Moving Average from Data Stream](346_moving_average_from_data_stream.md) - 数据流的移动平均值
- [933. Number of Recent Calls](933_number_of_recent_calls.md) - 最近的请求次数

这道题考查的是数据结构设计能力，重点掌握环形队列的实现原理和边界条件处理。

