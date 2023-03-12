023 merge k sorted lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example** 1:
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```
**Example** 2:
```
Input: lists = []
Output: []
```
**Example** 3:
```
Input: lists = [[]]
Output: []
```

## Constraints:

* k == lists.length
* 0 <= k <= 104
* 0 <= lists[i].length <= 500
* -104 <= lists[i][j] <= 104
* lists[i] is sorted in ascending order.
* The sum of lists[i].length will not exceed 104.

使用标准库的heapq方法实现

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        current = dummy = ListNode(0)

        heap = []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))

        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))

        return dummy.next

```

上面的方法，在Python3中，已经失败了，可以参考这个：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(None)
        curr = head
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return head.next
```

再来一个分治法

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)

    def merge(self, lst1, lst2):
        dummy = pt = ListNode(-1)
        while lst1 and lst2:
            if lst1.val < lst2.val:
                pt.next = lst1
                lst1 = lst1.next
            else:
                pt.next = lst2
                lst2 = lst2.next
            pt = pt.next

        pt.next = lst1 if not lst2 else lst2
        return dummy.next
```

其他的方法：

```python
# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):		
        if self:		
            return "{} -> {}".format(self.val, self.next)


# Merge two by two solution.
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
        left, right = 0, len(lists) - 1;
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = mergeTwoLists(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]
```

```python

# Time:  O(nlogk)
# Space: O(logk)
# Divide and Conquer solution.
class Solution2:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        def mergeKListsHelper(lists, begin, end):
            if begin > end:
                return None
            if begin == end:
                return lists[begin]
            return mergeTwoLists(mergeKListsHelper(lists, begin, (begin + end) / 2), \
                                 mergeKListsHelper(lists, (begin + end) / 2 + 1, end))

        return mergeKListsHelper(lists, 0, len(lists) - 1)
```


