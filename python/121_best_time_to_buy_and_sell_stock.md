# Best time to buy and sell stock

[[dp]]

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
Subscribe to see which companies asked this question.

很简单的东西，先判断当前迭代的值和最低价格取最小值，然后在当前迭代循环条件下，取最大利润和当前价格减去最低值之间的最大值，标准的贪心算法。

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        min_stock_price = prices[0]

        # Start off with a profit of zero
        max_profit = 0

        for price in prices:
            min_stock_price = min(min_stock_price, price)
            max_profit = max(max_profit, price - min_stock_price)

        return max_profit
```

或者，这个速度超级快。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = float(inf), float(-inf)
        profit = 0
        for p in prices:
            if p < buy:
                buy = sell = p
                continue
            if p > sell:
                sell = p
                profit = max(profit, sell-buy)
        return profit
```

换个思路，用一套思维方式来解决所有这类股票买卖问题：

1. 状态有三个维度，分别是：天数、是否持有股票、已经完成的交易次数。
2. 状态转移方程：dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][1][0] + prices[i])，dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] - prices[i])。
3. 初始化：dp[0][0][0] = 0, dp[0][1][0] = -prices[0]。
4. 最终答案：max(dp[n-1][0][0], dp[n-1][0][1])。
5. 优化空间复杂度：dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][1][0] + prices[i])，dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] - prices[i])，只需要保存前一天的状态即可。

所以对于这个题来说，状态转移方程可以简化为：profit[i][0] = max(profit[i-1][0], profit[i-1][1] + prices[i])，profit[i][1] = max(profit[i-1][1], profit[i-1][0] - prices[i])。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        # 状态：0-不持有股票，1-持有股票
        # 初始化：第0天
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]  # 第0天买入
        
        for i in range(1, len(prices)):
            # 不持有股票：之前就不持有 或 今天卖出
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # 持有股票：之前就持有 或 今天买入
            # 对于LeetCode 121，今天买入意味着从初始状态买入（因为之前不能有交易）
            dp[i][1] = max(dp[i-1][1], -prices[i])  # 注意这里不是dp[i-1][0] - prices[i]
        
        return dp[-1][0]  # 最后一天不持有股票的最大利润
```

或者可以者直接把状态转移方程写成三维的，最后取最大值即可：

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        res = 0
        profit = [[0 for i in range(3)] for i in range(len(prices))]
        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0

        for i in range(1, len(prices)):
            profit[i][0] = profit[i-1][0]
            profit[i][1] = max(profit[i-1][1], profit[i-1][0] - prices[i])
            profit[i][2] = profit[i-1][1] + prices[i]
            res = max(res, profit[i][0], profit[i][1], profit[i][2])
        return res
```

再或者，直接记录一个变量k，表示交易次数：

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices: return 0
        
        n = len(prices)
        K = 1  # 最多1次交易
        dp = [[[0, 0] for _ in range(K+1)] for _ in range(n)]
        
        for k in range(K+1):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]
        
        for i in range(1, n):
            for k in range(K, 0, -1):  # 逆序遍历k
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        
        return dp[n-1][K][0]
```

总结一下：

核心状态定义：

```
# 状态定义
dp[i][k][s]
# i: 第i天 (0 ≤ i < n)
# k: 已完成交易次数 (0 ≤ k ≤ K)
# s: 是否持有股票 (0-不持有, 1-持有)
```

状态转移方程：

```
# 今天不持有股票
dp[i][k][0] = max(
    dp[i-1][k][0],           # 昨天不持有，今天休息
    dp[i-1][k][1] + prices[i]  # 昨天持有，今天卖出
)

# 今天持有股票
dp[i][k][1] = max(
    dp[i-1][k][1],           # 昨天持有，今天休息
    dp[i-1][k-1][0] - prices[i]  # 昨天不持有，今天买入（注意k的变化）
)
```

初始化：

```
# 第0天
dp[0][0][0] = 0
dp[0][0][1] = -prices[0]  # 第0天买入
dp[0][k][0] = 0
dp[0][k][1] = -prices[0]  # 允许交易k次，第0天可以买入
```

最终答案：

```
# 最后一天不持有股票的最大利润
return max(dp[n-1][k][0] for k in range(K+1))

# 或者直接返回dp[n-1][K][0]，因为最多K次交易，最后一天不持有股票的最大利润就是答案

max(dp[n-1][k][0] for k in range(K+1))  # 最后一天不持有股票
```
