# Palindrome Linked List

[[linkedlist]] [[2points]] [[recursion]]

## Problem Description

Given a singly linked list, determine if it is a palindrome.

A palindrome list reads the same forwards and backwards.

### Examples

**Example 1:**

```text
Input: head = [1,2,2,1]
Output: true
```

**Example 2:**

```text
Input: head = [1,2]
Output: false
```

### Constraints

- The number of nodes in the list is in the range `[1, 10^5]`
- `0 <= Node.val <= 9`

### Follow up

Could you do it in O(n) time and O(1) space?

---

## 解法一：快慢指针+反转后半部分（最优）

```python
from typing import Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        判断链表是否为回文：使用快慢指针找中点，反转后半部分，再比较
        思路：
        1. 使用快慢指针找到链表中点
        2. 反转后半部分
        3. 从头尾同时遍历，比较值是否相等
        """
        if not head or not head.next:
            return True

        # 步骤1：快慢指针找中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 步骤2：反转后半部分
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # 步骤3：比较前半部分和反转后的后半部分
        left, right = head, prev
        while right:  # right先到None（奇数长度链表中点不比较）
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
```

或者：

```python   
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        left = head
        right = self.reverse((slow))
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre        
```

**算法分析：**

- **快慢指针找中点**：时间O(n/2)
- **反转后半部分**：时间O(n/2)
- **比较两部分**：时间O(n/2)
- 总时间复杂度：**O(n)**
- 空间复杂度：**O(1)**（只使用指针，不创建新数据结构）

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n) |
| 空间复杂度 | O(1) |

---

## 解法二：栈方法（参考）

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        使用栈存储前半部分值，与后半部分比较

        思路：
        1. 快慢指针找中点
        2. 快指针扫描时将前半部分压栈
        3. 从中点开始逐个出栈与后半部分比较
        """
        if not head or not head.next:
            return True

        stack = []
        slow = fast = head

        # 快慢指针，同时将前半部分压栈
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # 奇数长度链表时，跳过中间节点
        if fast:
            slow = slow.next

        # 后半部分与栈比较
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n) |
| 空间复杂度 | O(n/2) |

---

## 解法三：数组法（简洁但非最优）

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        最简单的方法：将链表值存入数组，判断数组是否回文
        """
        if not head or not head.next:
            return True

        # 将链表所有值存入数组
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # 判断数组是否回文
        return values == values[::-1]
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n) |
| 空间复杂度 | O(n) |

---

## 解法对比

| 方法 | 时间 | 空间 | 符合Follow-up | 难度 |
|------|------|------|---------------|------|
| **快慢指针+反转** | O(n) | O(1) | ✅ | 中 |
| 栈方法 | O(n) | O(n/2) | ❌ | 易 |
| 数组法 | O(n) | O(n) | ❌ | 易 |
| 递归（栈隐式） | O(n) | O(n) | ❌ | 难 |

---

## 关键点剖析

### 快慢指针找中点的细节

```text
偶数长度链表：1 -> 2 -> 2 -> 1
  初始：slow = fast = 1
  第1步：slow = 2, fast = 2
  第2步：slow = 2, fast = None（停止）
  结果：slow指向第二个2（后半部分起点）

奇数长度链表：1 -> 2 -> 3 -> 2 -> 1
  初始：slow = fast = 1
  第1步：slow = 2, fast = 3
  第2步：slow = 3, fast = 2
  第3步：slow = 2, fast = None（停止）
  结果：slow指向第二个2（跳过中间的3）
```

### 反转算法的关键

```text
原始后半部分：2 -> 2 -> None
反转过程：
  step1: prev=None, curr=2(第一个)
         2.next指向None，prev指向2
  step2: prev=2, curr=2(第二个)
         2.next指向prev(第一个2)，prev指向2(第二个)
  结果：2 <- 2
```

---

## 常见错误

❌ **错误1：没有处理奇数长度链表**

```python
# 错误：不判断fast，会导致奇数链表中间节点被比较两次
while right:
    if left.val != right.val:
        return False
```

❌ **错误2：反转后忘记处理**

```python
# 错误：反转了后半部分但没有"恢复"，原链表被修改
# 如果面试官问能否恢复，需要再反转一次
```

---

## 相关题目

- [206. Reverse Linked List](206_reverse_linked_list.md) - 反转整个链表
- [92. Reverse Linked List II](092_reverse_linked_list_ii.md) - 反转链表II
- [143. Reorder List](143_reorder_list.md) - 重排链表
