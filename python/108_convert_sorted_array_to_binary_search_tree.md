# convert sorted array to binary search tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

基本就是递归的思路，由于要求二叉查找树是平衡的。所以我们可以选在数组的中间那个数当树根root，然后这个数左边的数组为左子树，右边的数组为右子树，分别递归产生左右子树就可以了。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        size = len(nums)
        if size == 0:
            return None
        if size == 1:
            return TreeNode(nums[0])

        root = TreeNode(nums[size//2])
        root.left = self.sortedArrayToBST(nums[:size//2])
        root.right = self.sortedArrayToBST(nums[size//2+1:])
        return root
```
