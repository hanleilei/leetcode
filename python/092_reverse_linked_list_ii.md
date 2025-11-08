# Reverse Linked List II

[[linkedlist]] [[recursion]]

## Problem Description

Reverse a linked list from position m to n. Do it in-place and in one-pass.

### Examples

**Example 1:**

```text
Input: head = 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

Explanation: Reverse nodes from position 2 to 4
```

**Example 2:**

```text
Input: head = 5->NULL, m = 1, n = 1
Output: 5->NULL
```

### Constraints

- The number of nodes in the list is `n`
- `1 <= m <= n <= length of list`
- `-100 <= Node.val <= 100`

---

## 解法一：虚拟头+逐个反转（最优）

```python
from typing import Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        """
        在位置m到n之间反转链表，原地操作，一次遍历
        
        思路：
        1. 创建虚拟头节点处理边界情况
        2. 找到m-1位置的节点作为反转段的前驱
        3. 逐个将[m, n]范围的节点提取到前面（每次都是提到反转段的最前面）
        4. 时间复杂度O(n)，只需一次遍历
        """
        if not head or not head.next:
            return head
        
        # 创建虚拟头节点
        dummy = ListNode(0)
        dummy.next = head
        
        # pre：指向反转段前一个节点
        pre = dummy
        
        # 移动到第m-1个节点的位置
        for _ in range(m - 1):
            pre = pre.next
        
        # curr：指向反转段的第一个节点
        curr = pre.next
        
        # 逐个将后续节点提取到前面（共n-m个节点需要反转）
        for _ in range(n - m):
            # tmp：下一个要提的节点
            tmp = curr.next
            
            # 将tmp从链表中移出
            curr.next = tmp.next
            
            # 将tmp插入到反转段的最前面（即pre.next）
            tmp.next = pre.next
            pre.next = tmp
        
        return dummy.next
```

**关键思路演示：**

```text
原始：1 -> 2 -> 3 -> 4 -> 5, m=2, n=4

初始化：
  dummy -> 1 -> 2 -> 3 -> 4 -> 5
  pre指向1前（dummy）

第一步：提取节点3（curr.next）
  curr指向2，tmp指向3
  操作：2.next = 4, 3.next = 2, dummy.next = 3
  结果：1 -> 3 -> 2 -> 4 -> 5
  
第二步：提取节点4（curr.next）
  curr指向2，tmp指向4
  操作：2.next = 5, 4.next = 3, 1后面.next = 4
  结果：1 -> 4 -> 3 -> 2 -> 5
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n) |
| 空间复杂度 | O(1) |

---

## 解法二：递归方法

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        """
        使用递归方法反转链表的一部分
        """
        # 递归处理
        def reverse_recursive(node, m, n, count=1):
            # 到达反转区间的末尾+1
            if count == n + 1:
                return node
            
            # 递归到下一个节点
            next_node = reverse_recursive(node.next, m, n, count + 1)
            
            # 反向阶段：从最深处开始交换
            if count >= m:
                # 交换当前节点和下一个节点的值
                node.val, next_node.val = next_node.val, node.val
            
            return next_node
        
        reverse_recursive(head, m, n)
        return head
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n) |
| 空间复杂度 | O(n) |

---

## 算法对比

| 方法 | 时间复杂度 | 空间复杂度 | 优势 |
|------|-----------|-----------|------|
| **虚拟头+逐个反转** | O(n) | O(1) | **推荐，最优** |
| 递归 | O(n) | O(n) | 代码简洁但占用栈空间 |
| 三指针反转 | O(n) | O(1) | 逻辑复杂 |

---

## 关键点剖析

### 虚拟头节点的作用

- 统一处理m=1和m>1的情况
- 避免单独处理头节点

### 提取法的妙处

- 每次迭代都把下一个要反转的节点提到前面
- 经过n-m次迭代，整个反转段就自动反序了
- 只需一次遍历，不需要反复指针调整

### 为什么能原地操作

- 只是改变了指针方向，没有创建新节点
- 空间复杂度O(1)

---

## 常见错误

❌ **错误1：混淆虚拟头的位置**

```python
# 错误：虚拟头没有指向实际链表
dummy = ListNode(0)  # 忘记 dummy.next = head
```

❌ **错误2：循环次数错误**

```python
# 错误：应该是 n-m 次，不是 n-m+1 次
for _ in range(n - m + 1):  # 这会导致多反转一个节点
```

---

## 相关题目

- [206. Reverse Linked List](206_reverse_linked_list.md) - 反转整个链表
- [25. Reverse Nodes in K-Group](025_reverse_node_in_k_group.md) - K个一组翻转链表
- [86. Partition List](086_partition_list.md) - 链表分割
