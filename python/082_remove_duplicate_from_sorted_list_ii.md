# remove duplicates from sorted list II

[[linkedlist]]

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

## Example 1

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg)

```text
Input: 1->2->3->3->4->4->5
Output: 1->2->5
```

## Example 2

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg)

```text
Input: 1->1->1->2->3
Output: 2->3
```

## Constraints:

```text
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        p, pre = ListNode(0), ListNode(0)
        p.next = head
        pre = p
        cur = head
        while cur != None:
            while cur.next != None and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return p.next
```

时隔多年，再来一个：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
```
