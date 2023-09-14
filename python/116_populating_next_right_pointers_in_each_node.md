# populating next right pointers in each node

Given a binary tree
```
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
```
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

#### Note:

* You may only use constant extra space.
* Recursive approach is fine, implicit stack space does not count as extra space for this problem.
* You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

#### Example:

Given the following perfect binary tree,
```
     1
   /  \
  2    3
 / \  / \
4  5  6  7
```
After calling your function, the tree should look like:
```
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
```

先来的stefan的方法，现在通过不了了（2023/09/15）

```python
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
```

```python
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        head = root
        while head and head.left:
            p = head
            cur = None

            while p:
                if cur is None:
                    cur = p.left
                else:
                    cur.next = p.left
                    cur = p.left

                cur.next = p.right
                cur = p.right
                p = p.next

            head = head.left
```

```Python
# """
# Definition for a Node.
# class Node:
#     def __init__(self, val, left, right, next):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
# """
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        cur = root
        next = cur.left
        while cur.left:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next
                next = cur.left
        return root
```

我就知道会有这样的bfs方法，配上一个临时数组和对于数组宽度为长度的遍历。

```Python

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None

        queue = [root]
        while queue:
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
            queue[-1].next = None
            tmp = []
            for node in queue:
                tmp.extend([node.left, node.right])

            queue = [n for n in tmp if n]
        return root
```

再来一个labuladong的递归方法：

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            self.connectTwoNode(root.left, root.right)
        return root

    def connectTwoNode(self, left, right):
        if left is None or right is None:
            return 
        left.next = right
        self.connectTwoNode(left.left, left.right)
        self.connectTwoNode(right.left, right.right)
        self.connectTwoNode(left.right, right.left)
```

可能我的境界还没有达到，目前还是觉得labuladong的方法最容易理解。