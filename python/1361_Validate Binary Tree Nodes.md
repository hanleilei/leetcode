# Validate Binary Tree Nodes

[[bfs]] [[dfs]]

You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

## Example 1

![1](https://assets.leetcode.com/uploads/2019/08/23/1503_ex1.png)

```text
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
```

## Example 2

![2](https://assets.leetcode.com/uploads/2019/08/23/1503_ex2.png)

```text
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
```

## Example 3

![2](https://assets.leetcode.com/uploads/2019/08/23/1503_ex3.png)

```text
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
```

## Constraints

```text
n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1
```

这题目棒呆了！！！

直接上bfs：

```python
class Solution:
    def validateBinaryNodes(self, n, leftChild, rightChild):
        # find the root node, assume root is node(0) by default
        # a node without any parent would be a root node
        # note: if there are multiple root nodes => 2+ trees
        root = 0
        childrenNodes = set(leftChild + rightChild)
        for i in range(n):
            if i not in childrenNodes:
                root = i
        
        # keep track of visited nodes
        visited = set()
        # queue to keep track of in which order do we need to process nodes
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            
            # mark visited
            visited.add(node)
            
            # process node
            if leftChild[node] != -1:
                queue.append(leftChild[node])
            if rightChild[node] != -1:
                queue.append(rightChild[node])
                
        # number of visited nodes == given number of nodes
        # if n != len(visited) => some nodes are unreachable/multiple different trees
        return len(visited) == n
```

Kahn's topological sort

```python
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        for left, right in zip(leftChild, rightChild):
            if left > -1: indegree[left] += 1
            if right > -1: indegree[right] += 1
            if indegree[left] > 1 or indegree[right] > 1: return False
        queue = collections.deque(i for i, d in enumerate(indegree) if d == 0)
        if len(queue) > 1: return False
        while queue:
            node = queue.popleft()
            for child in leftChild[node], rightChild[node]:
                if child == -1: continue
                indegree[child] -= 1
                if indegree[child] == 0: queue.append(child)
        return sum(indegree) == 0
```

dfs

```python
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        for l, r in zip(leftChild, rightChild):
            if l != -1:
                indegree[l] += 1
                # if there are nodes that has more than 2+ parents, return false.
                if indegree[l] > 1:
                    return False
            if r != -1:
                indegree[r] += 1
                if indegree[r] > 1:
                    return False
        # a valid tree only has 1 root. 
        if indegree.count(0) != 1:
            return False
        
        # count nodes from root, if the total number is not n, it means there are islands, then return false.
        root = indegree.index(0)
        def count_nodes(root):
            if root == -1:
                return 0
            return 1 + count_nodes(leftChild[root]) + count_nodes(rightChild[root])
        
        return count_nodes(root) == n
```
