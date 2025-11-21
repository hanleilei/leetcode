# Rotate List

[[linkedlist]]

Given the head of a linked list, rotate the list to the right by k places.

## Examples

### Example 1

```text
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

原链表: 1 -> 2 -> 3 -> 4 -> 5
右旋2位: 4 -> 5 -> 1 -> 2 -> 3
```

### Example 2

```text
Input: head = [0,1,2], k = 4
Output: [2,0,1]

原链表: 0 -> 1 -> 2
k=4, 但链表长度为3，所以 k % 3 = 1
右旋1位: 2 -> 0 -> 1
```

## Constraints

- The number of nodes in the list is in the range [0, 500]
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 10^9

## 解题思路

核心思想是将链表首尾相连形成环，然后在合适的位置断开。

### 算法步骤

1. **边界处理**: 空链表直接返回 None
2. **计算链表长度**: 遍历链表获得长度 n，同时记录尾节点位置
3. **优化 k 值**: 由于旋转 n 次等于不旋转，所以 `k = k % n`
4. **形成环形链表**: 将尾节点的 next 指向头节点
5. **找到断开点**: 从尾节点开始走 `n - k` 步找到新的尾节点
6. **断开环形**: 设置新头节点，断开环形结构

### 可视化解释

以 `[1,2,3,4,5], k=2` 为例：

```text
步骤1: 原链表
1 -> 2 -> 3 -> 4 -> 5 -> NULL
                    ↑
                    p (尾节点)

步骤2: 形成环形链表 (p.next = head)
1 -> 2 -> 3 -> 4 -> 5
↑              ↑    |
head           p    |
↑____________________

步骤3: 移动 n-k=3 步找断开点
1 -> 2 -> 3 -> 4 -> 5
↑         ↑         |
head      p         |
↑____________________

步骤4: 断开环形，设置新头节点
     4 -> 5 -> 1 -> 2 -> 3 -> NULL
     ↑              ↑
   new head    断开点 (p.next = None)
```

### 复杂度分析

- **时间复杂度**: O(n) - 需要遍历链表两次（计算长度 + 找断开点）
- **空间复杂度**: O(1) - 只使用常数额外空间

## 解法一：环形链表法（推荐）

```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 边界处理
        if not head or not head.next or k == 0:
            return head

        # 1. 计算链表长度，同时找到尾节点
        p = dummy = ListNode(0)
        dummy.next = head
        n = 0
        while p.next:
            p = p.next
            n += 1
        
        # 2. 优化 k 值
        k = k % n
         # 3. 形成环形链表
        p.next = head # 问题的关键：构造一个环形链表，首尾相接

        # 4. 找到新的尾节点（从尾节点走 n-k 步）
        for _ in range(n - k):
            p = p.next
        
        # 5. 设置新头节点并断开环形
        head = p.next
        p.next = None
        return head
```

## 解法二：双指针法

```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # 计算链表长度
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        k = k % length
        if k == 0:
            return head
        
        # 快慢指针找到断开点
        fast = slow = head
        
        # 快指针先走 k 步
        for _ in range(k):
            fast = fast.next
        
        # 同时移动，直到快指针到达尾节点
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # 重新连接
        new_head = slow.next
        slow.next = None
        fast.next = head
        
        return new_head
```

## 关键要点

1. **取模优化**: `k % n` 避免不必要的旋转
2. **环形思维**: 形成环再断开，思路更清晰
3. **边界处理**: 注意空链表、单节点、k=0 等情况
4. **指针操作**: 小心断开和重新连接的顺序

## 相关题目

- [206. Reverse Linked List](../206_reverse_linked_list.md)
- [234. Palindrome Linked List](../234_palindrome_linked_list.md)
- [143. Reorder List](../143_reorder_list.md)

经典问题，使用快慢指针就可以，由于k可能非常大，但是k如果大于链表长度，就会做重复的工作，所以先要得到链表长度，然后取模。

```cpp
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) return head;
        ListNode* root = new ListNode(-1, head);
        int n = 0;
        ListNode* tail = root;
        while (tail-> next){
            tail = tail->next;
            n++;
        }
        k %= n;
        int step = n - k;
        ListNode* kNode = root;
        while (step --){
            kNode = kNode->next;
        }
        tail->next = root->next;
        root->next = kNode->next;
        kNode->next = nullptr;
        return root->next;
    }
};
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        root = ListNode(-1, head)
        n = 0
        tail = root
        while tail.next:
            tail = tail.next
            n += 1
        
        k %= n
        step = n - k
        knode = root
        for _ in range(step):
            knode = knode.next
        
        tail.next = root.next
        root.next = knode.next
        knode.next = None
        return root.next
```
