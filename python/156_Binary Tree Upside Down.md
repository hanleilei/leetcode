# 156. Binary Tree Upside Down

[[tree]]

## 问题描述

Given the `root` of a binary tree, turn the tree upside down and
return the new root.

You can turn a binary tree upside down with the following steps:

1. The original left child becomes the new root.
2. The original root becomes the new right child.
3. The original right child becomes the new left child.

The mentioned steps are done level by level. It is guaranteed that
every right node has a sibling (a left node with the same parent)
and has no children.

## 示例

**Example 1:**

```text
Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]
```

可视化：

```text
原树：               翻转后：
      1                  4
     / \                / \
    2   3              5   2
   / \                    / \
  4   5                  3   1
```

**Example 2:**

```text
Input: root = []
Output: []
```

**Example 3:**

```text
Input: root = [1]
Output: [1]
```

## 约束条件

- The number of nodes in the tree will be in the range `[0, 10]`
- $1 \le \text{Node.val} \le 10$
- Every right node in the tree has a sibling (a left node that
  shares the same parent)
- Every right node in the tree has no children

## 解法

### 方法1：迭代（模拟链表反转）推荐

将二叉树看作链表，沿着左子树一路向下，同时记录父节点和父节点的
右子节点，逐步构建新树。

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        迭代法：模拟链表反转

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        parent = None           # 父节点
        parent_right = None     # 父节点的右子节点

        while root:
            # 保存当前节点的左子节点
            root_left = root.left

            # 重新连接：
            # 1. 当前节点的左子 = 父节点的右子
            root.left = parent_right

            # 2. 保存当前节点的右子节点（下一轮要用）
            parent_right = root.right

            # 3. 当前节点的右子 = 父节点
            root.right = parent

            # 4. 更新父节点为当前节点
            parent = root

            # 5. 移动到左子节点
            root = root_left

        return parent
