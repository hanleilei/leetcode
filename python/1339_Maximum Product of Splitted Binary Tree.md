# Maximum Product of Splitted Binary Tree

[[tree]] [[dfs]]

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

Example 1:

![](https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png)

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:

![](https://assets.leetcode.com/uploads/2020/01/21/sample_2_1699.png)

Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

Constraints:

The number of nodes in the tree is in the range [2, 5 * 10^4].
1 <= Node.val <= 10^4

就是一个后序遍历的题目：

1. 要求两棵子树和的最大乘积，那就得先求出两棵子树各自的和。
2. 分别求两棵子树的和显然很难做到，但我们可以很方便的其中一个子树的和。
3. 用整棵树的总和 减去求出的子树和，就得到了另一棵子树和。
4. 枚举所有子树，对乘积取最大。
5. 这样这道题就变成了，树的遍历 以及 对树的结点求和 两种过程的结合：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # 1. 第一步：计算整棵树的总和
        def calRootSum(node):
            if not node:
                return 0
            return node.val + calRootSum(node.left) + calRootSum(node.right)
        
        # 2. 第二步：后序遍历计算子树和，并更新最大乘积
        def subTreeSum(node):
            if not node:
                return 0
            
            # 递归获取左右子树和
            left_sum = subTreeSum(node.left)
            right_sum = subTreeSum(node.right)
            
            # 当前子树的总和
            curr_sub_sum = node.val + left_sum + right_sum
            
            # 更新全局最大乘积 (Python 自动处理大整数，不会像 C++ 那样溢出)
            # 计算：(总和 - 当前子树和) * 当前子树和
            product = (rootSum - curr_sub_sum) * curr_sub_sum
            if product > self.res:
                self.res = product
                
            return curr_sub_sum
        
        self.res = 0
        rootSum = calRootSum(root)
        subTreeSum(root)
        
        # 3. 最后取模
        return self.res % (10**9 + 7)
```


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.res = total = 0

        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            self.res = max(self.res, left * (total - left), right * (total - right))
            return left + right + root.val

        total = dfs(root)
        dfs(root)
        return self.res % (10**9 + 7)
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # 使用列表或成员变量，方便在递归中更新
        all_sums = []
        
        def get_sum(node):
            if not node:
                return 0
            # 后序遍历计算当前节点为根的子树和
            current_sum = node.val + get_sum(node.left) + get_sum(node.right)
            all_sums.append(current_sum)
            return current_sum
        
        # 1. 只进行一次 DFS，收集所有可能的子树和
        total_sum = get_sum(root)
        
        # 2. 遍历收集到的子树和，寻找最大乘积
        # 乘积函数 f(x) = x * (total - x) 是一个开口向下的抛物线
        # 我们寻找最接近 total_sum / 2 的子树和
        # max_prod = 0
        # for s in all_sums:
        #     product = s * (total_sum - s)
        #     if product > max_prod:
        #         max_prod = product
        
        # return max_prod % (10**9 + 7)
        ans = max(s * (total_sum - s) for s in all_sums)
        
        return ans % 1_000_000_007
```

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
typedef long long LL;
class Solution {
public:
    // 计算整棵树的总和
    LL calRootSum(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        return root->val + calRootSum(root->left) + calRootSum(root->right);
    }
    // 后序遍历的同时，求出子树和
    LL subTreeSum(TreeNode* root, LL rootSum, LL& ret) {
        if (root == NULL) {
            return 0;
        }
        LL leftSum = subTreeSum(root->left, rootSum, ret);
        LL rightSum = subTreeSum(root->right, rootSum, ret);
        LL subSum = root->val + leftSum + rightSum;
        // 对结果取最大
        ret = max(ret, (rootSum - subSum) * subSum);
        return subSum;
    }
    int maxProduct(TreeNode* root) {
        LL rootSum = calRootSum(root);
        LL ret = 0;
        subTreeSum(root, rootSum, ret);
        return ret % LL(1e9 + 7);
    }
};
```
