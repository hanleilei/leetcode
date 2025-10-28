# Reverse Linked List

[[linkedlist]]

## Problem Description

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

## Examples

**Example 1:**

```text
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**

```text
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**

```text
Input: head = []
Output: []
```

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## 解法一：迭代法（推荐）

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        迭代法反转链表
        时间复杂度：O(n)，空间复杂度：O(1)
        """
        # 初始化三个指针
        prev = None     # 前一个节点
        curr = head     # 当前节点
        
        while curr:
            t = curr.next          # 暂存下一个节点
            curr.next = prev       # 反转当前节点的指向
            prev = curr            # 移动prev指针
            curr = t               # 移动curr指针
        
        return prev  # prev就是新的头节点
```

### 迭代法图解

以链表 `1 -> 2 -> 3 -> null` 为例，演示反转过程：

```text
初始状态：
prev = null    curr = 1 -> 2 -> 3 -> null
     ↑              ↑
   前节点         当前节点

第1步：保存next，反转指针
next_temp = 2 -> 3 -> null
curr.next = prev

结果：null <- 1    2 -> 3 -> null
         ↑         ↑
       prev      curr

第2步：移动指针
prev = 1 -> null
curr = 2 -> 3 -> null

状态：null <- 1    curr = 2 -> 3 -> null
            ↑             ↑
          prev         当前节点

第3步：保存next，反转指针
next_temp = 3 -> null
curr.next = prev

结果：null <- 1 <- 2    3 -> null
              ↑         ↑
            prev      curr

第4步：移动指针
prev = 2 -> 1 -> null
curr = 3 -> null

状态：null <- 1 <- 2    curr = 3 -> null
                  ↑             ↑
                prev         当前节点

第5步：保存next，反转指针
next_temp = null
curr.next = prev

结果：null <- 1 <- 2 <- 3    next_temp = null
                      ↑             ↑
                    prev          curr

第6步：移动指针
prev = 3 -> 2 -> 1 -> null
curr = null (循环结束)

最终结果：prev = 3 -> 2 -> 1 -> null
```

**核心要点**：

1. **三指针协作**：prev追踪已反转部分，curr处理当前节点，next_temp防止链表断开
2. **反转顺序**：先保存next → 反转指针 → 移动指针
3. **循环条件**：当curr为null时停止，此时prev指向新的头节点

**复杂度分析**：

- 时间复杂度：O(n) - 需要遍历链表一次
- 空间复杂度：O(1) - 只使用常数额外空间

## 解法二：递归法

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归法反转链表
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        def reverse_helper(curr, prev):
            if not curr:
                return prev  # 递归终止条件，返回新的头节点
            
            next_temp = curr.next    # 保存下一个节点
            curr.next = prev         # 反转当前节点的指向
            return reverse_helper(next_temp, curr)  # 递归处理下一个节点
        
        return reverse_helper(head, None)
```

**复杂度分析**：

- 时间复杂度：O(n) - 递归调用n次
- 空间复杂度：O(n) - 递归调用栈的深度

## 解法三：递归法（另一种写法）

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归法的另一种实现
        从链表尾部开始反转
        """
        # 递归终止条件
        if not head or not head.next:
            return head
        
        # 递归反转子链表
        new_head = self.reverseList(head.next)
        
        # 反转当前节点和下一个节点的指向
        head.next.next = head
        head.next = None
        
        return new_head
```

## 算法详解

### 迭代法核心思路

1. **三指针技巧**：
   - `prev`：指向已反转部分的尾节点
   - `curr`：指向当前要处理的节点
   - `next_temp`：暂存下一个节点，防止丢失

2. **反转步骤**：
   - 保存下一个节点
   - 反转当前节点的指针
   - 移动指针位置

### 算法可视化

以链表 `1 -> 2 -> 3 -> 4 -> 5` 为例：

```text
初始状态:
prev = null, curr = 1 -> 2 -> 3 -> 4 -> 5

第1步:
next_temp = 2 -> 3 -> 4 -> 5
curr.next = prev  →  1 -> null
prev = 1, curr = 2 -> 3 -> 4 -> 5

第2步:
next_temp = 3 -> 4 -> 5  
curr.next = prev  →  2 -> 1 -> null
prev = 2 -> 1 -> null, curr = 3 -> 4 -> 5

第3步:
next_temp = 4 -> 5
curr.next = prev  →  3 -> 2 -> 1 -> null
prev = 3 -> 2 -> 1 -> null, curr = 4 -> 5

第4步:
next_temp = 5
curr.next = prev  →  4 -> 3 -> 2 -> 1 -> null
prev = 4 -> 3 -> 2 -> 1 -> null, curr = 5

第5步:
next_temp = null
curr.next = prev  →  5 -> 4 -> 3 -> 2 -> 1 -> null
prev = 5 -> 4 -> 3 -> 2 -> 1 -> null, curr = null

返回 prev = 5 -> 4 -> 3 -> 2 -> 1 -> null
```

### 递归法核心思路

#### 方法一：尾递归

- 从头开始，每次处理一个节点
- 将当前节点的next指向前一个节点
- 递归处理下一个节点

#### 方法二：从尾部反转

- 先递归到链表尾部
- 从尾部开始逐步反转指针
- 最终返回新的头节点

## 边界情况处理

1. **空链表**：直接返回null
2. **单节点链表**：返回该节点本身
3. **两节点链表**：反转两个节点的指向关系

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 迭代法 | O(n) | O(1) | 最优解，推荐 |
| 递归法（尾递归） | O(n) | O(n) | 易理解，空间开销大 |
| 递归法（从尾反转） | O(n) | O(n) | 思路独特，较难理解 |

## 关键要点

1. **指针操作**：理解prev、curr、next三指针的作用
2. **状态保存**：反转前必须保存next节点
3. **边界处理**：空链表和单节点的特殊情况
4. **递归理解**：掌握递归的终止条件和状态转移

## 常见错误

1. **丢失节点**：忘记保存next节点导致链表断开
2. **指针混乱**：prev和curr的更新顺序错误
3. **边界遗漏**：没有处理空链表的情况
4. **递归栈溢出**：对于很长的链表，递归可能导致栈溢出

## 相关题目

- [92. Reverse Linked List II](092_reverse_linked_list_II.md) - 反转链表 II
- [25. Reverse Nodes in k-Group](025_reverse_node_in_k_group.md) - K 个一组翻转链表
- [24. Swap Nodes in Pairs](024_swap_nodes_in_pairs.md) - 两两交换链表中的节点

这道题是链表操作的基础题目，掌握好反转链表的技巧对解决其他链表问题非常重要。
