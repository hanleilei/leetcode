# linked list cycle

[[linkedlist]]

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

## Example 1

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

## Example 2

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

## Example 3

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## Constraints

```text
The number of the nodes in the list is in the range [0, 10**4].
-10**5 <= Node.val <= 10**5
pos is -1 or a valid index in the linked-list.
```

Follow up: Can you solve it using O(1) (i.e. constant) memory?

很经典，也很简单的方法：一个快，一个慢的遍历整个链表，如果有环，它们就会相遇。

这个blog里面就描述的非常好：https://blog.csdn.net/linhuanmars/article/details/21200601

下面我们来考虑如何不用额外空间来判断是否有cycle，用到的方法很典型，就是那种walker-runner的方法，基本想法就是维护两个指针，一个走的快，一个走得慢，当一个走到链表尾或者两个相见的时候，能得到某个想要的结点，比如相遇点，中点等等。
介绍完方法，剩下的主要就是数学了，假设两个指针walker和runner，walker一倍速移动，runner两倍速移动。有一个链表，假设他在cycle开始前有a个结点，cycle长度是c，而我们相遇的点在cycle开始后b个结点。那么想要两个指针相遇，意味着要满足以下条件：(1) a+b+mc=s; (2) a+b+nc=2s; 其中s是指针走过的步数，m和n是两个常数。这里面还有一个隐含的条件，就是s必须大于等于a，否则还没走到cycle里面，两个指针不可能相遇。假设k是最小的整数使得a<=kc，也就是说(3) a<=kc<=a+c。接下来我们取m=0, n=k，用(2)-(1)可以得到s=kc以及a+b=kc。由此我们可以知道，只要取b=kc-a(由(3)可以知道b不会超过c)，那么(1)和(2)便可以同时满足，使得两个指针相遇在离cycle起始点b的结点上。
因为s=kc<=a+c=n，其中n是链表的长度，所以走过的步数小于等于n，时间复杂度是O(n)。并且不需要额外空间，空间复杂度O(1)。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

```
