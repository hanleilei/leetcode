# linked list cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

###### 很经典，也很简单的方法：一个快，一个慢的遍历整个链表，如果有环，它们就会相遇。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
```
