# ugly number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.

```python
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
```

```python
class Solution:
    ugly = sorted(2**a * 3**b * 5**c for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ugly[n - 1]
```

再来一个速度最快的：

```python
class Solution:
    cnt, nums = 1, [1]
    loc2 = loc3 = loc5 = 0
    while cnt < 1690:
        next_item = min(nums[loc2]*2, nums[loc3]*3, nums[loc5]*5)
        nums.append(next_item)
        if nums[loc2]*2 == next_item:
            loc2 += 1
        if nums[loc3]*3 == next_item:
            loc3 += 1
        if nums[loc5]*5 == next_item:
            loc5 += 1
        cnt += 1

    def nthUglyNumber(self, n):
        if n > 0 and n <= len(self.nums):
            return self.nums[n-1]
```

再来一个超级棒的，用 heap：

```python
class Solution:
    def nthUglyNumber(self, n):
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

上面 heap 的方法非常容易理解
