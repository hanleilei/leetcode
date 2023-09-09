# Split Linked List in Parts

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

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        // 扫描链表，得到总长度 cnt
        int cnt = 0;
        ListNode tmp = head;
        while (tmp != null && ++cnt > 0) tmp = tmp.next;
        // 理论最小分割长度
        int per = cnt / k;
        // 将链表分割为 k 份（sum 代表已经被处理的链表长度为多少）
        ListNode[] ans = new ListNode[k];
        for (int i = 0, sum = 1; i < k; i++, sum++) {
            ans[i] = head;
            tmp = ans[i];
            // 每次首先分配 per 的长度
            int u = per;
            while (u-- > 1 && ++sum > 0) tmp = tmp.next;
            // 当「已处理的链表长度 + 剩余待分配份数 * per < cnt」，再分配一个单位长度
            int remain = k - i - 1;
            if (per != 0 && sum + per * remain < cnt && ++sum > 0) tmp = tmp.next;
            head = tmp != null ? tmp.next : null;
            if (tmp != null) tmp.next = null; 
        }
        return ans;
    }
}

```
