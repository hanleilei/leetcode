# Min Stack

[[stack]]

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

## Example

```text
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

很简单的问题，没有任何难度，直接用deque就好了，但是这样没有满足要求：必须所有的操作都是O(1)的时间复杂度。

```python
from collections import deque

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.q)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

但是，江湖传言，需要用两个栈，另一个栈需要用来存储每次栈插入元素后，栈的最小值，这样将的好处是每次都会O(1)的时间复杂度。

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))  # 在每个元素x入栈时把当前栈的最小值m存储起来

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
