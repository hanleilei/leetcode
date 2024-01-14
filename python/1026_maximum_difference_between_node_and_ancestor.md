# Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

## Example 1

![](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg)

```text
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
```

## example 2

![](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg)

```text
Input: root = [1,null,2,null,0,3]
Output: 3
```

## Constraints:

- The number of nodes in the tree is in the range `[2, 5000]`.
- `0 <= Node.val <= 10`

果然太阳下面没有什么新鲜事情啊，完全就是之前的两个题目的合集：用dfs输出所有root到叶子的路径，以及对于每个路径，做类似于best time sell stock的问题。

```python
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val, root.val)
    
    def dfs(self, root, min_val, max_val):
        if root is None:
            return max_val - min_val
        max_val = max(max_val, root.val)
        min_val = min(min_val, root.val)
        return max(self.dfs(root.left, min_val, max_val), self.dfs(root.right, min_val, max_val))
```

这种 lee215 的单行算法，图个乐就行了：

```python
class Solution:
    # def maxAncestorDiff(self, root: TreeNode) -> int:
    def maxAncestorDiff(self, root, mx=0, mn=100000):
        return max(mx - root.val, root.val - mn, \
            self.maxAncestorDiff(root.left, max(mx, root.val), min(mn, root.val)), \
            self.maxAncestorDiff(root.right, max(mx, root.val), min(mn, root.val))) \
            if root else 0
```
