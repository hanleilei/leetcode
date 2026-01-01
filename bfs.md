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