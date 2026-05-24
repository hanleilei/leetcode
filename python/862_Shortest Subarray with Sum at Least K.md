# Shortest Subarray with Sum at Least K

[[prefixSum]]

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1

Example 2:

Input: nums = [1,2], k = 4
Output: -1

Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3

 

Constraints:

    1 <= nums.length <= 10^5
    -10^5 <= nums[i] <= 10^5
    1 <= k <= 10^9

在计算前缀和的同时去计算答案，这需要在双端队列中额外存储前缀和的值。

由于前缀和的初始值 0 在遍历 nums 之前就算出来了，因此需要在遍历之前，往双端队列中插入前缀和 0 及其下标 −1。

    注 1：为什么是 −1？因为上面遍历的是 s，下面遍历的是 nums，这两者的下标偏移了一位。
    注 2：该写法在 nums 是一个流的时候也适用。


```python
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = inf
        cur = 0
        q = deque([(0, -1)])
        for i, x in enumerate(nums):
            cur += x
            while q and cur - q[0][0] >= k:
                res = min(res, i - q.popleft()[1])
            while q and q[-1][0] >= cur:
                q.pop()
            q.append((cur, i))
        return res if res < inf else -1
```
