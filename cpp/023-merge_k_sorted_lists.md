023 merge k sorted lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

### 使用STL的PriorityQueue方法实现

```cpp
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0){
            return null;
        }

        int size = lists.length;
        Queue<ListNode> heap = new PriorityQueue(size, new ListNodeComparator());        

        for (int i =0; i < size; i++){
            if(lists[i]!= null){
                heap.offer(lists[i])    ;
            }            
        }
        ListNode dummy = new ListNode(-1);
        ListNode cur = dummy;
        while(!heap.isEmpty()){
            ListNode n = heap.poll();
            cur.next = n;
            cur = n;
            if (n.next != null){
                heap.offer(n.next);
            }            
        }
        return dummy.next;
    }

    public class ListNodeComparator implements Comparator<ListNode>{
        public int compare(ListNode o1, ListNode o2){
            assert o1 != null && o2 != null;
            return o1.val - o2.val;
        }
    }
}
```
