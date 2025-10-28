# Copy List with Random Pointer

[[linkedlist]] [[hashtable]]

## Problem Description

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a **deep copy** of the list. The deep copy should consist of exactly `n` **new nodes**, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list.**

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return *the head of the copied linked list*.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

## Examples

**Example 1:**

![example 1](https://assets.leetcode.com/uploads/2019/12/18/e1.png)

```text
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**Example 2:**

![example 2](https://assets.leetcode.com/uploads/2019/12/18/e2.png)

```text
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

**Example 3:**

![example 3](https://assets.leetcode.com/uploads/2019/12/18/e3.png)

```text
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

## Constraints

- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is null or is pointing to some node in the linked list.

## 解法一：哈希表映射（推荐）

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        """
        使用哈希表建立原节点到新节点的映射
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        if not head:
            return None
        
        # 建立原节点到新节点的映射
        d = {}
        
        # 第一遍遍历：创建所有新节点
        current = head
        while current:
            d[current] = Node(current.val)
            current = current.next
        
        # 第二遍遍历：建立新节点之间的连接关系
        current = head
        while current:
            # 设置next指针
            d[current].next = d.get(current.next)
            # 设置random指针
            d[current].random = d.get(current.random)
            current = current.next
        
        return d[head]
```

### 算法思路

**核心思想**：使用哈希表建立原节点与新节点的一一对应关系。

**算法步骤**：

1. **第一次遍历**：为每个原节点创建对应的新节点，存储在哈希表中
2. **第二次遍历**：根据原节点的指针关系，设置新节点的`next`和`random`指针
3. **返回结果**：返回新链表的头节点

**为什么需要两次遍历？**

- 第一次遍历时，只能确保当前节点的新节点存在
- 无法保证`random`指向的节点的新节点已经创建
- 第二次遍历时，所有新节点都已存在，可以安全地建立指针关系

**复杂度分析**：

- 时间复杂度：O(n) - 两次遍历链表
- 空间复杂度：O(n) - 哈希表存储n个节点映射

## 解法二：原地复制法（O(1)空间）

```python
class Solution:
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        """
        原地复制法：在原链表基础上构建新节点
        时间复杂度：O(n)，空间复杂度：O(1)
        """
        if not head:
            return None
        
        # 第一步：在每个原节点后插入对应的新节点
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # 第二步：设置新节点的random指针
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # 第三步：分离两个链表
        current = head
        new_head = head.next
        new_current = new_head
        
        while current:
            current.next = new_current.next
            current = current.next
            if current:
                new_current.next = current.next
                new_current = new_current.next
        
        return new_head
```

### 核心思想

**核心思想**：在原链表的每个节点后面插入对应的新节点，形成交替的链表结构。

### 算法演示

以链表 `A -> B -> C` 为例（省略random指针）：

```text
原始链表: A -> B -> C -> null

第一步：插入新节点
A -> A' -> B -> B' -> C -> C' -> null

第二步：设置random指针
如果 A.random = C，则 A'.random = C'
（因为 C.next = C'）

第三步：分离链表
原链表: A -> B -> C -> null
新链表: A' -> B' -> C' -> null
```

**算法优势**：

1. **空间效率**：不需要额外的哈希表，空间复杂度O(1)
2. **巧妙设计**：利用原链表结构存储映射关系
3. **三步清晰**：插入、连接、分离三个步骤逻辑清晰

**复杂度分析**：

- 时间复杂度：O(n) - 三次遍历链表
- 空间复杂度：O(1) - 只使用常数额外空间（不包括输出空间）

## 解法三：递归+哈希表

```python
class Solution:
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        """
        递归方法结合哈希表
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        self.node_map = {}
        
        def copy_node(node):
            if not node:
                return None
            
            # 如果已经复制过，直接返回
            if node in self.node_map:
                return self.node_map[node]
            
            # 创建新节点
            new_node = Node(node.val)
            self.node_map[node] = new_node
            
            # 递归复制next和random指针
            new_node.next = copy_node(node.next)
            new_node.random = copy_node(node.random)
            
            return new_node
        
        return copy_node(head)
```

**复杂度分析**：

- 时间复杂度：O(n) - 每个节点访问一次
- 空间复杂度：O(n) - 递归栈和哈希表

## 算法对比

| 解法 | 时间复杂度 | 空间复杂度 | 特点 |
|------|------------|------------|------|
| 哈希表映射 | O(n) | O(n) | 思路简单，易于理解 |
| 原地复制法 | O(n) | O(1) | 空间最优，技巧性强 |
| 递归方法 | O(n) | O(n) | 代码简洁，但栈深度较大 |

## 边界情况处理

1. **空链表**：直接返回null
2. **单节点链表**：正确处理random指针
3. **random指向自身**：确保指向新节点自身
4. **random为null**：新节点的random也为null

## 关键要点

1. **深拷贝理解**：新链表的所有指针都应指向新节点
2. **映射关系**：建立原节点与新节点的对应关系是关键
3. **指针处理**：正确处理next和random两种指针
4. **空间优化**：原地复制法展示了巧妙的空间优化技巧

## 常见错误

1. **浅拷贝**：新节点的指针指向原链表节点
2. **映射遗漏**：没有为所有节点建立映射关系
3. **指针混乱**：在原地复制法中错误地修改了指针
4. **边界处理**：没有正确处理null指针的情况

## 算法扩展

1. **如果链表很大怎么办？** - 考虑分批处理或流式处理
2. **如果要求保持原链表不变？** - 哈希表方法更合适
3. **如果有环怎么办？** - 需要额外的环检测逻辑

## 相关题目

- [133. Clone Graph](133_clone_graph.md) - 克隆图
- [1485. Clone Binary Tree With Random Pointer](1485_clone_binary_tree_with_random_pointer.md) - 克隆含随机指针的二叉树
- [1490. Clone N-ary Tree](1490_clone_n_ary_tree.md) - 克隆N叉树

这道题是链表和哈希表的经典结合，展示了如何处理复杂的指针关系和深拷贝问题。
