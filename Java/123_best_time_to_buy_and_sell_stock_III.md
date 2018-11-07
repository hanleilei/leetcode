# Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

超级牛的算法：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1).?page=1

The thinking is simple and is inspired by the best solution from Single Number II (I read through the discussion after I use DP).
Assume we only have 0 money at first;
4 Variables to maintain some interested 'ceilings' so far:
The maximum of if we've just buy 1st stock, if we've just sold 1nd stock, if we've just buy 2nd stock, if we've just sold 2nd stock.
Very simple code too and work well. I have to say the logic is simple than those in Single Number II.


```java
class Solution {
  public int maxProfit(int[] prices) {
      int hold1 = Integer.MIN_VALUE, hold2 = Integer.MIN_VALUE, release1 = Integer.MIN_VALUE, release2 = Integer.MIN_VALUE;
    if (prices.length == 0) return 0;
    for(int i:prices){
        hold1 = Math.max(hold1, -i);
        release1 = Math.max(release1, hold1+i);
        hold2 = Math.max(hold2, release1-i);
        release2 = Math.max(release2, hold2+i);
    }
    return release2;
  }
}
```

再来一个dp的方法：
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution

dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0..i-1]

For k transactions, on i-th day,
if we don't trade then the profit is same as previous day dp[k, i-1];
and if we bought the share on j-th day where j=[0..i-1], then sell the share on i-th day then the profit is prices[i] - prices[j] + dp[k-1, j-1] .
Actually j can be i as well. When j is i, the one more extra item prices[i] - prices[j] + dp[k-1, j] = dp[k-1, i] looks like we just lose one chance of transaction.

I see someone else use the formula dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j]), where the last one is dp[k-1, j] instead of dp[k-1, j-1]. It's not the direct sense, as if the share was bought on j-th day, then the total profit of previous transactions should be done on (j-1)th day. However, the result based on that formula is also correct, because if the share was sold on j-th day and then bought again, it is the same if we didn't trade on that day.
