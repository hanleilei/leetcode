# 617. Merge Two Binary Trees

## 问题描述

You are given two binary trees `root1` and `root2`.

Imagine that when you put one of them to cover the other, some
nodes of the two trees are overlapped while the others are not. You
need to merge the two trees into a new binary tree. The merge rule
is that if two nodes overlap, then sum node values up as the new
value of the merged node. Otherwise, the NOT null node will be used
as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both
trees.

## 示例

**Example 1:**

```text
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
```

可视化：

```text
    Tree 1          Tree 2          Merged
      1               2               3
     / \             / \             / \
    3   2           1   3           4   5
   /                 \   \         / \   \
  5                   4   7       5   4   7
```

**Example 2:**

```text
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
```

## 约束条件

- The number of nodes in both trees is in the range `[0, 2000]`
- $-10^4 \le \text{Node.val} \le 10^4$

## 解法

### 方法1：递归 DFS 推荐

使用递归深度优先遍历同时遍历两棵树，根据节点存在情况创建新树。

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        递归DFS合并两棵树

        时间复杂度：O(min(m, n))
        空间复杂度：O(min(h1, h2))
        """
        # Base case 1: root1为空，返回root2
        if not root1:
            return root2

        # Base case 2: root2为空，返回root1
        if not root2:
            return root1

        # 递归：创建新节点，值为两节点之和
        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)

        return merged
```

### 方法2：迭代 BFS

使用队列进行层序遍历，同时处理两棵树。

```python
from typing import Optional
from collections import deque

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        迭代BFS合并

        时间复杂度：O(min(m, n))
        空间复杂度：O(min(m, n))
        """
        if not root1:
            return root2
        if not root2:
            return root1

        # 队列存储待处理的节点对
        queue = deque([(root1, root2)])

        while queue:
            node1, node2 = queue.popleft()

            # 合并当前节点的值
            node1.val += node2.val

            # 处理左子树
            if node1.left and node2.left:
                queue.append((node1.left, node2.left))
            elif not node1.left:
                node1.left = node2.left

            # 处理右子树
            if node1.right and node2.right:
                queue.append((node1.right, node2.right))
            elif not node1.right:
                node1.right = node2.right

        return root1
