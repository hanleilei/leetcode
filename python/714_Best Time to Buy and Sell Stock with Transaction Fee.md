# Best Time to Buy and Sell Stock with Transaction Fee

[[dp]]

ou are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

**Note**: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

## Example 1

```text
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
```

## Example 2

```text
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
```

## Constraints

- 1 <= prices.length <= 5 * 104
- 1 <= prices[i] < 5 * 104
- 0 <= fee < 5 * 104

先来一个速度最快的，注意elif语句：

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_p = prices[0] + fee
        res = 0
        
        for p in prices:
            if min_p < p:
                res += p-min_p
                min_p = p
            # min_p = min(min_p, p + fee)
            elif p+fee < min_p:
                min_p = p + fee
        
        return res
```

再来一个比较容易懂的方案：

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        profit = 0
        buy_price = prices[0]

        for i in range(1, len(prices)):
            buy_price = min(buy_price, prices[i])
            if prices[i] - buy_price - fee > 0:
                profit += prices[i] - buy_price - fee
                buy_price = prices[i] - fee
        return profit
```
