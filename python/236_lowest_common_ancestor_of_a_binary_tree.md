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

或者使用倍增法(Binary Lifting):

最近公共祖先（LCA）问题是树结构中的一个经典问题，倍增法是一种高效的解决方案，它通过预处理在O(log n)时间内回答任意两个节点的LCA查询。

看b站[视频](https://www.bilibili.com/video/BV1T7iEBnEcx/?spm_id_from=333.1387.upload.video_card.click&vd_source=87d6dd47dbb44dd80e0f5eb84dd30767)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.depth = {}
        self.parent = {}  # 键: 节点, 值: 列表，存储2^i级祖先

    def _init_lca(self):
        """预处理深度和倍增表"""
        # 计算树的最大深度以确定LOG
        max_depth = self._compute_max_depth(self.root)
        self.LOG = 0
        while (1 << self.LOG) <= max_depth:
            self.LOG += 1

        # BFS遍历所有节点，记录直接父节点和深度
        parent_map = {self.root: None}
        depth_map = {self.root: 0}
        queue = [self.root]
        nodes = [self.root]

        while queue:
            node = queue.pop(0)
            if node.left:
                parent_map[node.left] = node
                depth_map[node.left] = depth_map[node] + 1
                queue.append(node.left)
                nodes.append(node.left)
            if node.right:
                parent_map[node.right] = node
                depth_map[node.right] = depth_map[node] + 1
                queue.append(node.right)
                nodes.append(node.right)

        self.depth = depth_map
        self.parent = {}

        # 初始化倍增表
        for node in nodes:
            self.parent[node] = [None] * self.LOG
            self.parent[node][0] = parent_map[node]  # 直接父节点

        # 动态规划填充倍增表
        for i in range(1, self.LOG):
            for node in nodes:
                if self.parent[node][i - 1] is not None:
                    self.parent[node][i] = (
                        self.parent[self.parent[node][i - 1]][i - 1]
                        if self.parent[node][i - 1] in self.parent
                        else None
                    )

    def _compute_max_depth(self, node):
        """计算树的最大深度"""
        if not node:
            return 0
        return 1 + max(
            self._compute_max_depth(node.left), self._compute_max_depth(node.right)
        )

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """查询节点p和q的最近公共祖先"""
        self.root = root
        self._init_lca()
        if p not in self.depth or q not in self.depth:
            return None

        # 确保p的深度 >= q的深度
        if self.depth[p] < self.depth[q]:
            p, q = q, p

        # 将p提升到与q同一深度
        diff = self.depth[p] - self.depth[q]
        for i in range(self.LOG):
            if (diff >> i) & 1:  # 检查深度差的二进制位
                p = self.parent[p][i]
                if p is None:
                    break

        if p == q:
            return p

        # 同步向上跳跃
        for i in range(self.LOG - 1, -1, -1):
            if self.parent[p][i] != self.parent[q][i]:
                p = self.parent[p][i]
                q = self.parent[q][i]

        return self.parent[p][0]  # 返回父节点即为LCA
```
