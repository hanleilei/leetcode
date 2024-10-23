# Kth Largest Sum in a Binary Tree

You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

Example 1:

![2](https://assets.leetcode.com/uploads/2022/12/14/binaryytreeedrawio-2.png)

```text
Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
```

Example 2:

![1](https://assets.leetcode.com/uploads/2022/12/14/treedrawio-3.png)

Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n

17分钟15秒，二次提交。加油！

层序遍历，计算每层的和，排序，返回第k大的值。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = [root.val]
        level = 0
        dq = deque([[root]])
        while dq:
            level += 1
            nodes = dq.popleft()
            t = list()
            res.append(0)
            for node in nodes:
                if node.left:
                    t.append(node.left)
                    res[-1] += node.left.val
                if node.right:
                    t.append(node.right)
                    res[-1] += node.right.val
            if t:
                dq.append(t)
        res.sort()

        return res[-k] if k <= level else -1
```

来个递归的版本：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = list()
        def bfs(root):
            nonlocal res
            q = deque([root])
            while q:
                level_sum = 0
                queue_size = len(q)
                for _ in range(queue_size):
                    node = q.popleft()
                    level_sum += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(level_sum)
        bfs(root)
        if len(res) < k:
            return -1
        res.sort(reverse=True)
        return res[k-1]
```
