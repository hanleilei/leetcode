# remove link list elements

[[linkedlist]]

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

使用“哑节点”记录链表头部, 循环遍历链表时使用pre, cur记录上一个元素和当前元素

```python
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = dummy = ListNode(-1, head)

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
```

自己手搓一个哑节点, 直接在原链表上修改, 不需要pre, cur两个指针, 只需要一个指针p

```python
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p = dummy = ListNode(-1, head)

        while p and p.next:
            while p.next and p.next.val == val:
                p.next = p.next.next
            p = p.next
        return dummy.next
```
