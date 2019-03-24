# Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



### Example:

![](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)
```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
```

### Note:

* next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
* You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

先来一个stack的版本：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = list()
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self) -> int:
        """
        @return the next smallest number
        """
        return len(self.stack) > 0


    def next(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# @return an integer, the next smallest number
```

很小的改进，更精简代码：

```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = list()
        self.helper(root)

    def hasNext(self) -> int:
        """
        @return the next smallest number
        """
        return self.stack != []


    def next(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        node = self.stack.pop()
        self.helper(node.right)
        return node.val

    def helper(self, root):
        while root:
            self.stack.append(root)
            root = root.left
```

再来一个迭代器版本的：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        self.last = root
        while self.last and self.last.right:
            self.last = self.last.right
        self.current = None
        self.g = self.iterate(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.current is not self.last

    # @return an integer, the next smallest number
    def next(self):
        return next(self.g)

    def iterate(self, node):
        if node is None:
            return
        for x in self.iterate(node.left):
            yield x
        self.current = node
        yield node.val
        for x in self.iterate(node.right):
            yield x






# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# @return an integer, the next smallest number
```
