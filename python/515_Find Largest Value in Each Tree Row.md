# Find Largest Value in Each Tree Row

[[tree]] [[bfs]]

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:

![](https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg)

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1

和102一样，用bfs来做，每次记录这一层的最大值即可。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            tmp = [x.val for x in queue]
            newq = []
            for node in queue:
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            queue = newq
            res.append(max(tmp))
        return res
```

```python
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        dq = deque([root])
        while dq:
            size = len(dq)
            vals = [i.val for i in dq if i]
            if vals:
                res.append(max(vals))
            for _ in range(size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res
```
