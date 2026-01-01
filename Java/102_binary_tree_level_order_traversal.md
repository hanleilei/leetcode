# 102. Binary Tree Level Order Traversal

[[tree]] [[bfs]] [[dfs]]

## 问题描述

Given the `root` of a binary tree, return the **level order traversal**
of its nodes' values. (i.e., from left to right, level by level).

## 示例

**Example 1:**

```text
    3
   / \
  9  20
    /  \
   15   7
```

```text
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Example 2:**

```text
Input: root = [1]
Output: [[1]]
```

**Example 3:**

```text
Input: root = []
Output: []
```

## 约束条件

- The number of nodes in the tree is in the range `[0, 2000]`
- $-1000 \le \text{Node.val} \le 1000$

bfs

使用队列进行层序遍历，每次处理完一层的所有节点。

```java
class Solution {
public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        
        if(root == null) return res;
        
        queue.offer(root);
        while(!queue.isEmpty()){
            int levelNum = queue.size();
            List<Integer> subList = new LinkedList<Integer>();
            for(int i=0; i<levelNum; i++) {
                if(queue.peek().left != null) queue.offer(queue.peek().left);
                if(queue.peek().right != null) queue.offer(queue.peek().right);
                subList.add(queue.poll().val);
            }
            res.add(subList);
        }
        return res;
    }
}
```

dfs

```java
class Solution {
public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        levelHelper(res, root, 0);
        return res;
    }
    
    public void levelHelper(List<List<Integer>> res, TreeNode root, int height) {
        if (root == null) return;
        if (height >= res.size()) {
            res.add(new LinkedList<Integer>());
        }
        res.get(height).add(root.val);
        levelHelper(res, root.left, height+1);
        levelHelper(res, root.right, height+1);
    }
}
```
