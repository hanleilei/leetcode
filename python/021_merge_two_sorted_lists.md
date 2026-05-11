# 21. Merge Two Sorted Lists

## 问题描述

You are given the heads of two sorted linked lists `list1` and
`list2`.

Merge the two lists into one **sorted** list. The list should be
made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## 示例

**Example 1:**

```text
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

```text
1 -> 2 -> 4
     +
1 -> 3 -> 4
     ↓
1 -> 1 -> 2 -> 3 -> 4 -> 4
```

**Example 2:**

```text
Input: list1 = [], list2 = []
Output: []
```

**Example 3:**

```text
Input: list1 = [], list2 = [0]
Output: [0]
```

## 约束条件

- The number of nodes in both lists is in the range `[0, 50]`
- -100 <= Node.val <= 100
- Both `list1` and `list2` are sorted in **non-decreasing** order

## 解法

### 方法1：迭代法（哨兵节点）推荐

使用哨兵节点简化边界处理，逐个比较两个链表的节点。

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        迭代法：使用哨兵节点

        时间复杂度：O(m + n)
        空间复杂度：O(1)
        """
        # 哨兵节点，简化边界处理
        current = dummy = ListNode(0)

        # 同时遍历两个链表
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 连接剩余部分
        current.next = list1 if list1 else list2

        return dummy.next
```

### 方法2：递归法

利用递归的特性优雅地解决问题。

```python
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归法

        时间复杂度：O(m + n)
        空间复杂度：O(m + n) 递归栈
        """
        # 基本情况
        if not list1:
            return list2
        if not list2:
            return list1

        # 递归合并
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

### 方法3：原地修改（不用哨兵节点）

不使用哨兵节点，需要额外处理头节点。

```python
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],  list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        原地修改，不用哨兵节点

        时间复杂度：O(m + n)
        空间复杂度：O(1)
        """
        # 处理空链表
        if not list1:
            return list2
        if not list2:
            return list1

        # 确定头节点
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        current = head

        # 合并剩余节点
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 连接剩余部分
        current.next = list1 if list1 else list2

        return head
```

## 算法分析

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 迭代（哨兵） | O(m + n) | O(1) | 最优解 |
| 递归 | O(m + n) | O(m + n) | 代码简洁 |
| 无哨兵 | O(m + n) | O(1) | 需处理边界 |

其中 m 和 n 分别是两个链表的长度。

## 相关题目

- [0023. Merge k Sorted Lists](./023-merge_k_sorted_lists.md)
- [0088. Merge Sorted Array](./088_merge_sorted_array.md)
- [0148. Sort List](./148_sort_list.md)
- [0206. Reverse Linked List](./206_reverse_linked_list.md)
- [0141. Linked List Cycle](./141_linked_list_cycle.md)
