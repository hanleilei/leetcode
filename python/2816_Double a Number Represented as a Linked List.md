# Double a Number Represented as a Linked List

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

Example 1:

![](https://assets.leetcode.com/uploads/2023/05/28/example.png)

Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
Example 2:

![](https://assets.leetcode.com/uploads/2023/05/28/example2.png)

Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 

Constraints:

The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.

```python
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        node = head
        while node:
            node.val = (node.val * 2) % 10
            if node.next and node.next.val > 4:
                node.val += 1
            node = node.next
        return head 
```

```java
class Solution {
    public ListNode doubleIt(ListNode head) {
        if(head.val > 4){
            head = new ListNode(0, head);
        }
        for (ListNode node = head; node != null; node = node.next){
            node.val = (node.val * 2) % 10;
            if (node.next != null && node.next.val > 4){
                node.val++;
            }
        }
        return head;
    }
}
```

```cpp
class Solution {
public:
    ListNode* doubleIt(ListNode* head) {
        if (head->val > 4){
            head = new ListNode(0,  head);
        }
        for(ListNode* node = head; node; node = node->next){
            node->val = (node->val * 2) % 10;
            if (node->next && node->next->val > 4){
                node->val++;
            }
        }
        return head;
    }
};
```

```go
func doubleIt(head *ListNode) *ListNode {
    if head.Val > 4 {
        head = &ListNode{0, head}
    }
    for cur := head; cur != nil; cur = cur.Next {
        cur.Val = cur.Val * 2 % 10
        if cur.Next != nil && cur.Next.Val > 4 {
            cur.Val++
        }
    }
    return head
}
```

```rust
impl Solution {
    pub fn double_it(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut head = Some(Box::new(ListNode {val: 0, next: head}));
        let mut prev = head.as_mut().unwrap();
        while let Some(digit) = prev.next.as_mut() {
            let double = digit.val * 2;
            digit.val = double % 10;
            prev.val += double / 10;
            prev = digit;
        }
        if head.as_ref().unwrap().val == 0 {
            head = head.unwrap().next;
        }
        head
    }
}
```
