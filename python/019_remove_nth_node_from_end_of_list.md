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
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # fast 先走 n 步
        for _ in range(n):
            fast = fast.next

        # fast 和 slow 一起走
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 删除倒数第 n 个节点
        slow.next = slow.next.next
        return dummy.next
```

多一个哨兵节点，避免越界的情况：

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = ListNode(0, head)
        cur = head
        slow, fast = p, head

        for _ in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = cur
            cur = cur.next
        
        slow.next = cur.next
        return p.next
```
