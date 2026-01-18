# Find Duplicate Subtrees

[[tree]] [[dfs]] [[hashtable]]

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:
```
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
```
The following are two duplicate subtrees:
```
      2
     /
    4

```
and
```
    4
```
Therefore, you need to return above trees' root in the form of a list.

## 解法1: 序列化 + 哈希表

**核心思路**：将每个子树序列化成字符串，用哈希表记录每种子树出现的次数。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = collections.defaultdict(int)
        res = []
        
        def serialize(node):
            if not node:
                return "#"
            # 序列化格式: 左子树,右子树,根节点值
            serial = f"{serialize(node.left)},{serialize(node.right)},{node.val}"
            count[serial] += 1
            if count[serial] == 2:  # 第二次出现时加入结果
                res.append(node)
            return serial
        
        serialize(root)
        return res
```

**复杂度分析**：
- Time: O(n²) - 每个节点访问一次，序列化字符串操作 O(n)
- Space: O(n²) - 哈希表存储序列化字符串

## 解法2: ID映射优化（Stefan's Solution）

**优化点**：用唯一ID代替长字符串，减少空间和时间开销。

参考 [Stefan 的分析](https://leetcode.com/problems/find-duplicate-subtrees/discuss/106016/O(n)-time-and-space-lots-of-analysis)

```python
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        trees = defaultdict()
        trees.default_factory = trees.__len__  # 为每个新序列分配唯一ID
        count = defaultdict(int)
        result = []
        
        def lookup(node):
            if node:
                # 使用元组 (节点值, 左子树ID, 右子树ID) 作为键
                uid = trees[(node.val, lookup(node.left), lookup(node.right))]
                count[uid] += 1
                if count[uid] == 2:  # 第二次出现时加入结果
                    result.append(node)
                return uid
            return None  # 空节点返回None
        
        lookup(root)
        return result
```

**为什么更高效？**
- 用整数ID代替字符串，比较和存储更快
- `(val, left_id, right_id)` 作为key，空间 O(1) vs 字符串 O(n)

**复杂度分析**：
- Time: O(n) - 每个节点访问一次，元组操作 O(1)
- Space: O(n) - 存储 n 个节点的ID映射

## 解法3: 后序遍历 + 计数器

```python
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node):
            if not node:
                return "null"
            
            # 后序遍历：左 -> 右 -> 根
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 构造当前子树的唯一标识
            subtree = f"({left})({right}){node.val}"
            
            seen[subtree].append(node)
            return subtree
        
        seen = defaultdict(list)
        dfs(root)
        return [nodes[0] for nodes in seen.values() if len(nodes) > 1]
```

**复杂度分析**：
- Time: O(n²) - 字符串拼接
- Space: O(n²) - 存储序列化字符串

## 方法对比

| 方法 | 时间复杂度 | 空间复杂度 | 推荐度 |
|------|----------|----------|--------|
| 序列化 + 哈希表 | O(n²) | O(n²) | ⭐⭐⭐ |
| ID映射优化 | O(n) | O(n) | ⭐⭐⭐⭐⭐ |
| 后序遍历 | O(n²) | O(n²) | ⭐⭐⭐ |

**面试推荐**：ID映射优化方案（解法2），时间和空间都是最优的。
