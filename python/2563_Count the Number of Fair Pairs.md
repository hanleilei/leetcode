# Count the Number of Fair Pairs

[[2points]] [[binarysearch]]

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

- 1 <= nums.length <= 10**5
- nums.length == n
- -109 <= nums[i] <= 10**9
- -109 <= lower <= upper <= 10**9

显然，这个是一个计算有多少个的问题，所以可以排序用二分法。先来一个TLE的：

```python
class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] >= lower and nums[i] + nums[j] <= upper:
                    ans += 1
        return ans
```

二分法：

```python
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums) - 1):
            minReq = lower - nums[i]
            maxReq = upper - nums[i]
            low = bisect_left(nums, minReq, i+1)
            high = bisect_right(nums, maxReq, i+1)
            ans += high - low
        return ans
```

双指针

```python
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def getPair(bound):
            l, r = 0, len(nums) - 1
            count = 0
            while l < r:
                curSum = nums[l] + nums[r]

                if curSum < bound:
                    count += r - l
                    l += 1
                else:
                    r -= 1
            return count

        nums.sort()
        return getPair(upper + 1) - getPair(lower)
```
