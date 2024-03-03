# Find Bottom Left Tree Value

[[tree]]

Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
![](https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg)
Input: root = [2,1,3]
Output: 1
Example 2:

![](https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg)
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

典型的bfs问题：

注意这里有个细节：先右边，再左边。。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = collections.deque()
        dq.append(root)

        while dq:
            node = dq.popleft()
            res = node.val
            if node.right:
                dq.append(node.right)            
            if node.left:
                dq.append(node.left)
        return res
```

还有就是直接拿102 的层序遍历：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res[::-1][-1][0]
```
