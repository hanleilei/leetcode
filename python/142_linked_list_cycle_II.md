# linked list cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

参考链接：https://blog.csdn.net/linhuanmars/article/details/21260943

这道题是Linked List Cycle的扩展，就是在确定是否有cycle之后还要返回cycle的起始点的位置。从Linked List Cycle中用的方法我们可以得知a=kc-b（不了解的朋友可以先看看Linked List Cycle）。现在假设有两个结点，一个从链表头出发，一个从b点出发，经过a步之后，第一个结点会到达cycle的出发点，而第二个结点会走过kc-b，加上原来的b刚好也会停在cycle的起始点。如此我们就可以设立两个指针，以相同速度前进直到相遇，而相遇点就是cycle的起始点。算法的时间复杂度是O(n+a)=O(2n)=O(n)，先走一次确定cycle的存在性并且走到b点，然后走a步找到cycle的起始点。空间复杂度仍是O(1)。

```python
class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            # if there is an exception, we reach the end and there is no cycle
            return None

        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next

        return head
```

下面是一个更清晰的算法实现，用字典，不过还是有点感觉是在抖机灵。。

```python
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        current = head
        dict = {}

        while current:
            if current not in dict:
                dict[current] = current
            else:
                return dict[current]
            current = current.next

        return None
```

用字典和用集合的实现思路很接近，其实还是觉得集合的思路更清楚：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = set()
        if not head:
            return None

        current = head

        while current:
            if current in s:
                return current
            else:
                s.add(current)
            current = current.next
        return None
```

这些方法都太慢了，来个快一点的：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        slow, fast, cross = head, head, False
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                cross = True
                break

        if cross:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None
```

似乎，这个才是最终的最佳答案，java和cpp都是这种写法：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head

        # If they meet then there is a loop
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # To find the starting element where the loop starts
            if slow is fast:
                fast = fast
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
```

fast 一定比 slow 多走了 k 步，这多走的 k 步其实就是 fast 指针在环里转圈圈，所以 k 的值就是环长度的「整数倍」。

假设相遇点距环的起点的距离为 m，那么结合上图的 slow 指针，环的起点距头结点 head 的距离为 k - m，也就是说如果从 head 前进 k - m 步就能到达环起点。

巧的是，如果从相遇点继续前进 k - m 步，也恰好到达环起点。因为结合上图的 fast 指针，从相遇点开始走k步可以转回到相遇点，那走 k - m 步肯定就走到环起点了

```python

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        # 判断是否有环
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        # 上面的代码类似 hasCycle 函数
        if not fast or not fast.next:
            # fast 遇到空指针说明没有环
            return None
        
        # 重新指向头结点
        slow = head 

        # 快慢指针同步前进，相交点就是环起点
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
```
