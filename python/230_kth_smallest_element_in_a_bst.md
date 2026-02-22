# Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

### Example 1

Input: root = [3,1,4,null,2], k = 1

```
   3
  / \
 1   4
  \
   2
```

Output: 1

### Example 2

Input: root = [5,3,6,2,4,null,null,1], k = 3

```
       5
      / \
     3   6
    / \
   2   4
  /
 1
```

Output: 3

### Follow up

What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = list()
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        
```

思路

由于中序遍历就是在从小到大遍历节点值，所以遍历到的第 k 个节点值就是答案。

写法一：记录答案

在中序遍历，即「左-根-右」的过程中，每次递归完左子树，就把 k 减少 1，表示我们按照中序遍历访问到了一个节点。如果减一后 k 变成 0，那么答案就是当前节点的值，用一个外部变量 ans 记录。

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal k, res
            if node is None or k == 0:
                return 
            dfs(node.left)
            k -= 1
            if k == 0:
                res = node.val
            dfs(node.right)
        dfs(root)
        return res
```

写法二：不记录答案 + 提前返回

写法一使用了一个外部变量记录答案，能否不使用外部变量记录呢？

可以，做法如下：

- 递归边界：如果当前节点是空节点，返回 −1，表示没有找到。注意题目保证节点值非负。
- 执行中序遍历，先递归左子树。
- 判断左子树的返回值 leftRes 是否为 −1。如果不是 −1，说明我们在左子树中找到了答案，返回 leftRes。如果是 −1，说明尚未找到答案，继续下一步。
- 把 k 减少 1。如果 k=0，那么答案就是当前节点值，返回当前节点值。
- 现在，答案要么在当前节点的右子树中，要么在除了当前子树的其余节点中。递归右子树，如果答案在右子树中，那么直接返回答案；如果答案不在右子树中，那么右子树也会返回 −1，由于当前子树搜索完毕，所以当前子树没有找到答案，返回 −1。综上所述，可以直接返回右子树的返回值。

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1  # 题目保证节点值非负，用 -1 表示没有找到
            left_res = dfs(node.left)
            if left_res != -1:  # 答案在左子树中
                return left_res
            nonlocal k
            k -= 1
            if k == 0:  # 答案就是当前节点
                return node.val
            return dfs(node.right)  # 右子树会返回答案或者 -1
        return dfs(root)
```

写法三： 记录中序遍历结果

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = list()
        self.dfs(root)

        return self.res[k-1]
    
    def dfs(self, root):
        if root is None:
            return 

        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)
```
