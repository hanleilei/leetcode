# best time to buy and sell stock IV

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:
```
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
```

Example 2:
```
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
```


```python
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        from heapq import heapify, heappop
        profits = []
        stack = []

        p = -1
        while 1:
            v = p + 1
            while v + 1 < len(prices) and prices[v] >= prices[v+1]:
                v += 1
            p = v
            while p + 1 < len(prices) and prices[p] <= prices[p+1]:
                p += 1

            if v == p:
                break

            while stack and prices[v] <= prices[stack[-1][0]]:
                profits.append(prices[stack[-1][1]] - prices[stack[-1][0]])
                stack.pop()

            while stack and prices[p] >= prices[stack[-1][1]]:
                profits.append(prices[stack[-1][1]] - prices[v])
                v = stack[-1][0]
                stack.pop()
            stack.append((v, p))

        while stack:
            profits.append(prices[stack[-1][1]] - prices[stack[-1][0]])
            stack.pop()

        if len(profits) < k:
            return sum(profits)
        profits = [-i for i in profits]
        heapify(profits)
        result = 0
        for _ in range(k):
            result = result - heappop(profits)
        return result
```


```python
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0
        max_profit = 0
        #if k>= n/2, then it can't complete k transactions. The problem becomes buy-and-sell problem 2
        if k>=length/2:
            for i in xrange(1,length):
                max_profit += max(prices[i]-prices[i-1],0)
            return max_profit

        #max_global[i][j] is to store the maximum profit, at day j, and having i transactions already
        #max_local[i][j] is to store the maximum profit at day j, having i transactions already, and having transaction at day j
        max_global = [[0]*length for _ in xrange(k+1)]
        max_local = [[0]*length for _ in xrange(k+1)]

        #i indicates the transaction times, j indicates the times
        for j in xrange(1,length):
            cur_profit = prices[j]-prices[j-1] #variable introduced by the current day transaction
            for i in xrange(1,k+1):
                #max_global depends on max_local, so updata local first, and then global.
                max_local[i][j] = max( max_global[i-1][j-1]+max(cur_profit,0), max_local[i][j-1] + cur_profit)
                #if cur_profit <0, then the current transaction loses money, so max_local[i][j] = max_global[i-1][j-1]
                #else, it can be max_global[i-1][j-1] + cur_profit, by considering the current transaction
                #or it can be max_local[i][j-1] + cur_profit, this is to CANCEL the last day transaction and moves to the current transaction. Note this doesn't change the total number of transactions. Also, max_local[i-1] has already been considered by max_global[i-1] term
                max_global[i][j] = max(max_global[i][j-1], max_local[i][j])
                #This is more obvious, by looking at whether transaction on day j has influenced max_global or not.
        return max_global[k][-1] #the last day, the last
```
