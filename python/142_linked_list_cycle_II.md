# Linked List Cycle II

[[linkedlist]] [[2points]] 

Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

**Note**: Do not modify the linked list.

## Examples

### Example 1

```text
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

链表结构：
3 → 2 → 0 → -4
    ↑_________|

环的起始节点是索引为1的节点（值为2）
```

### Example 2

```text
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

链表结构：
1 → 2
↑___|

环的起始节点是索引为0的节点（值为1）
```

### Example 3

```text
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

## Constraints

- The number of the nodes in the list is in the range `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked-list

## Follow up

Can you solve it using O(1) (i.e. constant) memory?

## 解题思路

这道题是 [141. Linked List Cycle](141_linked_list_cycle.md) 的扩展，不仅要判断是否有环，还要找到环的起始节点。

### 核心思想：Floyd判圈算法（龟兔赛跑）

1. **第一阶段**：使用快慢指针判断是否有环
   - 慢指针每次走1步，快指针每次走2步
   - 如果有环，快慢指针必定会相遇

2. **第二阶段**：找到环的起始节点
   - 将一个指针重新指向head
   - 两个指针以相同速度前进，相遇点就是环的起始节点

### 数学原理

假设：

- 链表头到环起点的距离为 `a`
- 环起点到相遇点的距离为 `b`  
- 相遇点到环起点的距离为 `c`

当快慢指针相遇时：

- 慢指针走过的距离：`a + b`
- 快指针走过的距离：`a + b + c + b = a + 2b + c`

由于快指针速度是慢指针的2倍：

```text
2(a + b) = a + 2b + c
2a + 2b = a + 2b + c
a = c
```

**关键发现**：从链表头到环起点的距离 = 从相遇点到环起点的距离

## 解法一：Floyd判圈算法（推荐）

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        使用Floyd判圈算法（龟兔赛跑）
        时间复杂度：O(n)，空间复杂度：O(1)
        """
        if not head or not head.next:
            return None
        
        # 第一阶段：判断是否有环
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # 如果没有环，返回None
        if not fast or not fast.next:
            return None
        
        # 第二阶段：找到环的起始节点
        # 将慢指针重新指向头节点
        slow = head
        # 快慢指针以相同速度前进，相遇点就是环起点
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
```

**复杂度分析**：

- 时间复杂度：O(n) - 最多遍历链表两次
- 空间复杂度：O(1) - 只使用常数额外空间

## 解法二：哈希表法

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        使用集合记录访问过的节点
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return current
            visited.add(current)
            current = current.next
        
        return None
```

**复杂度分析**：

- 时间复杂度：O(n) - 遍历链表一次
- 空间复杂度：O(n) - 最坏情况需要存储所有节点

## 解法三：字典法（变体）

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        使用字典记录节点
        """
        if not head:
            return None
        
        visited = {}
        current = head
        
        while current:
            if current in visited:
                return current
            visited[current] = True
            current = current.next
        
        return None
```

## 算法可视化

以 `[3,2,0,-4]` pos=1 为例：

```text
步骤1：快慢指针检测环
3 → 2 → 0 → -4
    ↑_________|

slow: 3 → 2 → 0 → -4 → 2 → 0 → -4 → 2 (在节点2相遇)
fast: 3 → 0 → 2 → -4 → 0 → 2 (在节点2相遇)

步骤2：寻找环起点
slow从head开始: 3 → 2
fast从相遇点开始: 2 → 0 → -4 → 2
在节点2相遇，这就是环的起点
```

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| Floyd算法 | O(n) | O(1) | 最优解，面试推荐 |
| 哈希表法 | O(n) | O(n) | 思路直观，易理解 |
| 字典法 | O(n) | O(n) | 哈希表的变体 |

## 关键要点

1. **Floyd算法的精髓**：利用数学原理，从链表头到环起点的距离等于从相遇点到环起点的距离
2. **两阶段处理**：先检测环的存在，再定位环的起点
3. **边界条件**：空链表或单节点链表的处理
4. **指针操作**：快慢指针的正确移动和终止条件

## 相关题目

- [141. Linked List Cycle](141_linked_list_cycle.md) - 判断链表是否有环
- [287. Find the Duplicate Number](287_find_duplicate_number.md) - 寻找重复数（Floyd算法应用）
- [202. Happy Number](202_happy_number.md) - 快乐数（类似的环检测问题）

这道题是链表算法的经典问题，Floyd判圈算法是必须掌握的重要技巧，在多个问题中都有应用。
