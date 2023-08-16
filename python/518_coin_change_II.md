# coin change II

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Example 1:

```
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

Example 2:

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

Example 3:

```
Input: amount = 10, coins = [10]
Output: 1
```

Note:
```
You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
```

本题目可以使用BFS和动态规划，还是动态规划的方法，先建立一个数组，长度可能比需要的长度大一些，然后最后返回的是数组的最后一个元素。中间的过程就是不断的迭代累加，对于数组的元素进行更新。

直接一步到位，来一个超过100%的提交：

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount - coin + 1):
                if dp[i]:
                    dp[i + coin] += dp[i]
        return dp[amount]
```

从这个代码可以看到影响时间的几个方面：
1. 数组生成的时候，不要用加号.
2. 在做遍历的时候，尽量选取较小的组合，如嵌套的range语句.
