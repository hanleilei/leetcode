# add two numbers

[[linkedlist]]

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

**问题的关键在于，如果某个链表为空，则返回另一个链表。否则就返货两个链表的相应值的和**

建立一个新链表，然后把输入的两个链表从头往后撸，每两个相加，添加一个新节点到新链表后面。为了避免两个输入链表同时为空，我们建立一个dummy结点，将两个结点相加生成的新结点按顺序加到dummy结点之后，由于dummy结点本身不能变，所以我们用一个指针cur来指向新链表的最后一个结点。好，可以开始让两个链表相加了，这道题好就好在最低位在链表的开头，所以我们可以在遍历链表的同时按从低到高的顺序直接相加。while循环的条件两个链表中只要有一个不为空行，由于链表可能为空，所以我们在取当前结点值的时候，先判断一下，若为空则取0，否则取结点值。然后把两个结点值相加，同时还要加上进位carry。然后更新carry，直接 sum/10 即可，然后以 sum%10 为值建立一个新结点，连到cur后面，然后cur移动到下一个结点。之后再更新两个结点，若存在，则指向下一个位置。while循环退出之后，最高位的进位问题要最后特殊处理一下，若carry为1，则再建一个值为1的结点。

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

再来一个简短的：

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

再来一个速度超级快的版本：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = dummy = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
            carry = val // 10
            p.next = ListNode(val % 10)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            p = p.next
        return dummy.next
```

自己手搓的方法：

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry: 
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
```

基本都是一个套路
