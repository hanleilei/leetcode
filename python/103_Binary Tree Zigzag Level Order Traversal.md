# Binary Tree Zigzag Level Order Traversal

[[bfs]]

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        nodes = deque([root])
        depth = 0  # 从0开始计数，表示当前层数
        
        while nodes:
            size = len(nodes)
            level_vals = []
            
            for _ in range(size):
                node = nodes.popleft()
                level_vals.append(node.val)
                
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            
            # 如果当前是奇数层（从0开始计数，0表示第1层），则反转
            if depth % 2 == 1:
                level_vals = level_vals[::-1]
            
            res.append(level_vals)
            depth += 1  # 只在处理完一层后增加深度
        
        return res
```

微小的差别在于最后一行的返回值：

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = list()
        nodes = deque([root])
        direction = 1
        while nodes:
            vals = list()
            size = len(nodes)
            for _ in range(size):
                node = nodes.popleft()
                vals.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            res.append(vals[::direction])
            direction *= -1
        return res
```
