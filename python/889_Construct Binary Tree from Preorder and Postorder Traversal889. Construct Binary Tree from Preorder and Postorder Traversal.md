# Construct Binary Tree from Preorder and Postorder Traversal

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:

![](https://assets.leetcode.com/uploads/2021/07/24/lc-prepost.jpg)

Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]

## Constraints

```text
    1 <= preorder.length <= 30
    1 <= preorder[i] <= preorder.length
    All the values of preorder are unique.
    postorder.length == preorder.length
    1 <= postorder[i] <= postorder.length
    All the values of postorder are unique.
    It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
```

同类型题目有三个。。

LeetCode889 根据前序和后序遍历构造二叉树
LeetCode105 从前序与中序遍历序列构造二叉树
LeetCode106 从中序与后序遍历序列构造二叉树

不同之处一 寻找当前根节点

这一部分总的来说是在寻找可以将左右子树划分开的根节点

    前+后
    首先我们可以显然知道当前根节点为pre[pre_start],并且它在后序中的位置为post_end，因此这里我们需要找到能区分左右子树的节点。
    我们知道左子树的根节点为pre[pre_start+1]，因此只要找到它在后序中的位置就可以分开左右子树（index的含义）
    前+中
    首先我们可以显然知道当前根节点为pre[pre_start],只用找出它在中序中的位置，就可以把左右子树分开（index的含义）
    中+后
    首先我们可以显然知道当前根节点为post[post_end]，只用找出它在中序中的位置，就可以把左右子树分开（index的含义）

不同之处二 左右遍历范围

这一部分运用了一个技巧是 “两种遍历中，同一子树的节点数目是相同的”
需要说明的是在"前+后","前+中"我们都运用到了“右子树起始位置为左子树终止位置+1”，其实这个也可以运用上面这个技巧来计算出起始位置

    前+后
    后序遍历中，我们知道 左子树：[post_start,index], 右子树：[index+1, post_end-1]
    在前序遍历中，左子树起始位置为pre_start+1,左子树个数一共有(index - post_start)个，因此左子树：[pre_start+1, pre_start+1 + (index - post_start)]
    右子树起始位置为左子树终止位置+1，终止位置为pre_end，因此右子树：[ pre_start+1 + (index - post_start) + 1, pre_end]

    前+中
    中序遍历中，我们知道 左子树：[inorder_start,index-1], 右子树：[index+1, inorder_end]
    在前序遍历中，左子树起始位置为pre_start+1,左子树一共有(index-1 - inorder_start)个，因此左子树：[pre_start+1, pre_start+1 + (index-1 - inorder_start)]
    右子树起始位置为左子树终止位置+1，终止位置为pre_end，因此右子树：[ pre_start+1 + (index-1 - inorder_start) + 1, pre_end]

    中+后
    中序遍历中，我们知道 左子树：[inorder_start,index-1], 右子树：[index+1, inorder_end]
    在后序遍历中，左子树起始位置为post_start，左子树一共有(index-1 - inorder_start)个，因此左子树：[post_start, post_start + (index-1 - inorder_start)]
    右子树的终止位置为post_end - 1,右子树一共有(inorder_end - (index+1))个,因此右子树:[post_end - 1 - (inorder_end - (index+1)), post_end - 1]

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        def dfs(pre, post):
            if not pre:
                return None
            # 数组长度为1时，直接返回即可
            if len(pre)==1:  ## 这里是关键，我似乎少了这一点。。
                return TreeNode(pre[0])
            # 根据前序数组的第一个元素，创建根节点     
            root = TreeNode(pre[0])
            # 根据前序数组第二个元素，确定后序数组左子树范围
            left_count = post.index(pre[1])+1
            # 递归执行前序数组左边、后序数组左边
            root.left = dfs(pre[1:left_count+1],post[:left_count])
            # 递归执行前序数组右边、后序数组右边
            root.right = dfs(pre[left_count+1:],post[left_count:-1])
            # 返回根节点
            return root
        return dfs(pre,post)
```
