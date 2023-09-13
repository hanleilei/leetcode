# maximum depth of binary tree

[[BFS]]

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
        visited = set()
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
