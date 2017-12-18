# binary tree paths

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:
```
   1
 /   \
2     3
 \
  5
```
All root-to-leaf paths are:
```
["1->2->5", "1->3"]
```

queue + bfs

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        from collections import deque
        if not root:
            return []
        res, stack = [], deque([(root, "")])
        while stack:
            node, ls = stack.popleft()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                stack.append((node.left, ls+str(node.val)+'->'))
            if node.right:
                stack.append((node.right, ls+str(node.val)+'->'))

        return res
```

DFS + stack

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+'->'))
            if node.left:
                stack.append((node.left, ls+str(node.val)+'->'))
        return res
```