```

### 方法3：原地修改

直接修改 root1，避免创建新节点。

```python
from typing import Optional

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        原地修改root1

        时间复杂度：O(min(m, n))
        空间复杂度：O(min(h1, h2))
        """
        if not root1:
            return root2
        if not root2:
            return root1

        # 直接修改root1的值
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
```

## 算法分析

### 核心思想详解

合并两棵二叉树的关键在于同时遍历两棵树，根据节点存在情况：

1. **两个节点都存在**：创建新节点，值为两节点值之和
2. **只有一个节点存在**：直接使用该节点（及其子树）
3. **两个节点都不存在**：返回 None

递归的三种情况：

```python
if not root1:      # 情况1：root1为空
    return root2   # 返回root2（可能也为空）

if not root2:      # 情况2：root2为空
    return root1   # 返回root1

# 情况3：两个都存在，合并
return TreeNode(root1.val + root2.val, ...)
```

### 为什么递归如此简洁？

因为树的定义本身就是递归的：

- 树 = 根节点 + 左子树 + 右子树
- 合并树 = 合并根 + 合并左子树 + 合并右子树

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 递归DFS | O(min(m,n)) | O(min(h₁,h₂)) | 最优解 |
| 迭代BFS | O(min(m,n)) | O(min(m,n)) | 避免栈溢出 |
| 原地修改 | O(min(m,n)) | O(min(h₁,h₂)) | 节省空间 |

其中：

- m, n 是两棵树的节点数
- h₁, h₂ 是两棵树的高度
- 递归空间复杂度为递归栈深度
- BFS空间复杂度为队列最大长度（最坏情况下一层的节点数）

### 执行过程示例

以 `root1 = [1,3,2,5]`, `root2 = [2,1,3,null,4,null,7]` 为例：

初始状态：

```text
Tree 1:        Tree 2:
    1              2
   / \            / \
  3   2          1   3
 /                \   \
5                  4   7
```

**递归执行过程：**

```text
mergeTrees(1, 2):
├─ val = 1 + 2 = 3
├─ left = mergeTrees(3, 1):
│  ├─ val = 3 + 1 = 4
│  ├─ left = mergeTrees(5, null):
│  │  └─ 返回 5
│  └─ right = mergeTrees(null, 4):
│     └─ 返回 4
└─ right = mergeTrees(2, 3):
   ├─ val = 2 + 3 = 5
   ├─ left = mergeTrees(null, null):
   │  └─ 返回 null
   └─ right = mergeTrees(null, 7):
      └─ 返回 7

最终结果：
      3
     / \
    4   5
   / \   \
  5   4   7
```

**逐步可视化：**

Step 1：合并根节点 (1 + 2 = 3)

```text
      3
```

Step 2：合并左子树 (3 + 1 = 4)

```text
      3
     /
    4
```

Step 3：合并左子树的左子节点 (5 + null = 5)

```text
      3
     /
    4
   /
  5
```

Step 4：合并左子树的右子节点 (null + 4 = 4)

```text
      3
     /
    4
   / \
  5   4
```

Step 5：合并右子树 (2 + 3 = 5)

```text
      3
     / \
    4   5
   / \
  5   4
```

Step 6：合并右子树的右子节点 (null + 7 = 7)

```text
      3
     / \
    4   5
   / \   \
  5   4   7
```

## 常见错误

### 错误1：忘记处理空节点

```python
# 错误：没有检查空节点
def mergeTrees(self, r1, r2):
    return TreeNode(r1.val + r2.val, ...)  # r1或r2可能为None

# 正确：先处理边界条件
def mergeTrees(self, r1, r2):
    if not r1:
        return r2
    if not r2:
        return r1
    return TreeNode(r1.val + r2.val, ...)
```

### 错误2：只返回一方的值而非整个子树

```python
# 错误：只返回节点值，丢失子树
if not r1:
    return TreeNode(r2.val)  # 丢失了r2的子树

# 正确：返回整个子树
if not r1:
    return r2  # 保留完整子树结构
```

### 错误3：创建不必要的新节点

```python
# 错误：即使只有一棵树也创建新节点
if not r1:
    return TreeNode(r2.val, r2.left, r2.right)  # 浪费空间

# 正确：直接返回原节点
if not r1:
    return r2  # 复用现有节点
```

### 错误4：BFS中未检查子节点是否为空

```python
# 错误：直接加入队列
queue.append((node1.left, node2.left))  # 可能是(None, node)

# 正确：检查是否都存在
if node1.left and node2.left:
    queue.append((node1.left, node2.left))
elif not node1.left:
    node1.left = node2.left
```

### 错误5：递归时修改了原节点

```python
# 错误：修改了原树结构
root1.val += root2.val  # 改变了输入

# 正确：创建新节点
return TreeNode(root1.val + root2.val, ...)
```

### 错误6：混淆 None 和 0

```python
# 错误：认为空节点值为0
if not root1:
    return TreeNode(root2.val if root2 else 0)

# 正确：空节点就是None，不需要创建值为0的节点
if not root1:
    return root2
```

## 相关题目

- [0617. Merge Two Binary Trees](./617_Merge Two Binary Trees.md)
- [0226. Invert Binary Tree](./226_invert_binary_tree.md) - 树的递归修改
- [0104. Maximum Depth of Binary Tree](./104_maximum_depth_of_binary_tree.md) - 基础递归
- [0101. Symmetric Tree](./101_symmetric_tree.md) - 同时遍历两棵树
- [0100. Same Tree](./100_same_tree.md) - 树的比较
