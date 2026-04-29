# Flatten a Multilevel Doubly Linked List

[[linkedlist]]

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

Example 1:

![](https://assets.leetcode.com/uploads/2021/11/09/flatten11.jpg)

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:
![](https://assets.leetcode.com/uploads/2021/11/09/flatten12.jpg)

Example 2:

![](https://assets.leetcode.com/uploads/2021/11/09/flatten2.1jpg)

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

![](https://assets.leetcode.com/uploads/2021/11/24/list.jpg)

Example 3:

Input: head = []
Output: []
Explanation: There could be empty list in the input.

Constraints:

    The number of Nodes will not exceed 1000.
    1 <= Node.val <= 105

How the multilevel linked list is represented in test cases:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

To serialize all levels together, we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]

Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        curr = head
        while curr:
            if curr.child:
                nex = curr.next
                child = curr.child

                # 遇到一个child，先在 curr 这里豁开一个口子，把child变成 next 的关系
                curr.next = child
                curr.child = None
                child.prev = curr

                # 找到当前这个child链的最末尾
                while child.next:
                    child = child.next
                # 把child的最末尾的节点，跟上面豁开的口子 nex 接上
                if nex:
                    nex.prev = child
                child.next = nex
            curr = curr.next
        return head
```

dfs recursive:

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        self.flatten_list(head)
        return head

    def flatten_list(self, node):
        curr = node
        last = node

        while curr:
            nxt = curr.next

            if curr.child:
                child_head = curr.child
                child_tail = self.flatten_list(child_head)

                curr.next = child_head
                child_head.prev = curr
                curr.child = None

                if nxt:
                    child_tail.next = nxt
                    nxt.prev = child_tail

                last = child_tail
            else:
                last = curr

            curr = nxt

        return last
```

dfs + stack:

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummy = Node(0, None, None, None)
        prev = dummy
        stack = [head]

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                curr.child = None
            curr.next = None

            prev = curr

        # detach
        head = dummy.next
        if head: head.prev = None
        return head
```
