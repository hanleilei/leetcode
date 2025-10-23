# add two numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

### Example:

![](https://assets.leetcode.com/uploads/2021/04/09/sumii-linked-list.jpg)

```
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Follow up: Could you solve it without reversing the input lists?

先按照要求保存数字，计算结果，然后再重构链表。注意最后几行的重构链表的过程，是从右往左实现的。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1, x2 = 0, 0
        while l1:
            x1 = x1*10+l1.val
            l1 = l1.next
        while l2:
            x2 = x2*10+l2.val
            l2 = l2.next
        x = x1 + x2

        head = ListNode(0)
        if x == 0: return head
        while x:
            v, x = x%10, x//10
            head.next, head.next.next = ListNode(v), head.next

        return head.next

```

再来一个自己手搓出来的算法：
1. 写一个反转链表的方法
2. 对每个链表求反转
3. 相加，记录进位
4. 返回构造好的一个新的链表

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_reversed = self.reverseList(l1)
        l2_reversed = self.reverseList(l2)
        
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1_reversed or l2_reversed or carry: # 注意这里的 or 非常关键，确保链表部位空或者进位不为0
            val1 = l1_reversed.val if l1_reversed else 0
            val2 = l2_reversed.val if l2_reversed else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)。# 这里，哪怕两个链表都结束了，如果还有进位，则还需要加上一个进位的值。
            current = current.next
            
            if l1_reversed:
                l1_reversed = l1_reversed.next
            if l2_reversed:
                l2_reversed = l2_reversed.next
        
        return self.reverseList(dummy.next)
    
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
```