```

### 方法2：递归

递归到最左下节点作为新根，然后逐层构建新树。

```python
from typing import Optional

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        递归法

        时间复杂度：O(n)
        空间复杂度：O(h) h为树高
        """
        if not root or not root.left:
            return root

        # 递归到最左下节点，它将成为新根
        new_root = self.upsideDownBinaryTree(root.left)

        # 重新连接：
        # root.left 成为父节点
        # root.left.left = root.right (原右子变成新左子)
        root.left.left = root.right

        # root.left.right = root (原根变成新右子)
        root.left.right = root

        # 断开原连接
        root.left = None
        root.right = None

        return new_root
```

### 方法3：递归（带辅助函数）

使用辅助函数返回新根和当前层的父节点。

```python
from typing import Optional, Tuple

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        递归法（带辅助函数）

        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        def helper(node: Optional[TreeNode]) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
            """
            返回：(新根, 当前子树的父节点)
            """
            if not node:
                return None, None

            if not node.left:
                return node, node

            # 递归处理左子树
            new_root, parent = helper(node.left)

            # 重新连接
            parent.left = node.right
            parent.right = node

            # 断开原连接
            node.left = None
            node.right = None

            return new_root, node

        new_root, _ = helper(root)
        return new_root
```

## 算法分析

### 核心思想详解

这道题的关键在于理解"翻转"的本质：

**原始结构**（沿着左子树向下）：

```text
1 (root)
├─ left: 2
│  ├─ left: 4
│  └─ right: 5
└─ right: 3
```

**翻转后**（原左子树的最左节点成为新根）：

```text
4 (new root)
├─ left: 5 (原2的右子)
└─ right: 2
   ├─ left: 3 (原1的右子)
   └─ right: 1
```

**变换规则**：

对于每个节点：

1. `node.left` → 新的父节点
2. `node.right` → 成为父节点的左子
3. `node` 本身 → 成为父节点的右子

**迭代法的关键**：

模拟链表反转，需要维护三个指针：

- `root`：当前节点
- `parent`：父节点（将成为当前节点的右子）
- `parent_right`：父节点的右子（将成为当前节点的左子）

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 迭代 | O(n) | O(1) | 最优解 |
| 递归 | O(n) | O(h) | 代码简洁 |
| 递归+辅助 | O(n) | O(h) | 易理解 |

其中 n 是节点数，h 是树的高度（最多为 n）。

### 执行过程示例

以 `root = [1,2,3,4,5]` 为例：

```text
原树：
      1
     / \
    2   3
   / \
  4   5
```

**迭代法执行过程：**

初始状态：

```text
root = 1, parent = None, parent_right = None
```

**Iteration 1**：处理节点 1

```text
root_left = 2
root.left = None (parent_right)
parent_right = 3
root.right = None (parent)
parent = 1
root = 2

节点1变为：1 (left=None, right=None)
```

**Iteration 2**：处理节点 2

```text
root_left = 4
root.left = 3 (parent_right)
parent_right = 5
root.right = 1 (parent)
parent = 2
root = 4

节点2变为：
    2
   / \
  3   1
```

**Iteration 3**：处理节点 4

```text
root_left = None
root.left = 5 (parent_right)
parent_right = None
root.right = 2 (parent)
parent = 4
root = None

节点4变为：
      4
     / \
    5   2
       / \
      3   1
```

循环结束，返回 `parent = 4`。

**递归法执行过程：**

```text
upsideDown(1):
├─ upsideDown(2):
│  └─ upsideDown(4):
│     └─ return 4 (最左下节点)
│  
│  处理节点2：
│  2.left.left = 2.right  → 4.left = 5
│  2.left.right = 2       → 4.right = 2
│  断开2的连接
│  return 4
│
│ 处理节点1：
│ 1.left.left = 1.right  → 2.left = 3
│ 1.left.right = 1       → 2.right = 1
│ 断开1的连接
│ return 4

最终树：
      4
     / \
    5   2
       / \
      3   1
```

## 常见错误

### 错误1：忘记保存节点的子节点

```python
# 错误：直接修改root.left，丢失了原左子节点
while root:
    root.left = parent_right  # 丢失了root.left
    root = root.left  # 错误！root.left已被修改

# 正确：先保存
while root:
    root_left = root.left  # 先保存
    root.left = parent_right
    root = root_left  # 使用保存的值
```

### 错误2：更新顺序错误

```python
# 错误：先更新parent，导致后续使用错误的值
root.right = parent
parent = root
root.left = parent_right  # 此时parent已经被改变

# 正确：按正确顺序更新
root.left = parent_right
root.right = parent
parent = root
```

### 错误3：递归时忘记断开原连接

```python
# 错误：没有断开原连接，导致环
root.left.left = root.right
root.left.right = root
return new_root  # root仍连接着原子树

# 正确：断开连接
root.left.left = root.right
root.left.right = root
root.left = None   # 断开
root.right = None  # 断开
return new_root
```

### 错误4：边界条件处理不当

```python
# 错误：没有检查root.left是否存在
if not root:
    return root
new_root = self.upsideDownBinaryTree(root.left)  # 可能为None

# 正确：检查是否有左子
if not root or not root.left:
    return root
```

### 错误5：混淆左右子树

```python
# 错误：搞反了左右
root.left.right = root.right  # 错
root.left.left = root         # 错

# 正确：
root.left.left = root.right   # 原右子→新左子
root.left.right = root        # 原根→新右子
```

### 错误6：返回错误的节点

```python
# 错误：返回原root（已被修改）
while root:
    ...
return root  # root已经是None了

# 正确：返回parent（最后处理的节点）
while root:
    ...
return parent
```

## 相关题目

- [0156. Binary Tree Upside Down](./156_Binary Tree Upside Down.md)
- [0206. Reverse Linked List](./206_reverse_linked_list.md) - 链表反转（类似思想）
- [0226. Invert Binary Tree](./226_invert_binary_tree.md) - 翻转二叉树
- [0114. Flatten Binary Tree to Linked List](./114_flatten_binary_tree_to_linked_list.md) - 展开为链表
- [0025. Reverse Nodes in k-Group](./025_reverse_node_in_k_group.md) - K组反转
