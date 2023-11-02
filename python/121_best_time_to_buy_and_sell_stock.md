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
            min_stock_price = min(min_stock_price,price)
            max_profit = max(max_profit,price - min_stock_price)

        return max_profit
```
