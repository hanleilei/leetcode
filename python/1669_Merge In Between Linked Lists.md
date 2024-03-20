# Merge In Between Linked Lists

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:

![](https://assets.leetcode.com/uploads/2020/11/05/fig1.png)

Build the result list and return its head.

Example 1:

![]((https://assets.leetcode.com/uploads/2024/03/01/ll.png))

Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
Example 2:

![](https://assets.leetcode.com/uploads/2020/11/05/merge_linked_list_ex2.png)

Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.

Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104

本来是阅读理解，但是自己还是的代码一直有bug。。有点无奈。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        slow = ListNode(0)
        fast = list1

        for i in range(b):
            if i == a - 1:
                slow = fast
            fast = fast.next
        slow.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = fast.next
        return list1
```

这个更容易理解。。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        fast = slow = list1
        for _ in range(a-1):
            slow = slow.next
        for _ in range(b):
            fast = fast.next
        
        slow.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = fast.next
        return list1
        
```

这个是我的代码，逻辑上一开始有点问题。。

```python
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        fast = slow = dummy = ListNode(0)

        fast.next = list1
        slow.next = list1
        for _ in range(a):
            slow = slow.next
        for _ in range(b+1):
            fast = fast.next
        slow.next = list2
        while list2.next:
            list2 = list2.next 
        list2.next = fast.next # 注意这里
        return dummy.next
```

一开始是测试结果总是多两个元素，这两个元素是a和b之间是否存在多移动一位或者少移动一位造成的。解决的方法，就是在遍历到fast的地方用b+1，最后用连接list2到list1的fast有半部分，用fast.next实现。

