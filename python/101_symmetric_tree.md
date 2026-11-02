# symmetric tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

But the following [1,2,2,null,3,null,3] is not:

```
    1
   / \
  2   2
   \   \
   3    3
```

### Note

Bonus points if you could solve it both recursively and iteratively.

先想到的办法，还是递归。。和之前的题目差别多。

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
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q: return True
            if not p or not q: return False
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)

        return check(root.left, root.right)
```

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque()
        q.append(root.left)
        q.append(root.right)
        
        while q:
            p = q.popleft()
            q_node = q.popleft()
            
            # 两个都为空，继续检查下一对节点
            if not p and not q_node:
                continue
            # 只有一个为空，结构不对称
            if not p or not q_node:
                return False
            # 值不相等，不对称
            if p.val != q_node.val:
                return False
            
            # 将对称位置的节点成对入队
            q.append(p.left)
            q.append(q_node.right)
            
            q.append(p.right)
            q.append(q_node.left)
        
        return True
```
