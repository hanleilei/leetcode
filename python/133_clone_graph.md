# clone graph

[[graph]]

Given the head of a graph, return a deep copy (clone) of the graph. Each node in the graph contains a label (int) and a list (List[UndirectedGraphNode]) of its neighbors. There is an edge between the given node and each of the nodes in its neighbors.


OJ's undirected graph serialization (so you can understand error output):
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.


As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.


Visually, the graph looks like the following:
```
       1
      / \
     /   \
    0 --- 2
         / \
         \_/
```
Note: The information about the tree serialization is only meant so that you can understand error output if you get a wrong answer. You don't need to understand the serialization to solve the problem

```python
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        visited = {}
        first = UndirectedGraphNode(node.label)
        visited[node.label] = first
        stack = [node]
        while stack:
            top = stack.pop()
            for n in top.neighbors:
                if n.label not in visited:
                    visited[n.label] = UndirectedGraphNode(n.label)
                    stack.append(n)
                visited[top.label].neighbors.append(visited[n.label])
        return first
```

dfs + memo:

```python
class Solution:
    def __init__(self):
        self.clone_nodes = {}  # 存储每一个克隆过的节点
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None    # 空节点不克隆
        if node.val in self.clone_nodes:
            return self.clone_nodes[node.val]    # 克隆了的节点不重复克隆
        
        clone_node = Node(node.val)    # 创建一个克隆后的节点
        self.clone_nodes[node.val] = clone_node       # 存储克隆节点
        for neighbor in node.neighbors:
            # 克隆节点 克隆 被克隆节点的邻接列表
            clone_node.neighbors.append(self.cloneGraph(neighbor))
        return clone_node
```

bfs:

```python
class Solution:        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None    # 空节点不拷贝
        clone_nodes = {node.val: Node(node.val)}  # 存储每一个拷贝过的节点，并克隆起点节点
        queue = deque([node])     # 用于广度优先搜索的队列，且起点节点入队
        while queue:
            cur = queue.popleft()     # 从队列中获取一个待处理的节点
            clone_node = clone_nodes[cur.val]   # 待处理的节点一定是克隆好了的，直接获取其克隆节点
            for neighbor in cur.neighbors:
                # 处理当前节点的邻接节点
                if neighbor.val not in clone_nodes:
                    clone_nodes[neighbor.val] = Node(neighbor.val)  # 如果邻接节点未拷贝，则拷贝
                    queue.append(neighbor)      # 未拷贝的节点说明还没有处理，加入队列等待处理
                clone_node.neighbors.append(clone_nodes[neighbor.val])  # 将邻接节点的拷贝节点加入当前节点的克隆节点的邻接列表
        return clone_nodes[node.val]    # 返回起点节点的克隆节点
```