# add two numbers

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

###### 问题的关键在于，如果某个链表为空，则返回另一个链表。否则就返货两个链表的相应值的和

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        cur = ret

        sum = 0
        while True:
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next

            cur.val = sum % 10
            sum //= 10
            if l1 != None or l2 != None or sum != 0:
                cur.next = ListNode(0)
                cur = cur.next
            else:
                break

        return ret
```
再来一个简短的，而且速度超级快的：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1,p2,dum,rem = l1, l2, ListNode(0),0
        p = dum
        while p1 or p2:
            cur = (p1.val if p1 else 0) + (p2.val if p2 else 0) + rem
            rem, cur = cur // 10, cur %10
            p.next = ListNode(cur)
            p,p1,p2 = p.next, p1.next if p1 else p1, p2.next if p2 else p2
        if rem: p.next = ListNode(rem)
        return dum.next
```
