# Search in a Binary Search Tree

[[binary-search-tree]] [[tree]] [[dfs]]

## Problem Description

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

### Examples

**Example 1:**

```text
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Tree structure:
    4
   / \
  2   7
 / \
1   3

Search for 2 returns subtree rooted at 2
```

**Example 2:**

```text
Input: root = [4,2,7,1,3], val = 5
Output: []

No node with value 5 found
```

### Constraints

- The number of nodes in the tree is in the range `[1, 5000]`
- `1 <= Node.val <= 10^7`
- root is a binary search tree
- `1 <= val <= 10^7`

---

## 解法一：递归（利用BST性质）

```python
from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        利用二叉搜索树性质递归查找

        BST性质：
        - 左子树所有节点值 < 根节点值
        - 右子树所有节点值 > 根节点值

        因此可以在O(logn)时间内定位到目标节点
        """
        # 基础情况：找到或搜索完毕
        if not root or root.val == val:
            return root

        # 利用BST性质：根据大小关系决定搜索方向
        if val < root.val:
            # 目标值更小，搜索左子树
            return self.searchBST(root.left, val)
        else:
            # 目标值更大，搜索右子树
            return self.searchBST(root.right, val)
```

**算法分析：**

- **时间复杂度**：O(log n) - 平衡BST；O(n) - 退化为链表
- **空间复杂度**：O(h) - 递归栈深度，h为树高

| 项目 | 值 |
|------|-----|
| 最佳情况 | O(log n) |
| 最坏情况 | O(n) |
| 平均情况 | O(log n) |

---

## 解法二：迭代（更优的空间使用）

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        使用迭代方式搜索，避免递归栈

        与递归逻辑相同，但不占用调用栈空间
        """
        current = root

        while current:
            if current.val == val:
                return current
            elif val < current.val:
                # 左子树
                current = current.left
            else:
                # 右子树
                current = current.right

        # 未找到
        return None
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(log n) - 平均；O(n) - 最坏 |
| 空间复杂度 | O(1) |

---

## 两种方法对比

| 方面 | 递归 | 迭代 |
|------|------|------|
| 代码简洁性 | ✅ 更简洁 | ❌ 略冗长 |
| 空间复杂度 | O(h) | **O(1)** |
| 栈溢出风险 | 有（深树） | 无 |
| 运行速度 | 略慢 | **更快** |
| 易读性 | ✅ 好 | ✅ 好 |

---

## 执行流程演示

```text
树结构：
    4
   / \
  2   7
 / \
1   3

查找 val = 2：
第1步：current = 4, 2 < 4，向左
第2步：current = 2, 2 == 2，找到！✓
返回以2为根的子树：
  2
 / \
1   3

查找 val = 5：
第1步：current = 4, 5 > 4，向右
第2步：current = 7, 5 < 7，向左
第3步：current = None，查找完毕
返回 None
```

---

## BST性质应用

**为什么BST查询这么快？**

- 普通二叉树：需要遍历所有节点，O(n)
- 二叉搜索树：每次比较时消除一半的搜索空间，O(log n)
- 原理：类似于二分查找

```text
比对过程：
val=2 vs root=4  →  2 < 4  →  去左子树（已排除右子树）
val=2 vs node=2  →  2 == 2 →  找到！
```

---

## 相关题目

- [701. Insert into a Binary Search Tree](701_insert_into_a_binary_search_tree.md) - 二叉搜索树中的插入操作
- [450. Delete Node in a BST](450_delete_node_in_a_bst.md) - 删除二叉搜索树中的节点
- [230. Kth Smallest Element in a BST](230_kth_smallest_element_in_a_bst.md) - 二叉搜索树中第K小的元素
- [235. Lowest Common Ancestor of a BST](235_lowest_common_ancestor_of_a_bst.md) - 二叉搜索树的最近公共祖先
