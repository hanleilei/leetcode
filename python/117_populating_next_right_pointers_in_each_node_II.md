# populating next right pointers in each node II

[[bfs]] [[dfs]]

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

Note:

* You may only use constant extra space.
* Recursive approach is fine, implicit stack space does not count as extra space for this problem.

Example:

Given the following binary tree,

```
     1
   /  \
  2    3
 / \    \
4   5    7
```

After calling your function, the tree should look like:

```
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
```

稍微要注意一下这个题目和上一个116的区别，这里是普通二叉树，不是完美二叉树。

BFS + 链表

```Python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        p = root
        pre = None
        head = None
        while p:  # 遍历当前层的所有节点
            
            # 1. 处理左子节点
            if p.left:
                if pre:  # 如果下一层已有节点，连接它们
                    pre.next = p.left
                pre = p.left  # 更新下一层的最后节点
            
            # 2. 处理右子节点
            if p.right:
                if pre:  # 连接到下一层已有的节点
                    pre.next = p.right
                pre = p.right  # 更新下一层的最后节点
            
            # 3. 记录下一层的起始节点
            if not head:
                head = p.left or p.right  # 第一个非空子节点
            
            # 4. 移动到当前层的下一个节点
            if p.next:
                p = p.next  # 当前层还有节点
            else:
                # 当前层结束，移动到下一层
                p = head
                head = None  # 重置下一层的头节点
                pre = None   # 重置下一层的连接指针
        return root
```

思路类似，换个写法：

```Python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:
            prev, cur, next_head = None, head, None
            while cur:
                if next_head is None:
                    if cur.left:
                        next_head = cur.left
                    elif cur.right:
                        next_head = cur.right

                if cur.left:
                    if prev:
                        prev.next = cur.left
                    prev = cur.left

                if cur.right:
                    if prev:
                        prev.next = cur.right
                    prev = cur.right

                cur = cur.next
            head = next_head
        return root
```

使用dummy node，更简洁：

```Python
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

dfs:

```Python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
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

这个dfs不是太好理解，看这个执行流程：

```text
示例树:
     1
   /  \
  2    3
 / \    \
4   5    7

DFS遍历顺序（先序：根→左→右）:
1 → 2 → 4 → 5 → 3 → 7

执行过程:
┌─────┬───────┬────────────────────┬──────────────────┐
│ 节点 │ depth │ pre 数组           │ 操作              │
├─────┼───────┼────────────────────┼──────────────────┤
│ 1   │ 0     │ []                 │ pre=[1]          │
│ 2   │ 1     │ [1]                │ pre=[1,2]        │
│ 4   │ 2     │ [1,2]              │ pre=[1,2,4]      │
│ 5   │ 2     │ [1,2,4]            │ 4.next=5         │
│     │       │                    │ pre=[1,2,5]      │
│ 3   │ 1     │ [1,2,5]            │ 2.next=3         │
│     │       │                    │ pre=[1,3,5]      │
│ 7   │ 2     │ [1,3,5]            │ 5.next=7         │
│     │       │                    │ pre=[1,3,7]      │
└─────┴───────┴────────────────────┴──────────────────┘

最终连接结果:
1 → NULL
2 → 3 → NULL
4 → 5 → 7 → NULL
```

bfs:

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        dq = deque([root])
        while dq:
            for x, y in pairwise(dq):
                x.next = y
            size = len(dq)
            for _ in range(size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return root
```
