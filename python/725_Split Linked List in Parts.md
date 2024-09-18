# Split Linked List in Parts

[[linkedlist]]

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

## Example 1

![](https://assets.leetcode.com/uploads/2021/06/13/split1-lc.jpg)

```text
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
```

## Example 2

![](https://assets.leetcode.com/uploads/2021/06/13/split2-lc.jpg)

```text
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
```

Constraints:

The number of nodes in the list is in the range [0, 1000].

- 0 <= Node.val <= 1000
- 1 <= k <= 50

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, current, parts = 0, head, []
        
        while current:
            length += 1
            current = current.next
        
        base_size, extra = divmod(length, k)
        current = head
        
        for _ in range(k):
            dummy = ListNode()
            part_head = dummy
            
            for _ in range(base_size + (extra > 0)):
                dummy.next, current, dummy = current, current.next, current
            
            if extra > 0:
                extra -= 1
  
            dummy.next = None
            parts.append(part_head.next)
        
        return parts
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1

        sizes, rm = [length // k] * k, length % k
        for i in range(rm):
            sizes[i] += 1

        res = []
        curr = head
        for size in sizes:
            if not size:
                res.append(None)
                continue
            res.append(curr)
            for i in range(size-1):
                curr = curr.next
            print(curr.val)
            curr.next, curr = None, curr.next
        return res

```

根据题意，我们应当近可能将链表平均分为 k 份。

我们可以采取与 (题解) 68. 文本左右对齐 类似的思路（在 68 中，填充空格的操作与本题一致：尽可能平均，无法均分时，应当使前面比后面多）。

回到本题，我们可以先对链表进行一次扫描，得到总长度 cnt，再结合需要将将链表划分为 k 份，可知每一份的 最小 分配单位为 cnt / k，最大分配单位为 (cnt / k) + 1。

然后从前往后切割出 k 份链表，由于是在原链表的基础上进行，因此这里的切分只需要在合适的位置将节点的 next 指针置空即可。

当我们需要构造出 ans[i] 的链表长度时，首先可以先分配 per 的长度，如果 已处理的链表长度 + 剩余待分配份数 * per < cnt，说明后面「待分配的份数」如果按照每份链表分配 per 长度的话，会有节点剩余，基于「不能均分时，前面的应当比后面长」原则，此时只需为当前 ans[i] 多分一个单位长度即可。
