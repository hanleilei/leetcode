# swap nodes in pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre, curr = dummy, head
        while curr and curr.next:       
            # swap node between curr and curr.next
            pre.next = curr.next        
            curr.next = pre.next.next   
            pre.next.next = curr        
            # go over 2 nodes
            pre, curr = curr,curr.next  
        return dummy.next

```

还有一个递归方法：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        new_head = head.next
        head.next = self.swapPairs(head.next.next)
        new_head.next = head
        return new_head
```

上面的那个交换值的方法略绕，还有看到网友写的一个更简单的方法，非常好理解：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)  
        dummy.next = head  
        cur = dummy  
        try:  
            while True:  
                pre, cur, nxt = cur, cur.next, cur.next.next  
                # change the position of cur and nxt  
                pre.next, cur.next, nxt.next = nxt, nxt.next, cur  
                # now cur is in the third place  
        except:  
            return dummy.next  
```