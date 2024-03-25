# Palindrome linked list

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

先求链表的反转，可见 206.
判断回文主要是前半部分和后半部分的比较，若能将后半部分反转（仍然是单链表），则可以方便的判断回文。该思路在实现上有多种方法，效率上也有差异。若能不借助多余的空间实现反转单链表后半部分，则可以实现空间复杂度 O(1) 的要求。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        slow = self.reverseList(slow)

        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True

    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head

```

判断回文主要是前半部分和后半部分的比较，若能将前半部分压栈，再依次出栈与后半部分比较，则可判断是否回文。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        new_list = []

        # 快慢指针法找链表的中点
        slow = fast = head
        while fast and fast.next:
            new_list.insert(0, slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast: # 链表有奇数个节点
            slow = slow.next

        for val in new_list:
            if val != slow.val:
                return False
            slow = slow.next
        return True
```

考虑到单链表缺失从后向前的信息，如果能得到双向信息将很容易判断回文。故考虑将单链表的节点值记录到一个数组中，判断数组是否回文；或通过一次遍历将单链表拓展成双向链表，再判断是否回文。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        tmp_list = []
        while head:
            tmp_list.append(head.val)
            head = head.next

        length = len(tmp_list)
        for i in range(0, length/2):
            if tmp_list[i] != tmp_list[length-i-1]:
                return False
        return True
```
