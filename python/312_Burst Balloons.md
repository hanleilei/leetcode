# Burst Balloons

[[dp]]

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = `[3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []`
coins =  `3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167`

Example 2:

Input: `nums = [1,5]`
Output: 10

Constraints:

    n == nums.length
    1 <= n <= 300
    0 <= nums[i] <= 100

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]
        
        @lru_cache(None)
        def solve(left: int, right: int) -> int:
            if left >= right - 1:
                return 0
            
            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            
            return best

        return solve(0, n + 1)
```

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(2, n):
            for j in range(n - i):
                r = j
                c = i + j
                maxim = float("-inf")
                for k in range(r + 1, c):
                    value = dp[r][k] + dp[k][c] + nums[r] * nums[k] * nums[c]
                    if value > maxim:
                        maxim = value
                dp[r][c] = maxim

        return dp[0][-1]
```
