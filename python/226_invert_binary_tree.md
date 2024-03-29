# invert binary Tree

Invert a binary tree.

```text
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

to

```text
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

### Trivia:

This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

据说是将 homebrew 作者折腾失败的 Google 面试题目。

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
```

bfs:

```Python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # BFS

        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
```

DFS:

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # DFS
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root
```

再来一个 labuladong 的：

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root

    def traverse(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.traverse(root.left)
        self.traverse(root.right)
```

再来一个分解问题后的方法：

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root
```
