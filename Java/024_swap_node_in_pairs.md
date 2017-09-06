# swap nodes in pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

使用java写出来的代码，至少链表操作和其他语言没差别。

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */  
public class Solution {  
    public ListNode swapPairs(ListNode head) {  
        ListNode p=new ListNode(0),s;  
        p.next=head;  
        head=p;  
        while(p.next!=null && p.next.next!=null){  
            s=p.next.next;  
            p.next.next=s.next;  
            s.next=p.next;  
            p.next=s;  
            p=s.next;  
        }  
        return head.next;  
    }  
}
```
