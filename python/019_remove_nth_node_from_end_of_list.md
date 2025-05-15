# Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

整个程序分成三部分：

1. 设定一个指针先走 n 步，然后记录位置
2. 再来一个指针从头开始，两个指针齐头并进
3. 第一个指针找到链表的末尾，第二个指针所处地位之就是所要删除的元素。

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
        # 初始化
        fast = slow = head
        # 步骤1
        for _ in range(n):
            fast = fast.next
        # 判断是否越界
        if not fast:
            return head.next
        # 步骤2
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 步骤3
        slow.next = slow.next.next
        return head
```

再来一个

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = ListNode(0)
        p.next = head
        fast = slow = p
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return p.next
```
