# binary tree maximum path sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
```
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
```
Example 2:
```
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxsums(node):
            if not node:
                return [-2**31] * 2
            left = maxsums(node.left)
            right = maxsums(node.right)
            return [node.val + max(left[0], right[0], 0),
                    max(left + right + [node.val + left[0] + right[0]])]
        return max(maxsums(root))
```
