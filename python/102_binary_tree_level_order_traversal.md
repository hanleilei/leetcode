# 102. Binary Tree Level Order Traversal

[[tree]] [[bfs]] [[dfs]]

## 问题描述

Given the `root` of a binary tree, return the **level order traversal**
of its nodes' values. (i.e., from left to right, level by level).

## 示例

**Example 1:**

```text
    3
   / \
  9  20
    /  \
   15   7
```

```text
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Example 2:**

```text
Input: root = [1]
Output: [[1]]
```

**Example 3:**

```text
Input: root = []
Output: []
```

## 约束条件

- The number of nodes in the tree is in the range `[0, 2000]`
- $-1000 \le \text{Node.val} \le 1000$

## 解法

### 方法1：BFS（层序遍历）推荐

使用队列进行层序遍历，每次处理完一层的所有节点。

```python
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS 层序遍历

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            # 处理当前层的所有节点
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                # 将下一层节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result
```

### 方法2：BFS 简洁版

使用列表推导式，代码更简洁。

```python
from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS 简洁版

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if not root:
            return []

        result = []
        level = [root]

        while level:
            # 记录当前层的值
            result.append([node.val for node in level])

            # 构建下一层
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp

        return result
```

### 方法3：DFS 递归

使用深度优先搜索，记录每个节点的层级。

```python
from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        DFS 递归

        时间复杂度：O(n)
        空间复杂度：O(h) h 为树高
        """
        result = []

        def dfs(node: Optional[TreeNode], level: int) -> None:
            if not node:
                return

            # 如果是新的一层，创建新列表
            if len(result) == level:
                result.append([])

            # 将当前节点值加入对应层
            result[level].append(node.val)

            # 递归处理左右子树
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return result
```

### 方法4：BFS + 队列存储层级

队列中存储 `(节点, 层级)` 元组。

```python
from typing import List, Optional
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS + 层级标记

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if not root:
            return []

        result = []
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()

            # 如果是新的一层，创建新列表
            if len(result) == level:
                result.append([])

            result[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result
```

## 算法分析

### 核心思想详解

**BFS 层序遍历的关键**：

1. **队列**：使用队列存储每一层的节点
2. **层数控制**：通过 `len(queue)` 确定当前层的节点数量
3. **顺序处理**：从左到右依次处理每个节点

```python
# 每次循环处理一层
while queue:
    level_size = len(queue)  # 当前层的节点数
    level_nodes = []

    for _ in range(level_size):  # 只处理当前层
        node = queue.popleft()
        level_nodes.append(node.val)
        # 将子节点加入队列（下一层）
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

**DFS 递归的关键**：

通过 `level` 参数记录当前节点所在的层级，确保节点值被添加到
正确的层。

```python
def dfs(node, level):
    if len(result) == level:  # 新的一层
        result.append([])
    result[level].append(node.val)  # 加入对应层
```

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| BFS 标准版 | O(n) | O(n) | 最优解 |
| BFS 简洁版 | O(n) | O(n) | 代码简洁 |
| DFS 递归 | O(n) | O(h) | h为树高 |
| BFS + 层级 | O(n) | O(n) | 易理解 |

其中 n 是节点数，h 是树的高度。

空间复杂度说明：

- BFS：队列最多存储一层的节点，最坏情况 O(n)（完全二叉树最后一层）
- DFS：递归栈深度为树高，平衡树 O(log n)，斜树 O(n)

### 执行过程示例

以 `root = [3,9,20,null,null,15,7]` 为例：

```text
树结构：
    3
   / \
  9  20
    /  \
   15   7
```

BFS 执行过程：

| 步骤 | 队列 | 当前层 | result |
|------|------|--------|--------|
| 初始 | [3] | - | [] |
| 1 | [9,20] | [3] | [[3]] |
| 2 | [15,7] | [9,20] | [[3],[9,20]] |
| 3 | [] | [15,7] | [[3],[9,20],[15,7]] |

详细步骤：

**Step 1**：处理第 0 层

```text
queue = [3]
level_size = 1
处理节点 3：加入 [3]
  添加左子 9 到队列
  添加右子 20 到队列
result = [[3]]
queue = [9, 20]
```

**Step 2**：处理第 1 层

```text
queue = [9, 20]
level_size = 2
处理节点 9：加入 [9]（无子节点）
处理节点 20：加入 [20]
  添加左子 15 到队列
  添加右子 7 到队列
result = [[3], [9, 20]]
queue = [15, 7]
```

**Step 3**：处理第 2 层

```text
queue = [15, 7]
level_size = 2
处理节点 15：加入 [15]（无子节点）
处理节点 7：加入 [7]（无子节点）
result = [[3], [9, 20], [15, 7]]
queue = []
```

DFS 执行过程：

```text
dfs(3, level=0):  result = [[3]]
├─ dfs(9, level=1):  result = [[3], [9]]
│  ├─ dfs(None, level=2): return
│  └─ dfs(None, level=2): return
└─ dfs(20, level=1):  result = [[3], [9, 20]]
   ├─ dfs(15, level=2):  result = [[3], [9, 20], [15]]
   └─ dfs(7, level=2):   result = [[3], [9, 20], [15, 7]]
```

## 常见错误

### 错误1：没有检查空节点

```python
# 错误：root 为 None 时会出错
queue = deque([root])
while queue:
    node = queue.popleft()
    result.append(node.val)  # None.val 报错

# 正确：先检查
if not root:
    return []
```

### 错误2：混淆层的边界

```python
# 错误：没有记录层的大小，导致层混乱
while queue:
    node = queue.popleft()
    level_nodes.append(node.val)
    # 错误：直接加入队列，无法区分层

# 正确：用 level_size 控制
level_size = len(queue)
for _ in range(level_size):
    node = queue.popleft()
```

### 错误3：DFS 时忘记检查 result 长度

```python
# 错误：直接访问可能越界
result[level].append(node.val)  # IndexError

# 正确：先检查是否需要创建新层
if len(result) == level:
    result.append([])
result[level].append(node.val)
```

### 错误4：子节点处理不当

```python
# 错误：没有检查子节点是否为 None
queue.append(node.left)
queue.append(node.right)
# 会导致 None 进入队列

# 正确：检查后再加入
if node.left:
    queue.append(node.left)
if node.right:
    queue.append(node.right)
```

### 错误5：使用列表当队列

```python
# 错误：列表的 pop(0) 是 O(n)
queue = [root]
node = queue.pop(0)  # 慢

# 正确：使用 deque
from collections import deque
queue = deque([root])
node = queue.popleft()  # O(1)
```

## 相关题目

- [0102. Binary Tree Level Order Traversal](./102_binary_tree_level_order_traversal.md)
- [0107. Binary Tree Level Order Traversal II](./107_binary_tree_level_order_traversal_ii.md) - 自底向上
- [0103. Binary Tree Zigzag Level Order Traversal](./103_binary_tree_zigzag_level_order_traversal.md) - 锯齿形遍历
- [0199. Binary Tree Right Side View](./199_binary_tree_right_side_view.md) - 右视图
- [0637. Average of Levels in Binary Tree](./637_average_of_levels_in_binary_tree.md) - 每层平均值
