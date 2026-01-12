# Insert into a Binary Search Tree

[[bst]] [[tree]] [[dfs]]

## Problem Description

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion.

It is guaranteed that the new value does not exist in the original BST.

**Note:** There may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

### Examples

**Example 1:**

```text
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

Tree structure:
    4              4
   / \            / \
  2   7    =>    2   7
 / \           / \   /
1   3         1   3 5
```

**Example 2:**

```text
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Insertion point: as right child of 20
```

**Example 3:**

```text
Input: root = [], val = 5
Output: [5]

Empty tree, create new node
```

### Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`
- `-10^8 <= Node.val <= 10^8`
- All values in the tree are unique
- `-10^8 <= val <= 10^8`
- It is guaranteed that val does not exist in the original BST

---

## 解法一：递归（最简洁）

```python
from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        利用BST性质递归插入新值

        思路：
        1. 如果当前节点为空，创建新节点
        2. 根据BST性质，比较val与root.val
        3. 递归到适当的子树进行插入
        """
        # 基础情况：到达叶子节点，创建新节点
        if not root:
            return TreeNode(val)

        # 根据BST性质决定插入方向
        if val < root.val:
            # 新值更小，插入到左子树
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            # 新值更大，插入到右子树
            root.right = self.insertIntoBST(root.right, val)
        # val == root.val 时什么都不做（题目保证不会出现）

        return root
```

**算法分析：**

- **时间复杂度**：O(log n) - 平衡树；O(n) - 退化为链表
- **空间复杂度**：O(h) - 递归栈深度

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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        使用迭代方式插入，避免递归栈

        思路：
        1. 如果树为空，直接返回新节点
        2. 从根节点开始，根据值的大小找到插入位置
        3. 在合适的位置创建新节点
        """
        # 处理空树的情况
        if not root:
            return TreeNode(val)

        current = root

        # 遍历找到插入位置
        while current:
            if val < current.val:
                # 应该插入左子树
                if not current.left:
                    current.left = TreeNode(val)
                    break
                current = current.left
            else:
                # 应该插入右子树
                if not current.right:
                    current.right = TreeNode(val)
                    break
                current = current.right

        return root
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

### 递归方式

```text
树结构：
    4
   / \
  2   7
 / \
1   3

插入 val = 5：

第1层：5 > 4，递归到右子树
  return 4, right = insertIntoBST(7, 5)

第2层：5 < 7，递归到左子树
  return 7, left = insertIntoBST(None, 5)

第3层：None，创建新节点TreeNode(5)
  return TreeNode(5)

最终结构：
    4
   / \
  2   7
 / \ /
1  3 5
```

### 迭代方式

```text
初始：current = 4

第1步：5 > 4，current = 7
第2步：5 < 7，7.left = None，插入
  7.left = TreeNode(5)
  结束

返回原root，结构完成
```

---

## 关键点剖析

### BST插入的规则

```text
1. 新值 < 节点值  →  插入到左子树
2. 新值 > 节点值  →  插入到右子树
3. 新值 == 节点值 →  不存在（题目保证）
```

### 为什么两种方式都正确？

BST的特性决定了插入位置是唯一的（对于任意给定的值），因此：

- 递归一直下探，直到找到空位
- 迭代也是一直下探，直到找到空位
- 两者结果相同

### 插入后仍然保持BST性质

因为：

- 新节点总是插入在**叶子位置**
- 比所有祖先更符合大小关系
- 不改变原有的BST结构

---

## 与搜索和删除的对比

| 操作 | 时间复杂度 | 空间复杂度 | 难度 |
|------|-----------|-----------|------|
| 搜索 | O(log n) | O(1) 迭代 / O(h) 递归 | 易 |
| **插入** | O(log n) | O(1) 迭代 / O(h) 递归 | 易 |
| 删除 | O(log n) | O(1) 迭代 / O(h) 递归 | 难 |

---

## 相关题目

- [700. Search in a Binary Search Tree](700_search_in_a_binary_search_tree.md) - 在二叉搜索树中搜索
- [450. Delete Node in a BST](450_delete_node_in_a_bst.md) - 删除二叉搜索树中的节点
- [98. Validate Binary Search Tree](098_validate_binary_search_tree.md) - 验证二叉搜索树
- [230. Kth Smallest Element in a BST](230_kth_smallest_element_in_a_bst.md) - 二叉搜索树中第K小的元素
