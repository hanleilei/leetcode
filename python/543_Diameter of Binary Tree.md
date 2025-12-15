# Diameter of Binary Tree

[[tree]]

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

## Example 1

![Diamtree](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```text
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

## Example 2

```text
Input: root = [1,2]
Output: 1
```

## Constraints

```text
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node is None:
            return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        self.res = max(self.res, l + r)
        return max(l, r) + 1
```

再来一个迭代的方法，速度还很快：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [[root, False]]
        heights = {}
        while stack:
            node, seen = stack[-1]
            if not seen:
                stack[-1][1] = True
                if node.left:
                    stack.append([node.left, False])
                if node.right:
                    stack.append([node.right, False])
            else:
                left = heights.get(node.left, 0)
                right = heights.get(node.right, 0)

                res = max(res, left + right)
                heights[node] = max(left, right) + 1
                stack.pop()
        return res   
```
