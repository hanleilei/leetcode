# implement stack using queues

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

###### 直接用collections里面的deque就能搞定了。

```python
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        from collections import deque
        self.stack = deque()


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        return self.stack.append(x)



    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()
        return self.stack        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return True
        else:
            return False

```
