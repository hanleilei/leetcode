# balance binary tree

Given a binary tree, determine if it is .

Example 1:

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -10^4 <= Node.val <= 10^4

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1
```

稍微修改一下，这个速度最快：

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        flag = 0
        def recur(root):
            nonlocal flag
            if not root: return 0
            left = recur(root.left)
            right = recur(root.right)
            if flag == 1 or abs(left - right) > 1:
                flag = 1
                return
            return max(left, right) + 1
        recur(root)
        return flag == 0
```

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
```
