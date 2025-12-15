# minimum depth of binary tree

[[BFS]] [[DFS]] [[tree]]

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

![Ex Depth image](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

The number of nodes in the tree is in the range [0, 10^5].
-1000 <= Node.val <= 1000

dfs:

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

或者和最大深度类似的方法：

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        if not root:
            return 0

        def dfs(node, depth):
            nonlocal res
            if not node.left and not node.right:
                res = min(res, depth)
                return
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 1)
        return res
```

bfs：

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

再来一个更好理解的，注意每次遍历都是要获取dq的长度:

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        dq = deque([root])
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

时隔多年，闭眼手搓了一个：

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq = deque([(root, 1)])

        while dq:
            node, level = dq.popleft()
            if node.left or node.right:
                level += 1
                if node.left:
                    dq.append((node.left, level))
                if node.right:
                    dq.append((node.right, level))
            else:
                return level
        return 0
```
