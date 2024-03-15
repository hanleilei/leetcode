# convert sorted array to binary search tree

[[tree]]

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

## Example 1

![](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

```text
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
```

![](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)

## Example 2

![](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)

```text
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
```

## Constraints

```text
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
```

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

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = helper(left,mid-1)
            root.right = helper(mid+1, right)
            return root
        return helper(0,len(nums)-1)
```
