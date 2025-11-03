# Linked List Random Node

[[linkedlist]]

## Problem Description

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the `Solution` class:

- `Solution(ListNode head)`: Initializes the object with the head of the singly-linked list `head`.
- `int getRandom()`: Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

## Examples

**Example 1:**

![1](https://assets.leetcode.com/uploads/2021/03/16/getrand-linked-list.jpg)

```text
Input: ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
       [[[1, 2, 3]], [], [], [], [], []]
Output: [null, 1, 3, 2, 2, 3]

Explanation:
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
```

## Constraints

- The number of nodes in the linked list will be in the range `[1, 10^4]`.
- `-10^4 <= Node.val <= 10^4`
- At most `10^4` calls will be made to `getRandom`.

**Follow up:**

- What if the linked list is extremely large and its length is unknown to you?
- Could you solve this efficiently without using extra space?

---

## 解法一：水塘抽样（Reservoir Sampling，最优解）

思路：

1. 算法问题是谷歌的一道算法题：给你一个未知长度的单链表，请你设计一个算法，只能遍历一次，随机地返回链表中的一个节点。
2. 这里说的随机是均匀随机（uniform random），也就是说，如果有 n 个元素，每个元素被选中的概率都是 1/n，不可以有统计意义上的偏差。

一般的想法就是，我先遍历一遍链表，得到链表的总长度 n，再生成一个 [0,n-1) 之间的随机数为索引，然后找到索引对应的节点。但这不符合只能遍历一次链表的要求。

这个问题的难点在于随机选择是「动态」的，比如说你现在你已经遍历了 5 个元素，你已经随机选取了其中的某个元素 a 作为结果，但是现在再给你一个新元素 b，你应该留着 a 还是将 b 作为结果呢？以什么逻辑做出的选择，才能保证你的选择方法在概率上是公平的呢？

先说结论，当你遇到第 i 个元素时，应该有 1/i 的概率选择该元素，1 - 1/i 的概率保持原有的选择。看代码容易理解这个思路：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.r = random.Random()

    def getRandom(self) -> int:
        res = 0
        i = 0
        p = self.head
        while p:
            i += 1
            # 以1/i的概率选择当前节点
            if self.r.randint(0, i - 1) == 0:
                res = p.val
            p = p.next
        return res
```

对于概率算法，代码往往都是很浅显的，但是这种问题的关键在于证明，你的算法为什么是对的？为什么每次以 1/i 的概率更新结果就可以保证结果是平均随机的？

我们来证明一下，假设总共有 n 个元素，我们要的随机性无非就是每个元素被选择的概率都是 1/n 对吧，那么对于第 i 个元素，它被选择的概率就是：

$\frac{1}{i} \times (1 - \frac{1}{i + 1}) \times (1 - \frac{1}{i + 2}) \times ... \times (1 - \frac{1}{n})= \frac{1}{i} \times (\frac{i}{i + 1}) \times (\frac{i + 1}{i + 2}) \times ... \times (\frac{n - 1}{n}) = \frac{1}{n}$

**核心思想：**

- 水塘抽样算法，适用于数据流或长度未知的链表，保证每个节点被选中的概率均等。
- 每遍历到第i个节点时，以1/i的概率替换当前答案。

**时间复杂度：** O(n)（每次getRandom遍历一次链表）
**空间复杂度：** O(1)

---

## 算法分析

### 水塘抽样的概率证明

对于第i个节点被选中的概率：

- 第i次被选中概率为1/i
- 之后每次都不被替换的概率为∏(j=i+1到n)(1-1/j) = (i/n)
- 所以最终概率为1/i * (i/n) = 1/n

### 复杂度对比

| 方法         | 时间复杂度 | 空间复杂度 | 适用场景         |
|--------------|------------|------------|------------------|
| 水塘抽样     | O(n)       | O(1)       | 长链表/数据流    |
| 预处理数组   | O(1)       | O(n)       | 空间充足/短链表  |

---

## 相关题目

- [398. Random Pick Index](398_random_pick_index.md) - 随机数索引
- [528. Random Pick with Weight](528_random_pick_with_weight.md) - 带权重的随机选择
