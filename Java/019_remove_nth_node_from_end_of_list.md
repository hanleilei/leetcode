# Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

**好吧，我不是一次性过去的，现在算是理解双指针的含义了，整个程序分成三部分：**

1. 设定一个指针先走 n 步，然后记录位置
2. 再来一个指针从头开始，两个指针齐头并进
3. 第一个指针找到链表的末尾，第二个指针所处地位之就是所要删除的元素。

```java
**
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode fast, slow, dummy = new ListNode(0);
        fast = dummy;
        slow = dummy;
        dummy.next = head;

        for (int i = 0;i < n + 1; i++){
            fast = fast.next;
        }
        while(fast != null){
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return dummy.next;

    }
}
```
