# super ugly numbers

[[heap]]

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

```
Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
             super ugly numbers given primes = [2,7,13,19] of size 4.
```

# Note

* 1 is a super ugly number for any given primes.
* The given numbers in primes are in ascending order.
* 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
* The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

和264一样，来一个超级棒的，用heap：

```python
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        import heapq
        visited = set([1])
        heap = [1]
        res = None

        for _ in range(n):
            res = heapq.heappop(heap)
            for i in [2,3,5]:
                if res * i not in visited:
                    heapq.heappush(heap, res*i)
                    visited.add(res*i)
        return res
```

上面heap的方法非常容易理解，但是问题在于速度慢，并且内存占用大，下面看这个方法：

```python
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        p = [1] * n
        idx = [0] * k
        fct = [0] * n

        pq = [(primes[i], i) for i in range(k)]
        heapq.heapify(pq)

        for m in range(1, n):
            p[m], i = heapq.heappop(pq)
            idx[i] += 1
            fct[m] = i
            while fct[idx[i]] > i:
                idx[i] += 1
            heapq.heappush(pq, (primes[i] * p[idx[i]], i))
        return p[-1]
```
