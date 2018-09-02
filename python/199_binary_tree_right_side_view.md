# binary tree right side view

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

Solution 1: Recursive, combine right and left: 5 lines, 56 ms

Compute the right view of both right and left left subtree, then combine them. For very unbalanced trees, this can be O(n^2), though.
```Python
def rightSideView(self, root):
    if not root:
        return []
    right = self.rightSideView(root.right)
    left = self.rightSideView(root.left)
    return [root.val] + right + left[len(right):]
```
Solution 2: Recursive, first come first serve: 9 lines, 48 ms

DFS-traverse the tree right-to-left, add values to the view whenever we first reach a new record depth. This is O(n).
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                dfs(node.right, depth + 1)
                dfs(node.left, depth +1)
        view = list()
        dfs(root, 0)
        return view
```
Solution 3: Iterative, level-by-level: 7 lines, 48 ms

Traverse the tree level by level and add the last value of each level to the view. This is O(n).
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view

```

再来一个caikehe的算法合集：

```Python
# DFS recursively
def rightSideView1(self, root):
    res = []
    self.dfs(root, 0, res)
    return res

def dfs(self, root, level, res):
    if root:
        if len(res) == level:
            res.append(root.val)
        self.dfs(root.right, level+1, res)
        self.dfs(root.left, level+1, res)

# DFS + stack
def rightSideView2(self, root):
    res, stack = [], [(root, 0)]
    while stack:
        curr, level = stack.pop()
        if curr:
            if len(res) == level:
                res.append(curr.val)
            stack.append((curr.left, level+1))
            stack.append((curr.right, level+1))
    return res

# BFS + queue
def rightSideView3(self, root):
    res, queue = [], [(root, 0)]
    while queue:
        curr, level = queue.pop(0)
        if curr:
            if len(res) == level:
                res.append(curr.val)
            queue.append((curr.right, level+1))
            queue.append((curr.left, level+1))
    return res
```
