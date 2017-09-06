# rotate list


Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

###### 经典问题，使用快慢指针就可以，由于k可能非常大，但是k如果大于链表长度，就会做重复的工作，所以先要得到链表长度，然后取模。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k==0:  
            return head
        ListLen = 0  
        p = head  
        while(p):  
            ListLen+=1  
            p = p.next  
        k = k%ListLen  
        if k==0:  
            return head  
        p = head  
        while(k>0):  
            k -=1  
            p = p.next  
        slow = head  
        fast = p  
        while fast.next:  
            slow = slow.next  
            fast = fast.next  

        new_head = slow.next   
        fast.next = head  
        slow.next = None  
        return new_head
```

下面的是一个速度更快的方法：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        length=0
        l=head
        while l:
            l=l.next
            length+=1

        if k>length:
            k=k%length

        current=head
        while current.next:
            current=current.next

        current.next=head

        for i in range(length-k):
            current=current.next

        head=current.next
        current.next=None
        return head
```
