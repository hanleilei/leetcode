# populating next right pointers in each node

[[tree]] [[bfs]] [[dfs]]

Given a binary tree

```text
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

## Note

* You may only use constant extra space.
* Recursive approach is fine, implicit stack space does not count as extra space for this problem.
* You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

### Example

Given the following perfect binary tree,

```text
     1
   /  \
  2    3
 / \  / \
4  5  6  7
```

After calling your function, the tree should look like:

```text
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
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

bfs方法，配上一个临时数组和对于数组宽度为长度的遍历。

思路: 只需要把每一层的节点，从左到右依次用 next 指针连接起来。注意特判 root 为空的情况。

```python
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = deque([root])
        result=[]
        while queue:
            level_size = len(queue)
            prve = None
            for i in range (level_size):
                node = queue.popleft()
                if prve:
                    prve.next = node
                prve = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root   
```

思路

既然每一层都连接成一个链表了，那么知道链表头，就能访问这一层的所有节点。

所以在 BFS 的时候，可以一边遍历当前层的节点，一边把下一层的节点连接起来。这样就无需存储下一层的节点了，只需要拿到下一层链表的头节点。

算法

1. 从第一层开始（第一层只有一个 root 节点），每次循环：
2. 遍历当前层的链表节点，通过节点的 left 和 right 得到下一层的节点。
3. 把下一层的节点从左到右连接成一个链表。
4. 拿到下一层链表的头节点，进入下一轮循环。

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur:
            nxt = dummy = Node()  # 下一层的链表
            while cur:  # 遍历当前层的链表
                if cur.left:
                    nxt.next = cur.left  # 下一层的相邻节点连起来
                    nxt = cur.left
                if cur.right:
                    nxt.next = cur.right  # 下一层的相邻节点连起来
                    nxt = cur.right
                cur = cur.next  # 当前层链表的下一个节点
            cur = dummy.next  # 下一层链表的头节点
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

按照题目要求仿真：

```python
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftmost = root  # 保存每一层的最左节点

        while leftmost.left:  # 当还有下一层时
            curr = leftmost  # 当前层遍历指针

            while curr:
                # 连接当前节点的左右子节点
                curr.left.next = curr.right

                # 连接当前节点的右子节点和相邻节点的左子节点
                if curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next  # 移动到当前层的下一个节点

            leftmost = leftmost.left  # 移动到下一层

        return root
```

DFS:

算法:

1. 创建一个空数组 pre（因为一开始不知道二叉树有多深）。
2. DFS 这棵二叉树，递归参数为当前节点 node，以及当前节点的深度 depth。每往下递归一层，就把 depth 加一。
3. 如果 depth 等于 pre 数组的长度，说明 node 是这一层最左边的节点，把 node 添加到 pre 的末尾。
4. 否则，把 pre[depth] 的 next 指向 node，然后更新 pre[depth] 为 node。
5. 递归边界：如果 node 是空节点，直接返回。
6. 递归入口：dfs(root,0)。
7. 最后返回 root。

```python
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        pre = []
        def dfs(node: 'Node', depth: int) -> None:
            if node is None:
                return
            if depth == len(pre):  # node 是这一层最左边的节点
                pre.append(node)
            else:  # pre[depth] 是 node 左边的节点
                pre[depth].next = node  # node 左边的节点指向 node
                pre[depth] = node
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)  # 根节点的深度为 0
        return root
```
