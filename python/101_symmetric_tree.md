# symmetric tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

#### 先想到的办法，还是递归。。和之前的题目差别多。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.verify(root.left, root.right)

    def verify(self, L, R):
        if not L and not R:
            return True
        if L and R:
            return L.val == R.val and self.verify(L.left, R.right) and self.verify(L.right, R.left)
        return False

```

对于运行速度的渴求可以看下面的两个方法：

下面的这个速度就会快很多，也就是修改了一些判断条件，不去做重复判断，速度大幅提升

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.verify(root.left, root.right)

    def verify(self, L, R):
        if L is None and R is None:
            return True
        elif not L or not R:
            return False
        elif L.val != R.val:
            return False
        elif L.val == R.val:
            return L.val == R.val and self.verify(L.left, R.right) and self.verify(L.right, R.left)
        return False

```

下面的这个是速度最快的：

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def myfunc(n1,n2):
            if n1 is None and n2 is None:
                return True
            if n1 and n2 and n1.val == n2.val:
                return myfunc(n1.left,n2.right) and myfunc(n1.right,n2.left)
            return False

        return myfunc(root, root)
```
