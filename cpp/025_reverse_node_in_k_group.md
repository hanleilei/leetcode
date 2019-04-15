# reverse node in k group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

The key idea is to keep track of the next_head while reversing the group, tail of the current group is always the start node of the group, once the group reversing is done, next_head is available, simply connect it to tail.


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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *guard = new ListNode(0);
        guard->next = head;
        head = guard;

        for ( ; ; ){
            int res_node = 0;
            ListNode *last = head->next;
            for(int j = 0; j<k; j++){
                if (last == NULL)
                    break;
                res_node += 1;
                last = last->next;
            }

            if (res_node < k)
                break;

            ListNode *first = head->next;

            for(int j = 0; j < k; j++){
                int index = k - j - 1;
                ListNode *aim = first;
                while ( index--){
                    aim = aim->next;
                }
                head->next = aim;
                head = aim;
            }
            head->next = last;
        }

        return guard->next;
    }
};
```
