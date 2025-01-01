# target sum

[[dp]] [[dfs]] [[backtracking]] [[medium]]

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

```text
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:

1. The length of the given array is positive and will not exceed 20.
2. The sum of elements in the given array will not exceed 1000.
3. Your output answer is guaranteed to be fitted in a 32-bit integer.

```python
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        count = {0: 1}
        for x in nums:
            d = {}
            for s in count:
                d[s + x] = d.get(s + x, 0) + count[s]
                d[s - x] = d.get(s - x, 0) + count[s]
            count = d
        return count.get(S, 0)

```

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ##M--'+' N--'--'
        ##M+N=S--->M-N+M+N = S+M+N
        ##问题变为找到子集和为S+M+N/2
        if not nums:
            return 0
        sums = sum(nums)

        if (sums+target) % 2 == 1 or sums < abs(target):
            return 0
        half = (sums+target) // 2
        dp = [0 for _ in range(half+1)]
        # print(dp)
        dp[0] = 1
        for num in nums:
            for i in range(half, num-1, -1):
                 dp[i] += dp[i-num]
        return dp[half]

```
