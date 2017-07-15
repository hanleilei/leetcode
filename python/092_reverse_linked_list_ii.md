# reverse linked list II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

## 注意链表元素的交换方法：先定位到要找的元素，然后看两个元素之间的距离，然后再求值

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummyhead = ListNode(0)
        dummyhead.next = head

        p = dummyhead

        for i in range(m-1):
            p = p.next

        curr = p.next
        for i in range(n-m):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = p.next
            p.next = tmp

        return dummyhead.next

```
