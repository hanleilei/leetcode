# Implement Queue using Stacks

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
Subscribe to see which companies asked this question.

如果不是有用标准库，就可以直接用两个列表作为 stack 表示：

```python
class MyQueue:

    def __init__(self):
        self.q1 = list()
        self.q2 = list()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if len(self.q2) == 0:
            while self.q1:
                self.q2.append(self.q1.pop())
        return self.q2.pop()

    def peek(self) -> int:
        if len(self.q2) == 0:
            while self.q1:
                self.q2.append(self.q1.pop())
        return self.q2[-1]

    def empty(self) -> bool:
        if len(self.q1) == 0 and len(self.q2) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

## 很简答，只要用 deque 的函数就够了

```python
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.q = deque()


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        return self.q.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.q.popleft()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.q[0]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.q) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
