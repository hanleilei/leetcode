# 322. Coin Change

[[dp]] [[bfs]] [[dfs]] [[greedy]]

## Problem Description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**
```
Input: coins = [2], amount = 3
Output: -1
```

**Example 3:**
```
Input: coins = [1], amount = 0
Output: 0
```

**Constraints:**
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

---

## Solution 1: Dynamic Programming (推荐)

**思路：**
- 定义 `dp[i]` 表示凑成金额 i 所需的最少硬币数
- 状态转移：`dp[i] = min(dp[i-coin] + 1)` for all coins
- 完全背包问题的变形

**时间复杂度：** O(amount × len(coins))  
**空间复杂度：** O(amount)

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 表示凑成金额i所需的最少硬币数
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # 金额0需要0个硬币
        
        # 遍历所有金额
        for i in range(1, amount + 1):
            # 尝试每种硬币
            for coin in coins:
                if i >= coin:
                    # 状态转移：选择coin或不选
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # 如果dp[amount]没有被更新，说明无法凑成
        return dp[amount] if dp[amount] != amount + 1 else -1
```

**优化版本（更简洁）：**

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 使用 inf 作为初始值，语义更清晰
        f = [0] + [inf] * amount
        
        # 完全背包：先遍历物品（硬币），再遍历容量（金额）
        for x in coins:
            for c in range(x, amount + 1):
                f[c] = min(f[c], f[c - x] + 1)
        
        ans = f[amount]
        return ans if ans < inf else -1
```

**优化点：**
- ✅ 用 `inf` 替代 `amount + 1`，语义更明确
- ✅ 初始化更简洁：`[0] + [inf] * amount`
- ✅ 完全背包标准写法：先遍历物品，再遍历容量
- ✅ 自动满足 `c >= x` 条件，无需额外判断

---

## Solution 2: BFS (层序遍历)

**思路：**
- 将问题看作图的最短路径问题
- 从金额0开始，每次加上一个硬币作为一层
- 第一次到达目标金额时，步数即为最少硬币数
- 使用visited数组避免重复计算

**时间复杂度：** O(amount × len(coins))  
**空间复杂度：** O(amount)

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        # BFS层序遍历
        queue = [0]  # 从金额0开始
        visited = [False] * (amount + 1)
        visited[0] = True
        steps = 0
        
        while queue:
            steps += 1
            next_queue = []
            
            # 遍历当前层的所有金额
            for curr_amount in queue:
                # 尝试每种硬币
                for coin in coins:
                    new_amount = curr_amount + coin
                    
                    if new_amount == amount:
                        return steps
                    
                    # 如果新金额有效且未访问过
                    if new_amount < amount and not visited[new_amount]:
                        visited[new_amount] = True
                        next_queue.append(new_amount)
            
            queue = next_queue
        
        return -1
```

---

## Solution 3: DFS + 记忆化搜索 (推荐的DFS方法)

**思路：**
- 标准的DFS + 记忆化，避免重复计算
- memo[amount] 存储凑成该金额的最少硬币数
- 自顶向下的递归解法

**时间复杂度：** O(amount × len(coins))  
**空间复杂度：** O(amount) 递归栈 + 记忆化空间

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(remaining):
            # 基础情况
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1
            
            # 查找记忆化结果
            if remaining in memo:
                return memo[remaining]
            
            # 尝试每种硬币
            min_coins = float('inf')
            for coin in coins:
                result = dfs(remaining - coin)
                if result != -1:
                    min_coins = min(min_coins, result + 1)
            
            # 记忆化
            memo[remaining] = min_coins if min_coins != float('inf') else -1
            return memo[remaining]
        
        return dfs(amount)
```

递归搜索 + 保存计算结果 = 记忆化搜索

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, c: int) -> int:
            if i < 0:
                return 0 if c == 0 else inf
            if c < coins[i]:  # 只能不选
                return dfs(i - 1, c)
            # 不选 vs 继续选
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)

        ans = dfs(len(coins) - 1, amount)
        return ans if ans < inf else -1
```

---

## Solution 4: 位运算优化的BFS (高级技巧)

**思路：**
- 使用位运算表示可达的金额状态
- bit位为1表示该金额可达
- 通过位移操作快速计算下一层状态

**时间复杂度：** O(amount × len(coins) / 64) 位运算优化  
**空间复杂度：** O(1) 只用整数存储状态

```python
from functools import reduce

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        # 使用位表示状态，第i位为1表示金额i可达
        reachable = 1 << amount  # 初始只有金额amount可达（反向思考）
        steps = 0
        
        while reachable:
            steps += 1
            # 尝试所有硬币，计算下一层可达状态
            reachable = reduce(lambda acc, coin: acc | (reachable >> coin), coins, 0)
            
            # 检查金额0是否可达（因为是反向的）
            if reachable & 1:
                return steps
        
        return -1
```



---

## 总结与对比

| 方法 | 时间复杂度 | 空间复杂度 | 优点 | 缺点 |
|------|-----------|-----------|------|------|
| DP (Solution 1) | O(amount × n) | O(amount) | ✅ 稳定高效<br>✅ 代码简洁<br>✅ 易理解 | 需要额外数组空间 |
| BFS (Solution 2) | O(amount × n) | O(amount) | ✅ 直观理解为最短路径<br>✅ 性能稳定 | 队列操作略慢 |
| DFS + 记忆化 (Solution 3) | O(amount × n) | O(amount) | ✅ 自顶向下思路清晰<br>✅ 避免重复计算 | 递归栈开销 |
| 位运算BFS (Solution 4) | O(amount × n / 64) | O(1) | 位运算快速 | amount不能太大 |

**推荐做法（按优先级）：**
1. 🥇 **DP方法 (Solution 1)** - 面试首选，清晰、稳定、高效
2. 🥈 **DFS + 记忆化 (Solution 3)** - 自顶向下思路，适合理解递归
3. 🥉 **BFS (Solution 2)** - 图论角度理解，概念清晰

**避免的做法：**
- ❌ DFS + 贪心剪枝 (Solution 3B) - 容易TLE，面试不推荐
- ⚠️ 位运算BFS (Solution 4) - 仅限小范围amount，实用性受限

**面试建议：** 
- 先说DP思路，写出状态转移方程
- 如果面试官要求优化空间，可以讨论滚动数组
- 可以提到BFS的图论建模思路作为加分项
