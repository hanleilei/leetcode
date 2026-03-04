# Best time to buy and sell stock

[[greedy]] [[dp]]

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

简单的有点过分了。。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        
        return max_profit
```

此时的k是无穷大了，所以就相当于每次只要有利润就卖掉，最后的结果就是所有利润的和了。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        return dp[n-1][0]
```

动态规划也可以，但是贪心是最合适的。
