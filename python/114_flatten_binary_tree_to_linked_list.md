# Flatten Binary Tree to Linked List

[[tree]]

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

```text
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

## 前序遍历逆序法（头部插入）

The answer use self.prev to recode the ordered tree of the right part of current node.
Remove the left part of current node

具体来说：

1. 如果当前节点为空，返回。
2. 递归右子树。
3. 递归左子树。
4. 把 root.left 置为空。
5. 头插法，把 root 插在 head 的前面，也就是 root.right=head。
6. 现在 root 是链表的头节点，把 head 更新为 root。

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

        root.left = None
        root.right = self.prev
        self.prev = root
```

```java
class Solution {
    private TreeNode head;

    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }
        flatten(root.right);
        flatten(root.left);
        root.left = null;
        root.right = head; // 头插法，相当于链表的 root.next = head
        head = root; // 现在链表头节点是 root
    }
}
```

```go
func flatten(root *TreeNode) {
    var head *TreeNode
    var dfs func(*TreeNode)
    dfs = func(node *TreeNode) {
        if node == nil {
            return
        }
        dfs(node.Right)
        dfs(node.Left)
        node.Left = nil
        node.Right = head // 头插法，相当于链表的 node.Next = head
        head = node       // 现在链表头节点是 node
    }
    dfs(root)
}
```

```rust
use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, head: &mut Option<Rc<RefCell<TreeNode>>>) {
        if let Some(x) = node {
            let mut x = x.borrow_mut();
            Self::dfs(&x.right, head);
            Self::dfs(&x.left, head);
            x.left = None;
            x.right = head.take(); // 头插法，相当于链表的 node.next = head
            *head = node.clone(); // 现在链表头节点是 node
        }
    }

    pub fn flatten(root: &mut Option<Rc<RefCell<TreeNode>>>) { // mut 可以去掉
        let mut head = None;
        Self::dfs(&root, &mut head);
    }
}
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

## 分治

考虑分治，假如我们计算出了 root=1 左子树的链表 2→3→4，以及右子树的链表 5→6，那么接下来只需要穿针引线，把节点 1 和两条链表连起来：

先把 2→3→4 和 5→6 连起来，也就是左子树链表尾节点 4 的 right 更新为节点 5（即 root.right），得到 2→3→4→5→6。
然后把 1 和 2→3→4→5→6 连起来，也就是节点 1 的 right 更新为节点 2（即 root.left），得到 1→2→3→4→5→6。
最后把 root.left 置为空。
上面的过程，我们需要知道左子树链表的尾节点 4。所以 DFS 需要返回链表的尾节点。

链表合并完成后，返回合并后的链表的尾节点，也就是右子树链表的尾节点。如果右子树是空的，则返回左子树链表的尾节点。如果左右子树都是空的，返回当前节点。

```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right)
        if left_tail:
            left_tail.right = root.right  # 左子树链表 -> 右子树链表
            root.right = root.left  # 当前节点 -> 左右子树合并后的链表
            root.left = None
        return right_tail or left_tail or root
```

```java
class Solution {
    public void flatten(TreeNode root) {
        dfs(root);
    }

    private TreeNode dfs(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode leftTail = dfs(root.left);
        TreeNode rightTail = dfs(root.right);
        if (leftTail != null) {
            leftTail.right = root.right; // 左子树链表 -> 右子树链表
            root.right = root.left; // 当前节点 -> 左右子树合并后的链表
            root.left = null;
        }
        return rightTail != null ? rightTail : leftTail != null ? leftTail : root;
    }
}
```

```go
func dfs(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    leftTail := dfs(root.Left)
    rightTail := dfs(root.Right)
    if leftTail != nil {
        leftTail.Right = root.Right // 左子树链表 -> 右子树链表
        root.Right = root.Left      // 当前节点 -> 左右子树合并后的链表
        root.Left = nil
    }
    if rightTail != nil {
        return rightTail
    }
    if leftTail != nil {
        return leftTail
    }
    return root
}

func flatten(root *TreeNode) {
    dfs(root)
}
```

```cpp
class Solution {
    TreeNode* dfs(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }
        TreeNode* left_tail = dfs(root->left);
        TreeNode* right_tail = dfs(root->right);
        if (left_tail) {
            left_tail->right = root->right; // 左子树链表 -> 右子树链表
            root->right = root->left; // 当前节点 -> 左右子树合并后的链表
            root->left = nullptr;
        }
        return right_tail ? right_tail : left_tail ? left_tail : root;
    }

public:
    void flatten(TreeNode* root) {
        dfs(root);
    }
};
```

```rust
use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(x) = node {
            let mut x = x.borrow_mut();
            let left_tail = Self::dfs(&x.left);
            let right_tail = Self::dfs(&x.right);
            if let Some(lt) = &left_tail {
                lt.borrow_mut().right = x.right.take(); // 左子树链表 -> 右子树链表
                x.right = x.left.take(); // 当前节点 -> 左右子树合并后的链表
            }
            return right_tail.or(left_tail).or(node.clone());
        }
        None
    }

    pub fn flatten(root: &mut Option<Rc<RefCell<TreeNode>>>) { // mut 可以去掉
        Self::dfs(root);
    }
}
```

### 后序遍历

```python
        def helper(root):
            if root == None: return
            helper(root.left)
            helper(root.right)
            if root.left != None: # 后序遍历
                pre = root.left # 令 pre 指向左子树
                while pre.right: 
                    pre = pre.right # 找到左子树中的最右节点
                pre.right = root.right # 令左子树中的最右节点的右子树 指向 根节点的右子树
                root.right = root.left # 令根节点的右子树指向根节点的左子树
                root.left = None # 置空根节点的左子树
            root = root.right # 令当前节点指向下一个节点
        helper(root)
```
