# Cousins in Binary Tree

[[tree]] [[dfs]] [[bfs]]

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:

![1](https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png)

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:

![2](https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png)

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:

![3](https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png)

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        dq = deque([root])
        while dq:
            size = len(dq)
            isXexist = False
            isYexist = False
            for i in range(size):
                cur = dq.popleft()
                if cur.val == x:
                    isXexist = True
                if cur.val == y:
                    isYexist = True
                if cur.left and cur.right:
                    if cur.left.val == x and cur.right.val == y:
                        return False
                    if cur.left.val == y and cur.right.val == x:
                        return False
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            if isXexist and isYexist:
                return True
        return False
```

似乎，加上一个parent，就变得更好理解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q = deque([(root, None)])  # 存储 (节点, 父节点)

        while q:
            level_size = len(q)
            x_parent, y_parent = None, None

            for _ in range(level_size):
                curr, parent = q.popleft()

                if curr.val == x:
                    x_parent = parent
                if curr.val == y:
                    y_parent = parent

                if curr.left:
                    q.append((curr.left, curr))
                if curr.right:
                    q.append((curr.right, curr))

            # 检查是否找到了 x 和 y
            if x_parent and y_parent:
                # 在同一层，但父节点不同，即为堂兄弟
                return x_parent != y_parent

            # 如果只找到一个，说明另一个不在这一层，它们不可能成为堂兄弟
            # if x_parent or y_parent:
            #     return False

        return False
```

再来一个dfs的版本：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # 递归函数，返回 (深度, 父节点)
        def find_info(node, target, parent, depth):
            if not node:
                return None, -1
            if node.val == target:
                return parent, depth

            left_parent, left_depth = find_info(node.left, target, node, depth + 1)
            if left_parent:
                return left_parent, left_depth

            right_parent, right_depth = find_info(node.right, target, node, depth + 1)
            return right_parent, right_depth

        x_parent, x_depth = find_info(root, x, None, 0)
        y_parent, y_depth = find_info(root, y, None, 0)

        # 深度相同且父节点不同
        return x_depth == y_depth and x_parent != y_parent
```

easy的题目，到这个程度，还是有点难度的。
