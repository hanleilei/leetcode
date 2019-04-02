# Next Greater Node In Linked List

We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.



#### Example 1:
```
Input: [2,1,5]
Output: [5,5,0]
```
#### Example 2:
```
Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
```
#### Example 3:
```
Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
```
* 1 <= node.val <= 10^9 for each node in the linked list.
* The given list has length in the range [0, 10000].


这个题目和496与503基本一致，唯一的差别就是链表和数组，可以直接照搬之前的算法：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res, stack = [], []

        while head:
            # 维护一个单调递减的栈，存储在找，但是还没有找到的比他更小的数
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append((len(res), head.val))
            res.append(0)
            head = head.next
        return res
```
