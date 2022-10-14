# path sum

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
```

return

```
[
   [5,4,11,2],
   [5,8,4,5]
]
```

bfs + stack

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type s: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res

```

dfs + queue

```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == targetSum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res
```

换一种写法：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        way = []

        def allway(root, target):
            if root is None:
                return
            way.append(root.val)
            if root.left is None and root.right is None and root.val == target:
                res.append(way.copy())
            else:
                allway(root.left, target-root.val)
                allway(root.right, target-root.val)
            way.pop()
        allway(root, target)
        return res
```
