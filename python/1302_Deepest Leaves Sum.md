# Deepest Leaves Sum

[[bfs]] [[tree]]

Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:

![](https://assets.leetcode.com/uploads/2019/07/31/1483_ex1.png)

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
1 <= Node.val <= 100

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res = []
        if not root:
            return res
        dq = deque([root])
        while dq:
            size = len(dq)
            vals = [i.val for i in dq if i]
            if vals:
                res.append(sum(vals))
            for _ in range(size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res[-1]
```
