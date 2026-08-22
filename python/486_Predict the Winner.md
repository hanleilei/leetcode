# Predict the Winner

You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

Example 1:

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return false.

Example 2:

Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Constraints:

    1 <= nums.length <= 20
    0 <= nums[i] <= 10^7

## 一、寻找子问题

设玩家 1 的最终得分为 A，玩家 2 的最终得分为 B。如果 A≥B，那么玩家 1 获胜，否则玩家 2 获胜。

A≥B 可以变形为 A−B≥0，这意味着，我们只需关注得分之差 A−B 的值，而不是 A 和 B 具体是多少。维护一个值，比维护两个值更容易。

用得分之差的观点来看，为了获胜，玩家 1 需要最大化 A−B，玩家 2 需要最小化 A−B（或者说最大化 B−A）。

也就是说，每个玩家都需要最大化自己的得分减去对手的得分。

看示例 1，nums=[1,5,2]。枚举玩家 1 在第一回合移除的整数：

    移除最左边的整数 nums[0]=1，那么需要解决的问题是：剩余整数为 nums′=[5,2]，玩家 2（现在是先手）的得分减去玩家 1（现在是后手）的得分最大是多少。
    移除最右边的整数 nums[2]=2，那么需要解决的问题是：剩余整数为 nums′=[1,5]，玩家 2（现在是先手）的得分减去玩家 1（现在是后手）的得分最大是多少。

这些问题都是和原问题相似的、规模更小的子问题，可以用递归解决。

虽然我们找到了子问题，但是，原问题和子问题的关系是什么？怎么利用子问题的结果，算出原问题的答案？

## 二、状态定义与状态转移方程

因为要解决的问题都形如「对于 nums 中的一个连续子数组，计算先手得分减去后手得分的最大值」，所以定义 dfs(i,j) 表示当剩余整数为 nums 的子数组 [i,j] 时，先手得分减去后手得分的最大值。

例如 nums=[1,5,2]。在第一回合，如果玩家 1 移除最右边的 nums[2]，那么玩家 1 的得分增加 nums[2]。

子问题为：对于 nums′=[1,5]，玩家 2 选哪个整数，可以最大化「玩家 2 的得分减去玩家 1 的得分」。注意这里的得分是在 nums′ 上的得分。

对于 nums′，设玩家 2 的得分为 B′，玩家 1 的得分为 A′，那么子问题可以表示为
$$dfs(0,1)=B′−A′$$

我们要计算的原问题可以表示为
$$dfs(0,2)=A−B$$

二者的关系是什么？

由于 A=nums[2]+A′, B=B′，所以有
$$dfs(0,2)=A−B=(nums[2]+A′)−B′=nums[2]−(B′−A′)=nums[2]−dfs(0,1)$$

即 $dfs(0,2)=nums[2]−dfs(0,1)$

这样就找到了原问题和子问题的关系。

一般地，如果剩余整数为 nums 的子数组 [i,j]，我们枚举先手移除的整数：

- 如果移除的是最左边的整数 nums[i]，先手得分增加 nums[i]，这种情况下 $dfs(i,j)=nums[i]−dfs(i+1,j)$。
- 如果移除的是最右边的整数 nums[j]，先手得分增加 nums[j]，这种情况下 $dfs(i,j)=nums[j]−dfs(i,j−1)$。

这两种情况取最大值，得

$$dfs(i,j)=max(nums[i]−dfs(i+1,j),nums[j]−dfs(i,j−1))$$

递归边界：$dfs(i,i)=nums[i]$。此时只有一个整数 nums[i]，先手得分为 nums[i]，后手得分为 0，得分之差为 $nums[i]−0=nums[i]$。

递归入口：$dfs(0,n−1)$，这是原问题，也是答案。

## 三、递归搜索 + 保存递归返回值 = 记忆化搜索

考虑到整个递归过程中有大量重复递归调用（递归入参相同）。由于递归函数没有副作用，同样的入参无论计算多少次，算出来的结果都是一样的，因此可以用记忆化搜索来优化：

    如果一个状态（递归入参）是第一次遇到，那么可以在返回前，把状态及其结果记到一个 memo 数组中。
    如果一个状态不是第一次遇到（memo 中保存的结果不等于 memo 的初始值），那么可以直接返回 memo 中保存的结果。

⚠注意：memo 数组的初始值一定不能等于要记忆化的值！例如初始值设置为 0，并且要记忆化的 dfs(i,j) 也等于 0，那就没法判断 0 到底表示第一次遇到这个状态，还是表示之前遇到过了，从而导致记忆化失效。一般初始化为 −1，但本题 dfs(i,j) 的返回值可能是负数，可以初始化为 ∞ 或 −∞。

```python
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            return max(nums[i] - dfs(i + 1, j), nums[j] - dfs(i, j - 1))

        return dfs(0, len(nums) - 1) >= 0
```

复杂度分析

- 时间复杂度：$O(n^2)$，其中 n 是 nums 的长度。由于每个状态只会计算一次，记忆化搜索的时间复杂度 = 状态个数 × 单个状态的计算时间。本题状态个数为 $O(n^2)$，单个状态的计算时间为 O(1)，所以总的时间复杂度为 $O(n^2)$。
- 空间复杂度：$O(n^2)$。保存多少状态，就需要多少空间。

## 四、1:1 翻译成递推

我们可以去掉递归中的「递」，只保留「归」的部分，即自底向上计算。

具体来说，f[i][j] 的定义和 dfs(i,j) 的定义是完全一样的，都表示当剩余整数为 nums 的子数组 [i,j] 时，先手得分减去后手得分的最大值。

相应的递推式（状态转移方程）也和 dfs 一样：

$$f[i][j]=max(nums[i]−f[i+1][j],nums[j]−f[i][j−1])$$

初始值 `f[i][i]=nums[i]`，翻译自递归边界 `dfs(i,i)=nums[i]`。

答案为 `f[0][n−1]`，翻译自递归入口 `dfs(0,n−1)`。

答疑

问：如何思考循环顺序？什么时候要正序枚举，什么时候要倒序枚举？

答：这里有一个通用的做法。看状态转移方程，为了计算 `f[i][j]`，一方面，必须先把 `f[i+1][j]` 算出来，那么只有 i 从大到小枚举才能做到；另一方面，必须先把 `f[i][j−1]` 算出来，那么只有 j 从小到大枚举才能做到。

```python
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = nums[i]
            for j in range(i + 1, n):
                f[i][j] = max(nums[i] - f[i+1][j], nums[j] - f[i][j - 1])
        return f[0][-1] >= 0
```

复杂度分析

- 时间复杂度：$O(n^2)$，其中 n 是 nums 的长度。
- 空间复杂度：$O(n^2)$。

五、空间优化

由于转移方程形如 完全背包，可以仿照完全背包的空间优化写法，去掉 f 的第一个维度，内层循环仍然从小到大枚举 j。

```python
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [0] * n

        for i in range(n - 1, -1, -1):
            f[i] = nums[i]
            for j in range(i + 1, n):
                f[j] = max(nums[i] - f[j], nums[j] - f[j - 1])
        return f[-1] >= 0
```

复杂度分析

- 时间复杂度：$O(n^2)$，其中 n 是 nums 的长度。
- 空间复杂度：$O(n)$。
