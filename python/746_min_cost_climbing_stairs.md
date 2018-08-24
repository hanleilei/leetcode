# min cost climbing stairs

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
```
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
```
Example 2:
```
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
```
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

还是动态规划的思路，首先写出状态转移方程：dp[i] = min(dp[i-1]， dp[i-2]） + cost[i]

```python
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        return min(dp[i], dp[i-1])

```

下面是一个速度优化过的版本。但是，每次这些几乎类似的逻辑，速度都是在很诡异的跳来跳去。。

```python
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        mins = [0 for i in range(len(cost))]
        mins[0:2] = cost[0:2]
        for i in range(2,len(cost)):
            mins[i] = cost[i] + min(mins[i-1], mins[i-2])
        return min(mins[-1], mins[-2])

```
