# reorder list

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

```text
Given 1->2->3->4, reorder it to 1->4->2->3.
```

Example 2:

```text
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None or head.next.next==None:
            return

        # break linked list into two equal length
        slow = fast = head                              #快慢指针技巧
        while fast and fast.next:                       #需要熟练掌握
            slow = slow.next                            #链表操作中常用
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # reverse linked list head2
        dummy=ListNode(0); dummy.next=head2             #翻转前加一个头结点
        p=head2.next; head2.next=None                   #将p指向的节点一个一个插入到dummy后面
        while p:                                        #就完成了链表的翻转
            tmp=p; p=p.next                             #运行时注意去掉中文注释
            tmp.next=dummy.next
            dummy.next=tmp
        head2=dummy.next

        # merge two linked list head1 and head2
        p1 = head1; p2 = head2
        while p2:
            tmp1 = p1.next; tmp2 = p2.next
            p1.next = p2; p2.next = tmp1
            p1 = tmp1; p2 = tmp2

```

再来一个更简洁的版本：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return

        # find midpoint of list
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # reverse second half of list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge
        l1, l2 = head, prev
        while l2.next:
            l1.next, l1 = l2, l1.next
            l2.next, l2 = l1, l2.next

        return

```
