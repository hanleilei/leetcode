021 Merge two sorted lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

###### 本题目只是考察了链表的基本概念：现在有两个已经排序过的链表，需要按照顺序合并。首先，挨个遍历两个链表的元素，只要两个链表不为空，就用cur链表指向比较小的链表中的节点，依次遍历。最后，需要将不为空的链表放在cur链表最后。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dum = cur = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2

        return dum.next

```
