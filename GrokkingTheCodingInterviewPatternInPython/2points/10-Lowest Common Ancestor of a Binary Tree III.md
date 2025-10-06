# Lowest Common Ancestor of a Binary Tree III

Try to solve the Lowest Common Ancestor of a Binary Tree III problem.

Statement
You are given two nodes, p and q. The task is to return their lowest common ancestor (LCA). Both nodes have a reference to their parent node. The tree’s root is not provided; you must use the parent pointers to find the nodes’ common ancestor.

Note: The lowest common ancestor of two nodes, p and q, is the lowest node in the binary tree, with both p and q as descendants.

In a tree, a descendant of a node is any node reachable by following edges downward from that node, including the node itself.

Constraints:

- −10 ** 4 ≤ Node.data ≤ 10 ** 4
- The number of nodes in the tree is in the range [2, 500].
- All Node.data are unique.
- p != q
- Both p and q are present in the tree.

## solution

This solution finds the lowest common ancestor (LCA) of two nodes in a binary tree using a smart two-pointer approach. We start by placing one pointer at node p and the other at node q. Both pointers move up the tree at each step by following their parent pointers. If a pointer reaches the root (i.e., its parent is None), it jumps to the other starting node. This process continues until the two pointers meet. **The key idea is that by switching starting points after reaching the top, both pointers end up traveling the same total distance, even if p and q are at different depths**. When they meet, that meeting point is their lowest common ancestor.

The steps of the algorithm are as follows:

Initialize two pointers: ptr1 starting at p and ptr2 starting at q.
While ptr1 and ptr2 are not pointing to the same node:
If ptr1 has a parent, move ptr1 to ptr1.parent; otherwise, set ptr1 = q.
If ptr2 has a parent, move ptr2 to ptr2.parent; otherwise, set ptr2 = p.
When ptr1 == ptr2, return ptr1. This node is the lowest common ancestor (LCA) of p and q.

steps:
1. Initialize two pointers, one on each of the given nodes.
2. Move both pointers upward along the tree using the parent node, one step at a time.
3. If a pointer reaches the top of the tree (NULL), move it to the starting position of the other node.
4. Continue moving until these pointers meet. The point where they meet is the lowest common ancestor of the p and q nodes.

```python
# Definition for a binary tree node
# class EduTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.parent = None

from EduTreeNode import *

def lowest_common_ancestor(p, q):
    pp, qq = p, q
    while pp != qq:
        if pp.parent:
            pp = pp.parent
        else:
            pp = q
        if qq.parent:
            qq = qq.parent
        else:
            qq = p
        

    # Replace this placeholder return statement with your code
    return pp
```
