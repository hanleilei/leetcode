# remove duplicate from sorted list

[[linkedlist]]

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Subscribe to see which companies asked this question.

只能说这类题目的套路

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre, cur = dummy, head
        while cur != None and cur.next != None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
```

这个逻辑似乎有点复杂，来个简单的：

```Python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        p=head
        while(p.next):
            if(p.val==p.next.val):
                p.next=p.next.next
            else:
                p=p.next
        return head
```

直接和26题类似：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        slow = head
        fast = head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head
        
```

上面的问题，只是为了解决排序数组中的重复元素，下面的方法，可以全链表去重：

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        visited = set()
        while cur:
            if cur.val in visited:
                pre.next = cur.next
            else:
                visited.add(cur.val)
                pre = cur
            cur = cur.next
        return head
```
