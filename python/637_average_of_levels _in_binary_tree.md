# average of levels in binary tree

[[bfs]] [[tree]]

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
```
    3
   / \
  9  20
    /  \
   15   7
```
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            t_array = [x.val for x in queue]
            tmp = float(sum(t_array)) / len(t_array)
            newq = []
            for node in queue:
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            queue = newq
            res.append(tmp)
        return res
```

```python
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = list()
        if not root:
            return res
        dq = deque([root])
        while dq:
            res.append(sum([i.val for i in dq]) / len(dq))
            size = len(dq)
            for _ in range(size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res
```
