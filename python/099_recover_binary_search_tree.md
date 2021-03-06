# recover binary search tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:
```
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
```
Example 2:
```
Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
```

Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prevNode = TreeNode(-sys.maxsize-1)
        self.first, self.second = None, None
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if not self.first and self.prevNode.val > root.val:
            self.first, self.second = self.prevNode, root
        if self.first and self.prevNode.val > root.val:
            self.second = root
        self.prevNode = root
        self.inorder(root.right)
```

还是完完全全看看caikehe的算法就对了，他对于这类的理解很深入：

```python
# average O(lgn) space (worst case O(n) space), iteratively, one-pass
def recoverTree(self, root):
    res, stack, first, second = None, [], None, None
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            break
        node = stack.pop()
        # first time occurs reversed order
        if res and res.val > node.val:
            if not first:
                 first = res
            # first or second time occurs reversed order
            second = node
        res = node
        root = node.right
    first.val, second.val = second.val, first.val

# average O(lgn) space (worst case, O(n) space), recursively, one-pass
def recoverTree2(self, root):
    self.prevNode = TreeNode(-sys.maxsize-1)
    self.first, self.second = None, None
    self.inorder(root)
    self.first.val, self.second.val = self.second.val, self.first.val

def inorder(self, root):
    if not root:
        return
    self.inorder(root.left)
    if not self.first and self.prevNode.val > root.val:
        self.first, self.second = self.prevNode, root
    if self.first and self.prevNode.val > root.val:
        self.second = root
    self.prevNode = root
    self.inorder(root.right)

# average O(n+lgn) space, worst case O(2n) space, recursively, two-pass
def recoverTree3(self, root):
    res = []
    self.helper(root, res)
    first, second = None, None
    for i in xrange(1, len(res)):
        if not first and res[i-1].val > res[i].val:
            first, second = res[i-1], res[i]
        if first and res[i-1].val > res[i].val:
            second = res[i]
    first.val, second.val = second.val, first.val

def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root)
        self.helper(root.right, res)
```
