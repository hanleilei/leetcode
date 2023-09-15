# Maximum Binary Tree

You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

Example 1:

![](https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg)

Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:

```
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.
```

Example 2:
![](https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg)

```

Input: nums = [3,2,1]
Output: [3,null,2,null,1]
```

Constraints:

```
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
All integers in nums are unique.
```

最终这类问题最好的办法还是[单调栈](https://leetcode.com/problems/maximum-binary-tree/solutions/258364/python-o-n-solution-with-explanation/?orderBy=most_votes)

Intuition
We want to optimize from O(n^2) time complexity, O(nlogn) doesn't seem like very promising, so we try O(n). Basically, if we need O(n) solution, we can only have constant operation during the traverse of the list. Therefore, we need something the keep track of the traversing memory. We then brainstorm several data structures that can help us keep track of this kind of memory.
What memory do we need? We need to remember the max node rather than trying to find them each time. So we need something that has an order and hierarchy. Stack comes in very naturally for this need given its characteristics. All we need to do is to force an order by ourselves.

Algorithm:
We keep track of a stack, and make sure the numbers in stack is in decreasing order.

For each new num, we make it into a TreeNode first.
Then:

If stack is empty, we push the node into stack and continue
If new value is smaller than the node value on top of the stack, we append TreeNode as the right node of top of stack.
If new value is larger, we keep poping from the stack until the stack is empty OR top of stack node value is greater than the new value. During the pop, we keep track of the last node being poped.
After step 2, we either in the situation of 0, or 1, either way, we append last node as left node of the new node.
After traversing, the bottom of stack is the root node because the bottom is always the largest value we have seen so far (during the traversing of list).

Space complexity:
Worst O(n) in the case that the list is sorted in descending order.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stk = []
        for i in nums:
            node = TreeNode(i)
            while stk and i > stk[-1].val:
                curr = stk.pop()
                node.left = curr
            if stk:
                stk[-1].right = node
            stk.append(node)
        return stk[0]
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        stack = []  #build a decreasing stack
        for i in nums:
            node = TreeNode(i)
            lastpop = None

            while stack and stack[-1].val < i:  #popping process
                lastpop = stack.pop()
            node.left = lastpop

            if stack:
                stack[-1].right = node
            stack.append(node)

        return stack[0]
```

或者，我们可以参考labuladong的方案，直接从题目含义出手：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)

    # 定义：将 nums[lo..hi] 构造成符合条件的树，返回根节点
    def build(self, nums: List[int], lo: int, hi: int) -> TreeNode:
        # base case
        if lo > hi:
            return None

        # 找到数组中的最大值和对应的索引
        index, maxVal = -1, -sys.maxsize
        for i in range(lo, hi+1):
            if maxVal < nums[i]:
                index = i
                maxVal = nums[i]

        # 先构造出根节点
        root = TreeNode(maxVal)
        # 递归调用构造左右子树
        root.left = self.build(nums, lo, index - 1)
        root.right = self.build(nums, index + 1, hi)
        
        return root
```

或者不用辅助函数

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # 找到数组中的最大值
        maxVal = max(nums)
        index = nums.index(maxVal)
        
        root = TreeNode(maxVal)
        # 递归调用构造左右子树
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        
        return root
```