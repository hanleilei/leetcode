# dfs

递归写法

```python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
        # already visited 
        return 
    
    visited.add(node) 

    # process current node here. 
    # ...
    for next_node in node.children(): 
        if next_node not in visited: 
            dfs(next_node, visited)
```

迭代写法：

```python
def DFS(self, root): 

    if tree.root is None: 
        return [] 

    visited, stack = [], [root]

    while stack: 
        node = stack.pop() 
        visited.add(node)

        process (node) 
        # 生成相关的节点
        nodes = generate_related_nodes(node) 
        stack.push(nodes) 

    # other processing work 
    # ...
```

tree的DFS：

```python
def dfs(self, tree):
    if tree.root is None:
        return []
    visited, stack = [], [tree.root]
    while stack:
        node = stack.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)

        # other processing work
        # ...
```

cpp

```cpp
//C/C++
//递归写法：
map<int, int> visited;

void dfs(Node* root) {
  // terminator
  if (!root) return ;

  if (visited.count(root->val)) {
    // already visited
    return ;
  }

  visited[root->val] = 1;

  // process current node here. 
  // ...
  for (int i = 0; i < root->children.size(); ++i) {
    dfs(root->children[i]);
  }
  return ;
}

//非递归写法：
void dfs(Node* root) {
  map<int, int> visited;
  if(!root) return ;

  stack<Node*> stackNode;
  stackNode.push(root);

  while (!stackNode.empty()) {
    Node* node = stackNode.top();
    stackNode.pop();
    if (visited.count(node->val)) continue;
    visited[node->val] = 1;


    for (int i = node->children.size() - 1; i >= 0; --i) {
        stackNode.push(node->children[i]);
    }
  }

  return ;
}
```

java

```java
// Java
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> allResults = new ArrayList<>();
        if(root==null){
            return allResults;
        }
        travel(root,0,allResults);
        return allResults;
    }


    private void travel(TreeNode root,int level,List<List<Integer>> results){
        if(results.size()==level){
            results.add(new ArrayList<>());
        }
        results.get(level).add(root.val);
        if(root.left!=null){
            travel(root.left,level+1,results);
        }
        if(root.right!=null){
            travel(root.right,level+1,results);
        }
    }
```
