# partition list

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:
```
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
```

思路还是要开放：直接建两个链表，一个存大于x的，另一个存小于x的；然后首尾连接两个链表。

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None  # important! avoid cycle in linked list. otherwise u will get TLE.
        l1.next = h2.next
        return h1.next

```
