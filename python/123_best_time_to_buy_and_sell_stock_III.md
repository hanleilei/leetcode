# Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

当交易次数为两次，就用一维的动态规划问题。所以状态转移方程：

finalmaxprofit = max(maxprofit(0, i) + maxprofit(i+1, n)) 0<=i<n

遍历所有的划分可能，就能找出最终的最大利润。如果每次都将时间段直接调用Best Time to Buy and Sell Stock的方法，复杂的用例会超时。我们可以先从前往后遍历，并缓存最多进行一次交易所能获取的最大利润；再从后往前遍历计算最多进行一次交易所能获取的最大利润，与对应的缓存相加就是在一次划分下的最大利润。

```python
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_max_profit = 0
        n = len(prices)
        first_profits = [0] * n
        min_price = float('inf')

        for i in range(n):
            min_price = min(min_price, prices[i])
            total_max_profit = max(total_max_profit, prices[i] - min_price)
            first_profits[i] = total_max_profit

        max_profit = 0
        max_price = float('-inf')
        for i in range(n - 1, 0, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price - prices[i])
            total_max_profit = max(total_max_profit, max_profit + first_profits[i - 1])
        return total_max_profit
```

在来一个泛化的版本，交易次数为k：

```Python
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        k = 2
        dp = [0 for i in range(len(prices))]
        for i in range(1, k + 1):
            temp_max = dp[0] - prices[0]
            for j in range(1, len(prices)):
                temp = temp_max
                temp_max = max(temp_max, dp[j] - prices[j])
                dp[j] = max(dp[j - 1], prices[j] + temp)
        return dp[len(prices) - 1]
    
```


```Python
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = -sys.maxsize
        sell1 = 0
        buy2 = -sys.maxsize
        sell2 = 0
        for p in prices:
            buy1 = buy1 if buy1 > -p else -p
            sell1 = sell1 if sell1 >  buy1+p else buy1+p
            buy2 = buy2 if buy2 > sell1-p else sell1-p
            sell2 = sell2 if sell2 > buy2+p else buy2+p
        return sell2
```

```Python
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1, hold2 = float("-inf"), float("-inf")
        release1, release2 = 0, 0
        for i in prices:
            release2 = max(release2, hold2 + i)
            hold2 = max(hold2, release1-i)
            release1 = max(release1, hold1+i)
            hold1 = max(hold1, -i)
        return release2
```
