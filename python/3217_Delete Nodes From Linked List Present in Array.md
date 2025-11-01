# Delete Nodes From Linked List Present in Array

[[linkedlist]] [[hashtable]]

## Problem Description

You are given an array of integers `nums` and the head of a linked list. Return *the head of the modified linked list after removing all nodes from the linked list that have a value that exists in* `nums`.

## Examples

**Example 1:**

```text
Input: nums = [1,2,3], head = [1,2,3,4,5]
Output: [4,5]
```

Explanation: Remove the nodes with values 1, 2, and 3.

**Example 2:**

```text
Input: nums = [1], head = [1,2,1,2,1,2]
Output: [2,2,2]
```

Explanation: Remove the nodes with value 1.

**Example 3:**

```text
Input: nums = [5], head = [1,2,3,4]
Output: [1,2,3,4]
```

Explanation: No node has value 5.

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- All elements in `nums` are unique.
- The number of nodes in the given list is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`
- The input is generated such that there is at least one node in the linked list that has a value not present in `nums`.

## 解法一：虚拟头节点（最优解）

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # 将数组转换为集合以提高查询效率
        s = set(nums)
        
        # 创建虚拟头节点，简化边界处理
        dummy = ListNode(0, head)
        current = dummy
        
        # 遍历链表
        while current.next:
            if current.next.val in s:
                # 删除节点：跳过当前的next节点
                current.next = current.next.next
            else:
                # 保留节点，继续遍历
                current = current.next
        
        return dummy.next
```

**核心思想：**

- **集合转换**：O(1)的查询时间
- **虚拟头节点**：统一处理所有节点，包括头节点的删除
- **单指针遍历**：当删除节点时不移动指针，继续检查下一个节点
- **简化边界**：无需特殊处理删除头节点的情况

**时间复杂度：** O(n + m)，其中n是链表长度，m是nums长度
**空间复杂度：** O(m) - 用于存储集合

## 解法二：直接修改头节点

```python
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        
        # 处理头节点被删除的情况
        while head and head.val in s:
            head = head.next
        
        # 处理剩余节点
        current = head
        while current and current.next:
            if current.next.val in s:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
```

直接修改头指针，不需要虚拟节点，但需要分别处理头节点。

## 解法三：前驱指针法

```python
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        prev = None
        current = head
        
        while current:
            if current.val in nums_set:
                # 删除当前节点
                if prev:
                    prev.next = current.next
                else:
                    # 删除的是头节点
                    head = current.next
            else:
                # 保留当前节点
                prev = current
            
            current = current.next
        
        return head
```

使用前驱指针追踪上一个节点，适合对链表删除操作的理解。

## 算法对比

### 解法对比

| 方法 | 使用虚拟节点 | 边界处理 | 代码复杂度 |
|------|------------|---------|----------|
| 虚拟头节点 | ✅ | 统一 | ⭐ |
| 直接修改 | ❌ | 分离 | ⭐⭐ |
| 前驱指针 | ❌ | 复杂 | ⭐⭐⭐ |

### 为什么虚拟头节点最优？

1. **统一处理**：所有节点包括头节点都用同样方式处理
2. **代码简洁**：无需特殊处理边界情况
3. **易于维护**：逻辑清晰，不易出错

## 关键概念

### 删除链表节点的通用模式

```python
dummy = ListNode(0, head)
prev = dummy
current = head

while current:
    if should_delete(current):
        prev.next = current.next
    else:
        prev = current
    current = current.next

return dummy.next
```

### 为什么删除节点时指针不动？

```text
链表: 1 -> 2 -> 3 -> 4
     prev  curr

删除curr前：prev指向1，curr指向2
删除2后：prev.next指向3
此时prev仍指向1，curr自动指向下一个要检查的节点3
不移动prev是因为3也可能在nums中需要删除
```

## 相关题目

- [83. Remove Duplicates from Sorted List](083_remove_duplicate_from_sorted_list.md) - 删除排序链表中的重复元素
- [27. Remove Element](027_remove_element.md) - 移除元素
- [203. Remove Linked List Elements](203_remove_linked_list_elements.md) - 移除链表元素
