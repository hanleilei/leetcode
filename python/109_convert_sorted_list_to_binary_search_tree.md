# convert sorted list to binary search tree

[[tree]]

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
```
      0
     / \
   -3   9
   /   /
 -10  5
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        # here we get the middle point,
        # even case, like '1234', slow points to '2',
        # '3' is root, '12' belongs to left, '4' is right
        # odd case, like '12345', slow points to '2', '12'
        # belongs to left, '3' is root, '45' belongs to right
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root
        
        
```

再来一个和上一个题目类似方案。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = list()
        while head:
            nums.append(head.val)
            head = head.next
            
        def helper(left, right):
            if left > right:
                return None
            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = helper(left,mid-1)
            root.right = helper(mid+1, right)
            return root
        return helper(0,len(nums)-1)
```
