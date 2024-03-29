# last stone weight

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

## Example 1:

```
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
```

## Example 2:

```
Input: stones = [1]
Output: 1
```
## Constraints:

* 1 <= stones.length <= 30
* 1 <= stones[i] <= 1000

很经典的heap问题：

```java
class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue <Integer> q = new PriorityQueue<>(Comparator.reverseOrder());
        for (int i: stones){ q.offer(i);}
        while(q.size()> 1){
            for (int sz = q.size(); sz > 1; sz -= 2){
                int diff = q.poll() - q.poll();
                q.offer(diff);
            }
        }
        return q.peek();
    }
}
```

换一个写法：

```java
class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b)-> b - a);
        for (int a : stones)
            pq.offer(a);
        while (pq.size() > 1)
            pq.offer(pq.poll() - pq.poll());
        return pq.poll();
    }
}
```