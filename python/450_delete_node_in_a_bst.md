# Delete Node in a BST

[[tree]]

## Problem Description

Given a root node reference of a BST and a key, delete the node with the
given key. Return the root node reference (possibly updated).

Basically, the deletion can be divided into two stages:

1. Search for a node to remove
2. If the node is found, delete the node

**Note:** Time complexity should be O(height of tree) in the average case.

### Examples

**Example 1:**

```text
Input: root = [5,3,6,2,4,null,7], key = 3

Initial Tree:
    5
   / \
  3   6
 / \   \
2   4   7

One valid answer is [5,4,6,2,null,null,7]:
    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7]:
    5
   / \
  2   6
   \   \
    4   7
```

### Constraints

- The number of nodes in the tree is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- -10^5 <= key <= 10^5
- Each node's value is unique
- root is a valid binary search tree
- root might be null

---

## 解法1：用右子树最小值替换（推荐✨）

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    用右子树最小值替换被删除节点的方法
    
    删除情况分类：
    1. 节点是叶子 → 直接删除
    2. 节点只有一个子树 → 用子树替换
    3. 节点有两个子树 → 用右子树最小值替换
    """
    
    def deleteNode(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:
        """删除BST中的节点，平均O(log n)，最坏O(n)"""
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            min_node = self.get_min(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root
    
    def get_min(self, node: TreeNode) -> TreeNode:
        """找BST中的最小值节点（最左边）"""
        while node.left:
            node = node.left
        return node
```

### 解法思路

```text
删除节点的三种情况：

1️⃣ 叶子节点（没有子树）
   直接删除
   
2️⃣ 只有一个子树
   用子树替换当前节点
   
3️⃣ 有两个子树（最复杂）
   a) 找右子树最小值（最左节点）
   b) 用其值替换当前节点
   c) 递归删除右子树中的最小值节点
   
关键：保持BST性质（左 < 中 < 右）
```

| 项目 | 值 |
|------|-----|
| 时间复杂度 | O(log n) 平均，O(n) 最坏（退化成链表） |
| 空间复杂度 | O(h) - 递归栈 |
| 是否修改树结构 | 否，只修改节点值 |

---

## 解法2：用左子树最大值替换（替代✓）

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    用左子树最大值替换的方法
    
    与解法1对称，用左子树最大值代替右子树最小值
    """
    
    def deleteNode(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            max_node = self.get_max(root.left)
            root.val = max_node.val
            root.left = self.deleteNode(root.left, max_node.val)
        
        return root
    
    def get_max(self, node: TreeNode) -> TreeNode:
        """找BST中的最大值节点（最右边）"""
        while node.right:
            node = node.right
        return node
```

## 解法对比

| 方案 | 替换值来源 | 优势 | 树结构影响 |
|------|----------|------|----------|
| 解法1 | 右子树最小 | 常用，符合直觉 | 等价 |
| 解法2 | 左子树最大 | 对称设计，灵活 | 等价 |

两种方案都维持 BST 性质，选择其一即可。

---

## 算法分析

### 核心思路

删除 BST 中的节点需要保持 BST 的性质：**左 < 中 < 右**

```text
关键点：
1. 如果目标节点是叶子
   → 直接移除
   
2. 如果有一个子树为空
   → 用另一个子树替换它
   
3. 如果有两个子树
   → 用相邻值替换（中序遍历的前驱或后继）
   → 后继 = 右子树最小值
   → 前驱 = 左子树最大值
```

### 为什么这样工作？

```text
例：删除值为3的节点

情况3前：          情况3后（用后继4替换）：
    5                  5
   / \                / \
  3   6              4   6
 / \   \            / \   \
2   4   7          2  □   7

右子树最小值（4）= 比3大的最小值
满足 2 < 4 < 6 ✓ BST性质保持
```

### 复杂度分析

| 操作 | 平均情况 | 最坏情况 | 说明 |
|------|---------|---------|------|
| **搜索** | O(log n) | O(n) | 找到目标节点 |
| **获取min/max** | O(log n) | O(n) | 沿着一侧走 |
| **删除** | O(log n) | O(n) | 总体复杂度 |

**最坏情况：** 树退化成链表时，O(n)

---

## 执行流程示例

```text
删除节点3：root = [5,3,6,2,4,null,7], key = 3

步骤1：递归找节点
  3 < 5 → 递归左子树
  
步骤2：找到节点3，且有两个子树
  
步骤3：找右子树最小值
  右子树为6，最左节点无
  最小值 = 4
  
步骤4：替换
  3 → 4
  树变为 [5,4,6,2,?,null,7]
  
步骤5：删除右子树中的4
  root.right = deleteNode(6, 4)
  
结果：[5,4,6,2,null,null,7] ✓
```

---

## 常见错误

### 错误1：只修改值而不删除重复

```python
# ❌ 错误
root.val = min_node.val
# 问题：min_node还在树中，产生重复值
```

### 错误2：忘记递归处理子树

```python
# ❌ 错误
if key > root.val:
    self.deleteNode(root.right, key)  # 未赋值回去
    
# ✓ 正确
root.right = self.deleteNode(root.right, key)
```

### 错误3：混淆min/max

```python
# ❌ 用右子树最大值（违反BST性质）
max_node = self.get_max(root.right)

# ✓ 用右子树最小值（正确）
min_node = self.get_min(root.right)
```

### 错误4：未处理所有情况

```python
# ❌ 忽略了左子树存在的情况
if not root.right:
    return root.left
# 问题：没有处理右子树为空但左子树不空的情况

# ✓ 完整处理
if not root.left:
    return root.right
if not root.right:
    return root.left
# 然后处理都不为空的情况
```

---

## 相关题目

- [[98. Validate Binary Search Tree]] - 验证BST
- [[700. Search in a Binary Search Tree]] - BST查询
- [[701. Insert into a Binary Search Tree]] - BST插入
- [[235. Lowest Common Ancestor of a BST]] - BST最近公共祖先
- [[108. Convert Sorted Array to Binary Search Tree]] - 有序数组转BST
