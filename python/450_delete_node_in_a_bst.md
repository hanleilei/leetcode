# delete node in a bst

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:
```
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
```
根据条件判断：
1. 如果root不存在，直接返回
2. 如果key大于root的值
3. 如果key小于root的值
4. 如果key等于root的值
    a). 如果左节点不存在
    b). 如果左节点存在，找到左子树的最大值，然后替换
    
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return

        # we always want to delete the node when it is the root of a subtree,
        # so we handle left or right according to the val.
        # if the node does not exist, we will hit the very first if statement and return None.
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # now the key is the root of a subtree
        else:
            # if the subtree does not have a left child, we just return its right child
            # to its father, and they will be connected on the higher level recursion.
            if not root.left:
                return root.right

            # if it has a left child, we want to find the max val on the left subtree to
            # replace the node we want to delete.
            else:
                # try to find the max value on the left subtree
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right

                # replace
                root.val = tmp.val

                # since we have replaced the node we want to delete with the tmp, now we don't
                # want to keep the tmp on this tree, so we just use our function to delete it.
                # pass the val of tmp to the left subtree and repeat the whole approach.
                root.left = self.deleteNode(root.left, tmp.val)

        return root

```
