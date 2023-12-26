# Remove Stones to Minimize the Total

[[heap]]

You are given a **0-indexed** integer array `piles`, where `piles[i]` represents the number of stones in the `ith` pile, and an integer `k`. You should apply the following operation **exactly** `k` times:

- Choose any `piles[i]` and **remove** `floor(piles[i] / 2)` stones from it.

**Notice** that you can apply the operation on the **same** pile more than once.

Return *the **minimum** possible total number of stones remaining after applying the* `k` *operations*.

`floor(x)` is the **greatest** integer that is **smaller** than or **equal** to `x` (i.e., rounds `x` down).

**Example 1:**

**Input:** piles = [5,4,9], k = 2
**Output:** 12
**Explanation:** Steps of a possible scenario are:

- Apply the operation on pile 2. The resulting piles are [5,4,<u>5</u>].
- Apply the operation on pile 0. The resulting piles are [<u>3</u>,4,5].
  The total number of stones in [3,4,5] is 12.

**Example 2:**

**Input:** piles = [4,3,6,7], k = 3
**Output:** 12
**Explanation:** Steps of a possible scenario are:

- Apply the operation on pile 2. The resulting piles are [4,3,<u>3</u>,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,<u>4</u>].
- Apply the operation on pile 0. The resulting piles are [<u>2</u>,3,3,4].
  The total number of stones in [2,3,3,4] is 12.

**Constraints:**

- `1 <= piles.length <= 105`
- `1 <= piles[i] <= 104`
- `1 <= k <= 105`



```python
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        p = [-i for i in piles]
        heapq.heapify(p)

        for _ in range(k):
            i = heapq.heappop(p)
            heapq.heappush(p, math.floor(i / 2))
        return abs(sum(p))
```

看看lee215的思路：

## Explanation
Use a max heap.
Each time pop the max value a,
remove a / 2 from the number of stones res
and push back the ceil half a - a / 2 to the heap.
Repeat this operation k times.


## Complexity
Time O(n + klogn)
Space O(n)

用heapreplace确实是我之前没有想到过的。

```python
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        p = [-i for i in piles]
        heapq.heapify(p)

        for _ in range(k):
            heapq.heapreplace(p, p[0]//2)
        return abs(sum(p))
```

```java
class Solution {
    public int minStoneSum(int[] A, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b)->b - a);
        int res = 0;
        for (int a : A) {
            pq.add(a);
            res += a;
        }
        while (k-- > 0) {
            int a = pq.poll();
            pq.add(a - a / 2);
            res -= a / 2;
        }
        return res;
    }
}
```

```cpp
class Solution {
public:
    int minStoneSum(vector<int>& A, int k) {
        priority_queue<int> pq(A.begin(), A.end());
        int res = accumulate(A.begin(), A.end(), 0);
        while (k--) {
            int a = pq.top();
            pq.pop();
            pq.push(a - a / 2);
            res -= a / 2;
        }
        return res;
    }
};
```


再来一个rust的方法：


```rust
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_stone_sum(piles: Vec<i32>, k: i32) -> i32 {
        let mut heap = BinaryHeap::from(piles);
        for _ in 0..k {
            let x = heap.pop().unwrap();
            heap.push((x + 1) / 2);
        }
        heap.into_iter().sum()
    }
}
```

#TODO

下面的这个写法，目前还是有点看不懂

```rust
impl Solution {
    pub fn min_stone_sum(piles: Vec<i32>, mut k: i32) -> i32 {
        let max = *piles.iter().max().unwrap() as usize;
        let mut count = vec![0; max + 1];
        for &x in piles.iter() {
            count[x as usize] += 1;
        }
        for i in (1..=max).rev() {
            if k == 0 {
                break;
            }
            let smaller = count[i].min(k);
            count[i] -= smaller;
            count[(i + 1) / 2] += smaller;
            k -= smaller;
        }
        count.iter().enumerate()
            .map(|(i, c)| i as i32 * c)
            .sum()
    }
}
```
