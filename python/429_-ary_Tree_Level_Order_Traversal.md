# ary tree level order traversal

[[tree]]

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:

![Narytreeexample image](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:

![Sample 4 964 image](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]

两个数组：

```python
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = [root]
        while q:
            ans.append([node.val for node in q])
            q = [c for node in q for c in node.children]
        return ans
```

双端队列：

```python
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root])
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                q.extend(node.children)
            ans.append(vals)
        return ans
```

dfs：

```python
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.max_depth = 0
        self.level_map = defaultdict(list)       

        if root is None:
            return []

        self.dfs(root, 0)

        ans = []
        for d in range(self.max_depth + 1):
            ans.append(self.level_map[d])
        return ans

    def dfs(self, node: 'Node', depth: int) -> None:
        self.max_depth = max(self.max_depth, depth)
        self.level_map[depth].append(node.val)

        for child in node.children:
            self.dfs(child, depth + 1)
```

这个dfs的方法，有点迷，因为n叉树的层次遍历，直接用bfs就很简单了，用dfs反而麻烦一些。不过也能理解为，是把每一层的节点值，按照深度存储在一个map里，最后再按深度顺序输出。
