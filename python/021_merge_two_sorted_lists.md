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
    def mergeTwoLists(
        self, 
        list1: Optional[ListNode], 
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        迭代法：使用哨兵节点

        时间复杂度：O(m + n)
        空间复杂度：O(1)
        """
        # 哨兵节点，简化边界处理
        dummy = ListNode(0)
        current = dummy

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
    def mergeTwoLists(
        self, 
        list1: Optional[ListNode], 
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
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
    def mergeTwoLists(
        self, 
        list1: Optional[ListNode], 
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
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

### 为什么使用哨兵节点？

哨兵节点（dummy node）的优势：

1. **简化边界处理**：不需要特判头节点
2. **统一操作**：所有节点用相同方式处理
3. **代码简洁**：减少条件判断

```python
# 不用哨兵：需要特判头节点
if not head:
    head = node
else:
    current.next = node

# 用哨兵：统一处理
dummy = ListNode(0)
current = dummy
current.next = node
```

### 执行过程示例

以 `list1 = [1,2,4]`, `list2 = [1,3,4]` 为例。

初始状态：

```text
dummy -> None
list1: 1 -> 2 -> 4
list2: 1 -> 3 -> 4
```

**Step 1**：比较 1 vs 1

```text
1 <= 1, 选 list1
dummy -> 1
         ↑
      current
list1: 2 -> 4
list2: 1 -> 3 -> 4
```

**Step 2**：比较 2 vs 1

```text
2 > 1, 选 list2
dummy -> 1 -> 1
              ↑
           current
list1: 2 -> 4
list2: 3 -> 4
```

**Step 3**：比较 2 vs 3

```text
2 <= 3, 选 list1
dummy -> 1 -> 1 -> 2
                   ↑
                current
list1: 4
list2: 3 -> 4
```

**Step 4**：比较 4 vs 3

```text
4 > 3, 选 list2
dummy -> 1 -> 1 -> 2 -> 3
                        ↑
                     current
list1: 4
list2: 4
```

**Step 5**：比较 4 vs 4

```text
4 <= 4, 选 list1
dummy -> 1 -> 1 -> 2 -> 3 -> 4
                             ↑
                          current
list1: None
list2: 4
```

**Step 6**：连接剩余

```text
list1 为 None，连接 list2
dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
```

返回 `dummy.next`：`1 -> 1 -> 2 -> 3 -> 4 -> 4`

## 常见错误

### 错误1：忘记返回 dummy.next

```python
# 错误：返回了哨兵节点
return dummy  # 错误！

# 正确：返回哨兵节点的下一个
return dummy.next
```

### 错误2：移动指针错误

```python
# 错误：忘记移动 current
current.next = list1
list1 = list1.next
# 忘记：current = current.next

# 正确：
current.next = list1
list1 = list1.next
current = current.next
```

### 错误3：剩余部分处理错误

```python
# 错误：分别处理
if list1:
    current.next = list1
if list2:
    current.next = list2

# 正确：只可能有一个非空
current.next = list1 if list1 else list2
# 或者更简洁：
current.next = list1 or list2
```

### 错误4：递归终止条件不完整

```python
# 错误：只处理一种情况
if not list1:
    return list2
# 忘记处理 list2 为空的情况

# 正确：
if not list1:
    return list2
if not list2:
    return list1
```

### 错误5：修改了输入链表的值

```python
# 错误：创建新节点（不必要）
new_node = ListNode(list1.val)
current.next = new_node

# 正确：直接连接原节点
current.next = list1
```

## 相关题目

- [0023. Merge k Sorted Lists](./023-merge_k_sorted_lists.md)
- [0088. Merge Sorted Array](./088_merge_sorted_array.md)
- [0148. Sort List](./148_sort_list.md)
- [0206. Reverse Linked List](./206_reverse_linked_list.md)
- [0141. Linked List Cycle](./141_linked_list_cycle.md)

