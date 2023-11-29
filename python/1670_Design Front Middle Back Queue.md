# Design Front Middle Back Queue

Design a queue that supports push and pop operations in the front, middle, and back.

Implement the FrontMiddleBack class:

```text
FrontMiddleBack() Initializes the queue.
void pushFront(int val) Adds val to the front of the queue.
void pushMiddle(int val) Adds val to the middle of the queue.
void pushBack(int val) Adds val to the back of the queue.
int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
```

Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].

## Example 1

```text
Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]


Explanation:
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

```text
1 <= val <= 109
At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack.
```

很傻逼的题目，都是corner case，用来恶心人不错。。

问题的关键是 rebalance函数，节省很多脑力

```python
class FrontMiddleBackQueue:
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def pushFront(self, val):
        self.left.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val):
        if len(self.left) == len(self.right):
            self.right.appendleft(val) 
        else:
            self.left.append(val)

    def pushBack(self, val):
        self.right.append(val)
        self.rebalance()

    def popFront(self):
        if not self.left:
            v = self.right.popleft() if self.right else -1 
        else:  
            v = self.left.popleft()
            self.rebalance()
        return v

    def popMiddle(self):
        if len(self.left) == len(self.right):
            return self.left.pop() if self.left else -1
        else:
            return self.right.popleft()

    def popBack(self):
        v = self.right.pop() if self.right else -1
        self.rebalance()
        return v

    def rebalance(self):
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())



# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
```
