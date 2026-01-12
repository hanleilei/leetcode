# Check Completeness of a Binary Tree

[[bfs]] [[tree]]

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:

![](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png)

```text
        1
      /   \
     2     3
    / \   /
   4   5 6
```

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:

![](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png)

```text
        1
      /   \
     2     3
    / \     \
   4   5     7
```

Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.


Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000

```python
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        prev = root
        
        while queue:
            node = queue.popleft()
            
            # 如果之前遇到了空节点，但当前节点不为空，说明不是完全二叉树 关键步骤！
            if prev is None and node is not None:
                return False
            
            # 将左右子节点加入队列（即使是None也要加入）
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
            
            prev = node  # 更新前一个节点
        
        return True
```
