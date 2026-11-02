# symmetric tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

But the following [1,2,2,null,3,null,3] is not:

```
    1
   / \
  2   2
   \   \
   3    3
```

### Note

Bonus points if you could solve it both recursively and iteratively.

先想到的办法，还是递归。。和之前的题目差别多。

递归:

```cpp
class Solution {
public:
    bool check(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;
        if (!p || !q) return false;
        return p->val == q->val && check(p->left, q->right) && check(p->right, q->left);
    }
    bool isSymmetric(TreeNode* root) {
        return check(root->left, root->right);
    }
};
```

迭代：

```cpp
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        queue<TreeNode*> q;
        q.push(root->left);
        q.push(root->right);
        while (!q.empty()) {
            TreeNode* p = q.front(); q.pop();
            TreeNode* qNode = q.front(); q.pop();
            if (!p && !qNode) continue;
            if (!p || !qNode) return false;
            if (p->val != qNode->val) return false;
            q.push(p->left);
            q.push(qNode->right);
            q.push(p->right);
            q.push(qNode->left);
        }
        return true;
    }
};
```
