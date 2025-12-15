# construct binary tree from preorder and inorder traversal

[[tree]] [[stack]] [[dfs]]

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

```text
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

Return the following binary tree:

```text
    3
   / \
  9  20
    /  \
   15   7
```

## Constraints

```text
    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.
```

递归

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

dfs:

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {x:i for i, x in enumerate(inorder)}

        def dfs(pre_l, pre_r, in_l, in_r):
            if pre_l == pre_r:
                return None

            left_size = index[preorder[pre_l]] - in_l
            left = dfs(pre_l+1, pre_l+1+left_size, in_l, in_l+left_size)
            right = dfs(pre_l+1+left_size, pre_r, in_l+left_size+1, in_r)
            return TreeNode(preorder[pre_l], left, right)
        return dfs(0, len(preorder), 0, len(inorder))
```

stack

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)

        return root
```
