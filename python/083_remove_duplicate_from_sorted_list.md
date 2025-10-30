# Remove Duplicates from Sorted List

[[linkedlist]]

## Problem Description

Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list **sorted** as well.

## Examples

**Example 1:**

```text
Input: head = [1,1,2]
Output: [1,2]
```

**Example 2:**

```text
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

## Constraints

- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`
- The list is guaranteed to be **sorted** in ascending order.

## 解法一：单指针遍历（最优解）

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur != None and cur.next != None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
```

这是最直接高效的方法，利用链表已排序的特性，时间复杂度O(n)，空间复杂度O(1)。

## 解法二：双指针法（类似26题）

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        slow = head
        fast = head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head
```

双指针法，slow维护去重后的链表，fast用于探索新元素。

## 解法三：通用去重法（适用于无序链表）

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        pre, cur = None, head
        visited = set()
        while cur:
            if cur.val in visited:
                pre.next = cur.next
            else:
                visited.add(cur.val)
                pre = cur
            cur = cur.next
        return head
```

使用哈希表的通用方法，可以处理无序链表的去重。时间复杂度O(n)，空间复杂度O(n)。

## 相关题目

- [82. Remove Duplicates from Sorted List II](082_remove_duplicates_from_sorted_list_II.md) - 删除排序链表中的重复元素 II
- [26. Remove Duplicates from Sorted Array](026_remove_duplicate_from_sorted_array.md) - 删除排序数组中的重复项
