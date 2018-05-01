# Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

当交易次数为两次，就用一维的动态规划问题。所以状态转移方程：

finalmaxprofit = max(maxprofit(0, i) + maxprofit(i+1, n)) 0<=i<n

```python

```
