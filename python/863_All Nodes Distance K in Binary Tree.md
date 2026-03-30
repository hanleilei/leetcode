# All Nodes Distance K in Binary Tree

[[bfs]] [[dfs]] [[tree]]

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png)

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:

Input: root = [1], target = 1, k = 3
Output: []

Constraints:

    The number of nodes in the tree is in the range [1, 500].
    0 <= Node.val <= 500
    All the values Node.val are unique.
    target is the value of one of the nodes in the tree.
    0 <= k <= 1000

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        def dfs(n):
            if not n:
                return
            if n.left:
                adj[n.val].append(n.left.val)
                adj[n.left.val].append(n.val)
                dfs(n.left)
            if n.right:
                adj[n.val].append(n.right.val)
                adj[n.right.val].append(n.val)
                dfs(n.right)
        q = [target.val]
        dfs(root)
        visited = set()
        visited.add(target.val)
        # print(adj)
        # defaultdict(<class 'list'>, {0: [2, 1], 2: [0], 1: [0, 3], 3: [1]})
        for _ in range(k):
            sz = len(q)
            new_q = []
            for _ in range(sz):
                n = q.pop()
                for u in adj[n]:
                    if u in visited:
                        continue
                    visited.add(u)
                    new_q.append(u)
            q = new_q
        return q
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.left: 
                q.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)

            if node.right: 
                q.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)

        q = collections.deque([(target, 0)])
        visited = set([target])
        ans = []
        while q:
            node, d = q.popleft()
            if d == k:
                ans.append(node.val)
                continue

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, d+1))

        return ans
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        conn = collections.defaultdict(list)
        def connect(parent, child):
            # both parent and child are not empty
            if parent and child:
                # building an undirected graph representation, assign the
                # child value for the parent as the key and vice versa
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            # in-order traversal
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        # the initial parent node of the root is None
        connect(None, root)
        # start the breadth-first search from the target, hence the starting level is 0
        bfs = [target.val]
        seen = set(bfs)
        # all nodes at (k-1)th level must also be K steps away from the target node
        for i in range(k):
            # expand the list comprehension to strip away the complexity
            new_level = []
            for q_node_val in bfs:
                for connected_node_val in conn[q_node_val]:
                    if connected_node_val not in seen:
                        new_level.append(connected_node_val)
            bfs = new_level
            # add all the values in bfs into seen
            seen |= set(bfs)
        return bfs
```
