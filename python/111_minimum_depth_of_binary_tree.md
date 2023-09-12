# minimum depth of binary tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """111
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return self.minDepth( root.right ) + 1
        if root.left != None and root.right == None:
            return self.minDepth( root.left ) + 1
        return min( self.minDepth( root.left ), self.minDepth( root.right ) ) + 1
```

上面的方法很好理解，不过这类问题第一反应应该是bfs：

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):return 0
        queue = deque([(1,root)])
        while(queue):
            depth,node=queue.popleft()
            if(not node.left and not node.right):
                return depth
            if(node.left):
                queue.append((depth+1,node.left))
            if(node.right):
                queue.append((depth+1,node.right))
```

再来一个更好理解的，注意每次遍历都是要获取dq的长度，这点真的很魔性。

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        dq = deque()
        dq.append(root)
        res = 0

        while dq:
            res += 1
            count = len(dq)
            for i in range(count):
                node = dq.popleft()
                if node is not None:
                    if not node.left and not node.right:
                        return res
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
        return res
```
