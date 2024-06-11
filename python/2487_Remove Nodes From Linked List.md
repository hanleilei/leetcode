# Remove Nodes From Linked List

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

## Example 1

![1](https://assets.leetcode.com/uploads/2022/10/02/drawio.png)

```text
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
```

## Example 2

```text
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
```

## Constraints

```text
    The number of the nodes in the given list is in the range [1, 105].
    1 <= Node.val <= 105
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        while head is not None:
            st.append(head)
            head = head.next
        while st:
            if head is None or st[-1].val >= head.val:
                st[-1].next = head
                head = st[-1]
            st.pop()
        return head
```
