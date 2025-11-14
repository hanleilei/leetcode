# coin change

# coin change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

这个问题在leetcode和lintcode这两个oj上都有，但是由于test case的不同，相同的代码，在两边运行结果完全不同。很怪异，下面是一个最快速的版本：

```python
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        len_coins, result = len(coins), amount+1

        def countCoins(index, target, count):
            nonlocal result
            if count + math.ceil(target/coins[index]) >= result:
                return

            if target % coins[index] == 0:
                result = count + target//coins[index]
                return

            if index == len_coins - 1:
                return

            for i in range(target//coins[index], -1, -1):
                countCoins(index+1, target - coins[index]*i, count+i)

        countCoins(0, amount, 0)
        return -1 if result > amount else result

```

在来一个stefan大大的bfs版本：

```python
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval <= amount:
                        if not visited[newval]:
                            if newval == amount:
                                return nc
                            visited[newval] = True
                            value2.append(newval)
            value1, value2 = value2, []
        return -1

```

再来一个dp的版本：

```python
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        rs = [amount+1] * (amount+1)
        rs[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)

        if rs[amount] == amount+1:
            return -1
        return rs[amount]

```

DFS的版本：

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        lenc, self.res = len(coins), float('inf')

        def dfs(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (self.res-count): # if hope still exists
                    dfs(i, rem-coins[i], count+1)

        for i in range(lenc):
            dfs(i, amount, 0)
        return self.res if self.res < float('inf') else -1
```

再来一个bfs的版本：

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        dp = 1<<amount
        ans = 0
        while dp:
            ans+=1
            temp = 0
            for coin in coins:
                temp |= dp>>coin

                if temp & 1:
                    return ans
            dp = temp
        return -1
```
