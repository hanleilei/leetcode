# reverse linked list

Reverse a singly linked list.

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
