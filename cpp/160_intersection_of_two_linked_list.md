# intersection of two linked list

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

##### 这个实现的思路还是分别遍历两个链表，然后找到他们的长度差别，然后并排跑的比较。直接求数值的方法太low了。。。以下是实现的cpp版本：

```c++
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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        std::set<ListNode*> node_set;
        while(headA){
            node_set.insert(headA);
            headA = headA->next;
        }
        while (headB) {
            if (node_set.find(headB)!= node_set.end()) {
                return headB;
            }
            headB = headB->next;
        }
        return NULL;
    }
};
```
