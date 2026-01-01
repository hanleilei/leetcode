# lowest common Ancestor of a Binary Tree

[[tree]]

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
```
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
```

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

不用太复杂，两个递归加上就好，深度优先遍历：

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):  # 找到 p 或 q 就不往下递归了，原因见上面答疑
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # 左右都找到
            return root  # 当前节点是最近公共祖先
        # 如果只有左子树找到，就返回左子树的返回值
        # 如果只有右子树找到，就返回右子树的返回值
        # 如果左右子树都没有找到，就返回 None（注意此时 right = None）
        return left or right
```
