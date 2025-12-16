# Maximum Depth of N-ary Tree

[[tree]]

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:

![Narytreeexample image](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Example 2:

![Sample 4 964 image](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

Constraints:

The total number of nodes is in the range [0, 104].
The depth of the n-ary tree is less than or equal to 1000.

DFS：

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        dq = collections.deque()
        dq.append(root)
        depth = 0

        while dq:
            for _ in range(0,len(dq)):
                cur = dq.popleft()
                if not cur:
                    return depth
                for neigh in cur.children:
                    dq.append(neigh)

            depth+=1

        return depth
```

递归版：

```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.depth = 0
        if not root:
            return self.depth
        def dfs(node, d):
            if not node.children:
                self.depth = max(self.depth, d)
                return
            for child in node.children:
                dfs(child, d + 1)
        dfs(root, 1)
        return self.depth
```

```python

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(n) for n in root.children) + 1
```

```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        depth = 0

        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return depth + 1
```
