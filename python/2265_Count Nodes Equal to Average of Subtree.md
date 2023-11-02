# Count Nodes Equal to Average of Subtree

[[tree]] [[dfs]]

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.

## Example 1

![1](https://assets.leetcode.com/uploads/2022/03/15/image-20220315203925-1.png)

```text
Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
```

## Example 2

![](https://assets.leetcode.com/uploads/2022/03/26/image-20220326133920-1.png)

```text
Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
```

## Constraints

```text
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
```

dfs

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> tuple[float, float]:
            if node is None:
                return 0.0, 0.0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1

            if curr_sum // curr_count == node.val:
                self.res += 1

            return curr_sum, curr_count

        dfs(root)
        return self.res
```
