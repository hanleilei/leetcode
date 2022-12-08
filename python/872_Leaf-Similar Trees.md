# Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:

```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
```

Example 2:

![](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg)

```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
```

Constraints:

```
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
```

直接来 preorder：

```python
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1, s2 = list(), list()
        self.preorder(root1, s1)
        self.preorder(root2, s2)
        return s1 == s2

    def preorder(self, root, s):
        if root.left is None and root.right is None:
            s.append(root.val)
        if root.left is not None:
            self.preorder(root.left, s)
        if root.right is not None:
            self.preorder(root.right, s)

```
