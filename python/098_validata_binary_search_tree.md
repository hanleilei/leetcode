# validate binary search tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

先做以下中序遍历，然后判断是否遍历的结果为一个递增序列就可以了。

```Python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans = list()
        self.preorder(root,ans)
        for i in range(1,len(ans)):
            if ans[i] <= ans[i-1]: return False
        return True

    def preorder(self,root,ans):
        if not root: return       
        self.preorder(root.left,ans)
        ans.append(root.val)
        self.preorder(root.right,ans)

```

下面是另一个实现方法：

递归判断左右子树。需要用出现过的最大、最小值来判断。 如左子树最大值不可能超过根，右子树最小值不可能小于根



```Python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        INF = float('inf')
        return self.judge(root,-INF,INF)


    def judge(self,root,minV,maxV):
        if not root: return True   
        if root.val <= minV or root.val >= maxV: return False      
        return self.judge(root.left,minV,root.val) and \
            self.judge(root.right,root.val,maxV)

```
