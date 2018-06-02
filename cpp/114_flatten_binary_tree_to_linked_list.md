# Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:
```
    1
   / \
  2   5
 / \   \
3   4   6
```
The flattened tree should look like:
```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

```javascript
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    TreeNode* flattenAux(TreeNode* root) {
        if(!root) return NULL;
        TreeNode *l = root->left, *r = root->right, *tmp = root;
        root->left = NULL;
        if(l) {
            tmp = flattenAux(l);
            root->right = l;
            root = tmp;
        }
        if(r) {
            tmp = flattenAux(r);
            root->right = r;
        }
        return tmp;
    }
public:
    void flatten(TreeNode* root) {
        flattenAux(root);
    }
};
```

下面的方法更简单，没有递归，没有stack：

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void flatten(TreeNode* root) {
        while (root) {
            if (root->left && root->right) {
                TreeNode* t = root->left;
                while (t->right)
                    t = t->right;
                t->right = root->right;
            }

            if(root->left)
                root->right = root->left;
            root->left = NULL;
            root = root->right;
	}

    }
};
```

还有一个第一种方法的变种，写的更简洁：

```javascript
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
  void flatten(TreeNode *root) {
    flatten(root, NULL);
  }
private:
// 把root 所代表树变成链表后，tail 跟在该链表后面
  TreeNode *flatten(TreeNode *root, TreeNode *tail) {
    if (NULL == root) return tail;
    root->right = flatten(root->left, flatten(root->right, tail));
    root->left = NULL;
    return root;
  }
};

```
