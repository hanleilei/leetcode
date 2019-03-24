# Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

## Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

### Example:

Input:
```
    1
   / \
  2   3
 / \  /
4  5 6
```
Output: 6

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        l = self.leftHeight(root.left)
        r = self.leftHeight(root.right)
        if l == r:
            return self.countNodes(root.right) + (1<<r)
        return self.countNodes(root.left) + (1 << r)

    def leftHeight(self, node):
        height = 0
        while node is not None:
            height += 1
            node = node.left
        return height
```

再来一个稍微简化一点的版本：
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)

        if l == r:
            return 2 ** l + self.countNodes(root.right)
        else:
            return 2 ** r + self.countNodes(root.left)

    def getDepth(self, node):
        if node is None:
            return 0
        return 1 + self.getDepth(node.left)

```

在这个算法中，似乎获取深度的函数可以省略：
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left, right = root, root
        height = 0
        while right is not None:
            left = left.left
            right = right.right
            height += 1

        if left is None:
            return (1 << height) -1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

再来一个 binary search 的版本：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        height = self.getHeight(root)
        last_level = 0
        left, right = 0, 2**height-1
        while left <= right:
            mid = (left+right)/2
            if self.getKthNode(root, height, mid) is None:
                right = mid - 1
            else:
                left = mid + 1
                last_level = mid+1
        return last_level + 2**height - 1

    def getHeight(self, root):
        count = 0
        while root.left is not None:
            count += 1
            root = root.left
        return count

    def getKthNode(self, root, height, k):
        # binary bits representation of the root-to-leaf path
        while height > 0:
            if 2**(height-1) & k == 2**(height-1): # current bit is '1', turn right
                root = root.right
            else: # current bit is '0', turn left
                root = root.left
            height -= 1
        return root

```
