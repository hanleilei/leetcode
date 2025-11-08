# Partition List

[[linkedlist]] [[2points]]

## Problem Description

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

### Examples

**Example 1:**

```text
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

Explanation: 
- Nodes < 3: [1, 2, 2]
- Nodes >= 3: [4, 3, 5]
```

**Example 2:**

```text
Input: head = 2->1, x = 2
Output: 1->2
```

### Constraints

- The number of nodes in the list is in the range `[0, 200]`
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

---

## 解法：双链表（最优）

```python
from typing import Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        将链表按值x分割，小于x的在前，大于等于x的在后，相对顺序不变
        
        思路：
        1. 创建两个虚拟头节点，分别用于小于x和大于等于x的两个链表
        2. 遍历原链表，将节点分配到两个链表中
        3. 连接两个链表
        """
        l = less = ListNode(0)
        m = more = ListNode(0)
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next
        less.next = m.next
        more.next = None
        return l.next
```

**关键点详解：**

1. **为什么需要虚拟头节点？**
   - 简化处理：避免判断链表是否为空
   - 统一逻辑：小、大链表的处理完全相同

2. **为什么要设置 `less.next = None`？**
   - 如果原链表形如 `[5, 4, 1, 3, 2], x=3`
   - 大链表为 `5 -> 4 -> 3`，此时 `3.next` 仍指向原链表中的下一个节点
   - 不设置为None会形成环，导致 TLE（Time Limit Exceeded）

3. **遍历只需一次：O(n)**
   - 每个节点访问一次，不需要重排

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n) |
| 空间复杂度 | O(1) |

---

## 图解演示

```text
原始链表：1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3

第一步：初始化
  less: 0 -> ?
  more: 0 -> ?

第二步：遍历并分割
  1 < 3:    less: 0 -> 1
  4 >= 3:   more: 0 -> 4
  3 >= 3:   more: 0 -> 4 -> 3
  2 < 3:    less: 0 -> 1 -> 2
  5 >= 3:   more: 0 -> 4 -> 3 -> 5
  2 < 3:    less: 0 -> 1 -> 2 -> 2

第三步：连接
  more.next = None     (断开循环)
  less.next = more.next
  
  结果：1 -> 2 -> 2 -> 4 -> 3 -> 5
```

---

## 常见错误

❌ **错误1：忘记设置 `more.next = None`**

```python
# 会导致TLE（形成环）
l1.next = h2.next  # 直接连接，原来的链接还在
```

❌ **错误2：没有保留相对顺序**

```python
# 不能对节点重排或使用额外数据结构排序
```

---

## 相关题目

- [328. Odd Even Linked List](328_odd_even_linked_list.md) - 奇偶链表
- [92. Reverse Linked List II](092_reverse_linked_list_II.md) - 反转链表II
- [25. Reverse Nodes in K-Group](025_reverse_node_in_k_group.md) - K个一组翻转链表
