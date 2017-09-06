# swap nodes in pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

```CPP
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode *newHead = new ListNode(0);  
        newHead->next = head;  
        ListNode *pre = newHead, *cur = head;  
        int cnt = 1;  
        while (cur != NULL && cur->next != NULL) {  
            // swap curNode and curNode->next  
            pre->next = cur->next;  
            cur->next = pre->next->next;  
            pre->next->next = cur;  

            // go over two nodes  
            pre = cur;  
            cur = cur->next;  
        }  
        head = newHead->next;  
        delete newHead;  
        return head;  
    }
};
```

一个传说中最搞笑的方法：

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(!head || !head->next) return head;
        ListNode* p = head->next;
        head->next = swapPairs(p->next);
        p->next = head;
        return p;
    }
};

```
