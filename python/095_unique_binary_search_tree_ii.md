# unique binary search tree II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:
```
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.genTree(1, n)if n >= 1 else []


    def genTree(self, s, e):
        if s > e:
            return [None]
        ans = []
        for i in range(s, e+1):
            L = self.genTree(s, i-1)
            R = self.genTree(i+1, e)
            for left in L:
                for right in R:
                    root = TreeNode(i)
                    root.left, root.right = left, right
                    ans.append(root)
        return ans
```
