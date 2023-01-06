# reverse linked list

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

**Input:** head = [1,2,3,4,5]
**Output:** [5,4,3,2,1]

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

**Input:** head = [1,2]
**Output:** [2,1]

**Example 3:**

**Input:** head = []
**Output:** []

**Constraints:**

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

#### 算法来自于udemy，很经典的问题，必须要掌握

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Set up current,previous, and next nodes
        current = head
        previous = None
        nextnode = None

        # until we have gone through to the end of the list
        while current:

            # Make sure to copy the current nodes next node to a variable next_node
            # Before overwriting as the previous node for reversal
            nextnode = current.next

            # Reverse the pointer ot the next_node
            current.next = previous

            # Go one forward in the list
            previous = current
            current = nextnode

        return previous
```

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=None
        cur=head
        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        return prev
```
