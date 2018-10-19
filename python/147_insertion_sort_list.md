# insertion sort list

Sort a linked list using insertion sort.

![](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


Algorithm of Insertion Sort:

1. Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
3. It repeats until no input elements remain.

Example 1:
```
Input: 4->2->1->3
Output: 1->2->3->4
```
Example 2:
```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

三步走：
1. 快慢指针，将链表分成两个
2. 快的那个链表求逆
3. 合并链表

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)                         #为链表加一个头节点
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:            #如果链表是升序的，那么curr指针一直往后移动
                pre = dummy                         #直到一个节点的值小于前面节点的值
                while pre.next.val < curr.next.val: #然后寻找插入的位置
                    pre = pre.next
                tmp = curr.next                     #上面的示意图就是以下这段代码
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next
```
