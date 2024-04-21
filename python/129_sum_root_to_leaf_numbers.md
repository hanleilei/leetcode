# sum root to leaf number

[[tree]] [[bfs]] [[dfs]]

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

```text
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

Example 2:

```text
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

首先，看下使用stack的DFS实现：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if not node.right and not node.left:
                res += value
            if node.right:
                stack.append((root.right, value * 10 + root.right.val))
            if node.left:
                stack.append((root.left, value * 10 + root.left.val))

        return res

```

再来看一个使用queue的BFS版本：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack, res = deque([(root, root.val)]), 0
        while stack:
            node, value = stack.popleft()
            if not node.right and not node.left:
                res += value
            if node.right:
                stack.append((node.right, value * 10 + node.right.val))
            if node.left:
                stack.append((node.left, value * 10 + node.left.val))

        return res
```
再来一个DFS的递归版本：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, value):
        if root:
            self.dfs(root.left, value * 10 + root.val)
            self.dfs(root.right, value * 10 + root.val)
            if not root.left and not root.right:
                self.res += value * 10 + root.val
```

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root,val):
            val=10*val+root.val
            if (root.left or root.right) is None:
                return val
            sums=0
            if root.left:
                sums+=dfs(root.left,val)
            if root.right:
                sums+=dfs(root.right,val)
            return sums
        if not root: return 0
        return dfs(root,0)
```

来一个最近的：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, path: str):
            nonlocal ans
            path = path + str(node.val)
            if not node.left and not node.right:
                ans += int(path)
            else:
                if node.left: dfs(node.left, path)
                if node.right: dfs(node.right, path)
        dfs(root, "")
        return ans
```
