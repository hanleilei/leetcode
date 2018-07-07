# construct binary tree from preorder and inorder traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

Return the following binary tree:
```
    3
   / \
  9  20
    /  \
   15   7
```




```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(preorder.pop(0))
            tree = TreeNode(inorder[index])
            tree.left = self.buildTree(preorder, inorder[0:index])
            tree.right = self.buildTree(preorder, inorder[index+1:])
            return tree
        
```