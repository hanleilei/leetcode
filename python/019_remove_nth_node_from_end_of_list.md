# Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

## 好吧，我不是一次性过去的，现在算是理解双指针的含义了。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        for i in range(n-1):
            cur = cur.next

        while cur != None and cur.next != None:
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next
        while pre != None and pre.next != None:
            pre = pre.next
        return dummy.next

```
