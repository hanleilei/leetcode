# Binary Tree Inorder Traversal

[[tree]] [[stack]] [[dfs]]

## Problem Description

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder traversal means: Left → Node → Right (对于二叉搜索树，中序遍历得到有序序列)

### Examples

**Example 1:**

```text
Given binary tree:
   1
    \
     2
    /
   3

Output: [1, 3, 2]

Explanation:
- Traverse left subtree: 1 (no left child)
- Visit node 1: append 1
- Traverse right subtree:
  - Go to node 2
  - Node 2 has left child 3
  - Traverse left: visit 3 → append 3
  - Visit node 2: append 2
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

### Constraints

- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

---

## 解法一：递归（最简洁）

```python
from typing import Optional, List

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        递归方式进行中序遍历：左 → 中 → 右

        时间复杂度：O(n) - 每个节点访问一次
        空间复杂度：O(h) - 递归栈深度，h为树高
        """
        result = []

        def dfs(node):
            if not node:
                return

            # 遍历左子树
            dfs(node.left)
            # 访问当前节点
            result.append(node.val)
            # 遍历右子树
            dfs(node.right)

        dfs(root)
        return result
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n) |
| 空间复杂度 | O(h) - 递归栈 |

---

## 解法二：迭代+栈（通用模板）

```python
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        使用栈模拟递归，进行迭代中序遍历

        核心思想：
        1. 一直向左走，将节点压入栈
        2. 当左子树走尽，弹出栈顶节点（访问）
        3. 转向右子树，重复步骤1
        """
        res = list()
        stack = list()

        while root or stack:
            # 步骤1：一直向左走，压入栈
            while root:
                stack.append(root)
                root = root.left
            # 步骤2：左子树已处理，弹出栈顶
            root = stack.pop()
            res.append(root.val)
            # 步骤3：处理右子树
            root = root.right
        return res
```

**执行流程图示：**

```text
树结构：
    1
   / \
  2   3

执行过程：
初始：current=1, stack=[], result=[]

向左走：
  current=2, stack=[1]
  current=None, stack=[1,2]

弹出处理：
  pop 2, result=[2], current=None

转向右（2的右子树为空）：
  current=None, stack=[1]

弹出处理：
  pop 1, result=[2,1], current=3

处理右子树：
  current=3, stack=[]
  current=None, stack=[3]

弹出处理：
  pop 3, result=[2,1,3]
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n) |
| 空间复杂度 | O(h) |

---

## 解法三：Morris遍历（常数空间）

```python
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Morris遍历：空间复杂度O(1)的遍历方法

        核心思想：通过建立临时线索（指向后继节点），避免栈的使用
        类似于线索二叉树的遍历
        """
        result = []
        current = root

        while current:
            # 如果没有左子树，直接访问当前节点
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                # 找左子树的最右节点（中序后继）
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                # 建立线索
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    # 线索已建立，说明左子树遍历完毕
                    predecessor.right = None  # 消除线索
                    result.append(current.val)
                    current = current.right

        return result
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(n) |
| 空间复杂度 | O(1) |

---

## 三种遍历方式对比

| 方法 | 时间 | 空间 | 难度 | 优势 |
|------|------|------|------|------|
| 递归 | O(n) | O(h) | 易 | 代码简洁，好理解 |
| 迭代+栈 | O(n) | O(h) | 中 | 通用模板，易扩展 |
| Morris遍历 | O(n) | O(1) | 难 | 常数空间，面试加分 |

---

## 前中后序遍历对比

| 顺序 | 访问时机 | 递归代码 |
|------|----------|----------|
| **前序** | 左右前 | dfs左 → visit → dfs右 |
| **中序** | 左中右 | dfs左 → visit → dfs右 |
| **后序** | 左右后 | dfs左 → dfs右 → visit |

---

## 相关题目

- [144. Binary Tree Preorder Traversal](144_binary_tree_preorder_traversal.md) - 前序遍历
- [145. Binary Tree Postorder Traversal](145_binary_tree_postorder_traversal.md) - 后序遍历
- [102. Binary Tree Level Order Traversal](102_binary_tree_level_order_traversal.md) - 层序遍历
- [173. Binary Search Tree Iterator](173_binary_search_tree_iterator.md) - 二叉搜索树迭代器
