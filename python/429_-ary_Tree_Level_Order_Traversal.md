# ary tree level order traversal

Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]


Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.

```python
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q, res = [root], list()
        while any(q):
            res.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return res
```
