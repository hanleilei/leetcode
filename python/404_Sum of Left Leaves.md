# Sum of Left Leaves

[[tree]] [[bfs]] [[dfs]]

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:

![1](https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg)

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
```

```python
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        stack = [(root, 0)]
        while stack:
            root, pos = stack.pop()
            if pos and not root.left and not root.right:
                total += root.val
            if root.left:
                stack.append((root.left, 1))
            if root.right:
                stack.append((root.right, 0))

        return total
```

```python
class Solution:
    total = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:        
        def treeTraverse(root, leftNode):
            if root == None:
                return
            if leftNode and not root.left and not root.right:
                self.total += root.val
            treeTraverse(root.left, True)
            treeTraverse(root.right, False)
        
        treeTraverse(root, False)
        return self.total
```

参看下这个： https://leetcode.com/problems/sum-of-left-leaves/solutions/1558055/c-python-recursive-iterative-dfs-bfs-morris-traversal-o-1-w-explanation-beats-100/

## ✔️ Solution - I (Recursive DFS)

One way we could solve this problem is using simple DFS traversal technique while keeping track of whether the current node is a left child or not.

- We start at root node. A boolean parameter isLeft is initialized to false denoting that root node is not left child.
- Recursively explore the left child nodes by setting the isLeft=true and right child nodes by setting isLeft=false.
- If the current node is a leaf node and isLeft=true, we return the node's value. Otherwise, we return 0.

```python
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, isLeft):
            if not root: return 0
            if not root.left and not root.right:
                return root.val if isLeft else 0
            return dfs(root.left, True) + dfs(root.right, False)
        return dfs(root, False)
```

One-Liner

```python
int sumOfLeftLeaves(TreeNode* root, bool isLeft = false) {
    return !root ? 0 : !root -> left && !root -> right ? (isLeft ? root -> val : 0) : sumOfLeftLeaves(root -> left, true) + sumOfLeftLeaves(root -> right, false);
}
```

- **Time Complexity**: O(N), where N is the number of nodes in the given binary tree. It is a standard DFS traversal technique where each node is visited once.
- **Space Complexity** : O(H), where H is the height of given binary tree. It is required for implicit recursive stack space. H = logN in case of a complete binary tree and H=N in case of a skewed tree.

## ✔️ Solution - II (Iterative DFS)

We can also solve the above using an iterative version of DFS.

```python
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s, ans = deque([(root, False)]), 0
        while s:
            cur, isLeft = s.pop()
            if not cur.left and not cur.right and isLeft:
                ans = ans + cur.val
            if cur.right: 
                s.append((cur.right, False))
            if cur.left: 
                s.append((cur.left, True))
        return ans
```

- **Time Complexity**: O(N)
- **Space Complexity** : O(H)

## ✔️ Solution - III (BFS)

Another way to solve this problem is using BFS traversal technique with keeping track of whether current node is left child or not.

- We start at root node and push it along with the isLeft parameter set to false into a queue
- Iteratively pop the front nodes from queue. If it is a leaf node, add to the final sum if the corresponding isLeft parameter is true.
- Iteratively push the left and right child nodes into the queue till it becomes empty

```python
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q, ans = deque([(root, False)]), 0
        while q:
            cur, isLeft = q.popleft()
            if not cur.left and not cur.right and isLeft:
                ans = ans + cur.val
            if cur.right:
                q.append((cur.right, False))
            if cur.left: 
                q.append((cur.left, True))
        return ans
```

- **Time Complexity**: O(N)
- **Space Complexity** : O(W), where W is the maximum width of tree. In case of complete binary tree, the maximium nodes stored in queue will be (N+1)/2 ≅ O(N) and in case of skewed tree where all nodes are lopsided to one end, queue will store 1 node at max.

## ✔️ Solution - IV (Morris Traversal)

This solution involves using the morris traversal technique to solve the problem. The advantage of this traversal is that we can traverse the tree in O(1) space complexity. The basic idea is to link predecessors to root nodes so we can trace it back once we have traversed a side without need of maintaining a stack. You can also find some good explanation here or check out my previous 129. Sum Root to Leaf Numbers post where I have posted an image of steps involved in morris traversal to get better idea of working.

```python
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        while root:
            if root.left:
                pre, isLeft = root.left, True
                while pre.right and pre.right != root:
                    pre = pre.right
                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    if pre == root.left and not pre.left:
                        ans = ans + pre.val
                    root = root.right
            else:
                root = root.right
        return ans
```

- **Time Complexity**: O(N), each node is visited once.
- **Space Complexity** : O(1), we are not maintaining any stack or queue and just iterate the whole tree using pointer manipulations within the given tree.
