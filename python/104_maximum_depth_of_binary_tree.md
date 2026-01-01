# maximum depth of binary tree

[[BFS]] [[DFS]] [[Tree]] [[BinaryTree]]

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node

先使用深度优先遍历：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

或者

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        # 记录遍历到的节点的深度
        self.depth = 0
        # 记录最大深度
        self.res = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.res

    # 遍历二叉树
    def traverse(self, root: TreeNode):
        if root is None:
            return

        # 前序遍历位置（进入节点）增加深度
        self.depth += 1
        # 遍历到叶子节点时记录最大深度
        if root.left is None and root.right is None:
            self.res = max(self.res, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)

        # 后序遍历位置（离开节点）减少深度
        self.depth -= 1
```

这个方法，第一次看确实不是很好理解，尤其是为什么最后还要减去1。不过理解了前序和后序遍历的位置后，就很清晰了。

下面尝试广度优先遍历：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        dq = collections.deque()
        dq.append(root)
        while dq:
            res += 1
            for i in range(len(dq)):
                p = dq.popleft()
                if p.left:
                    dq.append(p.left)
                if p.right:
                    dq.append(p.right)
        return res
```

现在，我也能熟练的手撕这类问题了：

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0 
        dq = deque([[root, 1]])
        depth = 0

        while dq:
            node, depth = dq.popleft()
            if node is not None:
                if node.left:
                    dq.append([node.left, depth + 1])
                if node.right:
                    dq.append([node.right, depth + 1])
        return depth
```
