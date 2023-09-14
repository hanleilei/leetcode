# Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

```text
    1
   / \
  2   5
 / \   \
3   4   6
```

The flattened tree should look like:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.prev = root
        self.flatten(root.left)

        temp = root.right
        root.right, root.left = root.left, None
        self.prev.right = temp

        self.flatten(temp)
```

下面的算法是对前序遍历求逆：
```
	root
    / 
  1 
 / \ 
3  4
```

Let's see what is happening with this code.

---

Node(4).right = None
Node(4).left = None
prev = Node(4)

Node(3).right = Node(4) (prev)
Node(3).left = None
prev = Node(3)->Node(4)

Node(1).right = prev = Node(3) -> Node(4)
Node(1).left = None
prev = Node(1)->Node(3)->Node(4) (Which is the answer)

---

The answer use self.prev to recode the ordered tree of the right part of current node.
Remove the left part of current node

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    prev = None
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
        
```

再来一个labuladong的方法：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        # /**** 后序遍历位置 ****/
        # // 1、左右子树已经被拉平成一条链表
        left = root.left;
        right = root.right;

        # // 2、将左子树作为右子树
        root.left = None;
        root.right = left;

        # // 3、将原先的右子树接到当前右子树的末端
        p = root
        while p.right is not None:
            p = p.right;

        p.right = right;
```

labuladong的方法确实属于我这样的废材人类。。
