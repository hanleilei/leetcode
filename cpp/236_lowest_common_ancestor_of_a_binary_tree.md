# lowest common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
```
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
```

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        std::vector<TreeNode*> path;
        std::vector<TreeNode*> node_p_path;
        std::vector<TreeNode*> node_q_path;
        int finish = 0;

        preorder(root, p, path, node_p_path, finish);

        path.clear();
        finish = 0;
        preorder(root, q, path, node_q_path, finish);

        int path_len = 0;

        if( node_p_path.size() < node_q_path.size() ){
            path_len = node_p_path.size();
        }else{
            path_len = node_q_path.size();
        }
        TreeNode *result = 0;
        for (int i = 0; i < path_len; i++){
            if(node_p_path[i] == node_q_path[i]){
                result = node_p_path[i];
            }
        }
        return result;

    }
    void preorder(TreeNode* node, TreeNode* search, std::vector<TreeNode*> &path, std::vector<TreeNode*>  &result, int &finish){
        if(!node || finish){
            return;
        }
        path.push_back(node);
        if(node == search){
            finish = 1;
            result = path;
        }
        preorder(node->left, search, path, result, finish);
        preorder(node->right, search, path, result, finish);
        path.pop_back();
    }
};
```
