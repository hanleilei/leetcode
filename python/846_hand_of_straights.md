# hand of straights

[[heap]]

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

Example 1:

```text
Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
```

Example 2:

```text
Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
```

Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length

简洁的方法就要是这样：

```python
class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        hand.sort()
        while hand:
            try:
                base = hand[0]
                for i in range(W):
                    hand.remove(base+i)        
            except:
                return False
        return True
```

时代变了，还是别用try catch，然后每次都争个list遍历一次，虽然限定了10000，但是还是离谱。。

```python
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        d = Counter(hand)
        min_heap = list(d.keys())
        heapq.heapify(min_heap)

        while min_heap:
            min_val = min_heap[0]

            for i in range(groupSize):
                current = min_val + i
                if current in d:
                    d[current] -= 1
                    if d[current] == 0:
                        if current != min_heap[0]:
                            return False
                        heapq.heappop(min_heap)
                else:
                    return False

        return True
```

lee215的方案，比我的巧妙：

```python
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(groupSize)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True
```

可以，不需要删除元素，不需要用heap。。
