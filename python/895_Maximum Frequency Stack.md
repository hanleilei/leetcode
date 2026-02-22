# Maximum Frequency Stack

[[design]]

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

Constraints:

0 <= val <= 10^9
At most 2 * 10^4 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.

```python
class FreqStack:
    def __init__(self):
        self.stacks = []  # 栈套栈，stacks 中的每个元素都是一个栈
        self.cnt = defaultdict(int)  # 每个 val 的出现次数

    def push(self, val: int) -> None:
        if self.cnt[val] == len(self.stacks):  # 这个元素的频率已经是目前最多的，现在又出现了一次
            self.stacks.append([val])  # 那么必须创建一个新栈
        else:
            self.stacks[self.cnt[val]].append(val)  # 否则就压入对应的栈
        self.cnt[val] += 1  # 更新频率

    def pop(self) -> int:
        val = self.stacks[-1].pop()  # 弹出最右侧栈的栈顶元素
        if not self.stacks[-1]:  # 弹出后，最右侧栈为空
            self.stacks.pop()  # 删除
        self.cnt[val] -= 1  # 更新频率
        return val
```
