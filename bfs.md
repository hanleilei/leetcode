# BFS

```python
def bfs(graph, start, end):
    queue = deque()
    queue.append(start)
    visited = set()
    while queue:
        node = queue.popleft()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.extend(nodes)
```

```python
def BFS(root):
    visited = set()
    queue = deque([root]) 
    queue.append([root])

    while queue: 
        node = queue.popleft() 
        visited.add(node)

        process(node) 
        nodes = generate_related_nodes(node) 
        queue.extend(nodes)

    # other processing work 
```

```cpp
// C/C++
void bfs(Node* root) {
  map<int, int> visited;
  if(!root) return ;

  queue<Node*> queueNode;
  queueNode.push(root);

  while (!queueNode.empty()) {
    Node* node = queueNode.top();
    queueNode.pop();
    if (visited.count(node->val)) continue;
    visited[node->val] = 1;

    for (int i = 0; i < node->children.size(); ++i) {
        queueNode.push(node->children[i]);
    }
  }

  return ;
}
```

```java
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> allResults = new ArrayList<>();
    if (root == null) {
        return allResults;
    }
    Queue<TreeNode> nodes = new LinkedList<>();
    nodes.add(root);
    while (!nodes.isEmpty()) {
        int size = nodes.size();
        List<Integer> results = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            TreeNode node = nodes.poll();
            results.add(node.val);
            if (node.left != null) {
                nodes.add(node.left);
            }
            if (node.right != null) {
                nodes.add(node.right);
            }
        }
        allResults.add(results);
    }
    return allResults;
}
```
