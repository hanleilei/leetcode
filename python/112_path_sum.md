# path sum

[[tree]]

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

## Example 1

![2](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)

```text
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
```

## Example 2

![1](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```text
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
```

## Example 3

```text
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
```

## Constraints

```text
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
```

直接上递归，算得上是最简便的方法了。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, targetsum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == targetsum
        return self.hasPathSum(root.left, targetsum - root.val) or self.hasPathSum(root.right, targetsum - root.val)
```

似乎，不是很清晰，看到还有一个更清晰的版本：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.helper(root, targetSum)

    def helper(self, node, targetSum):
        targetSum -= node.val

        if not node.left and not node.right:
            return targetSum == 0

        return (self.helper(node.left, targetSum) or self.helper(node.right, targetSum))

```

再来一个，直接用stack，和113一样，只是稍作改动：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        res = list()
        stack = [(root, 0)]

        while stack:
            node, curr = stack.pop()
            curr += node.val
            if not node.left and not node.right:
                if curr == targetSum:
                    return True
            if node.left:
                stack.append((node.left, curr))
            if node.right:
                stack.append((node.right, curr))
        return False
```
