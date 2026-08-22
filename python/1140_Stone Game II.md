# Stone Game II

Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:

Input: piles = [2,7,9,4,4]

Output: 10

Explanation:

    If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 stones in total.
    If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 stones in total.

So we return 10 since it's larger.

Example 2:

Input: piles = [1,2,3,4,5,100]

Output: 104

Constraints:

    1 <= piles.length <= 100
    1 <= piles[i] <= 10^4

```python
class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        f = [[0] * (n + 1) for _ in range(n)]
        col_q = [deque() for _ in range(n + 1)]  # 每列的滑动窗口最小值（窗口向上滑动）

        s = 0
        for i in range(n - 1, -1, -1):
            s += piles[i]
            diag_q = deque()  # 斜向的滑动窗口最小值（窗口向右下滑动）
            for m in range(1, i // 2 + 2):
                if i + m * 2 >= n:  # 全拿
                    f[i][m] = s
                    continue

                # f[i+1][m] 进入列窗口
                q = col_q[m]
                while q and f[q[-1]][m] >= f[i + 1][m]:
                    q.pop()
                q.append(i + 1)

                # 队首离开列窗口
                if q[0] > i + m:
                    q.popleft()

                # f[i+m*2-1][m*2-1] 和 f[i+m*2][m*2] 进入斜向窗口
                for x in range(m * 2 - 1, m * 2 + 1):
                    while diag_q and f[i + diag_q[-1]][diag_q[-1]] >= f[i + x][x]:
                        diag_q.pop()
                    diag_q.append(x)

                # 队首离开斜向窗口
                if diag_q[0] <= m:
                    diag_q.popleft()

                f[i][m] = s - min(f[q[0]][m], f[i + diag_q[0]][diag_q[0]])

        return f[0][1]
```

```python
class Solution:
    def stoneGameII(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 2, -1, -1):
            nums[i] += nums[i+1]
        
        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= n:
                return nums[i]
            return nums[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        return dp(0, 1)
```

```python
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        s, n = 0, len(piles)
        f = [[0] * (n + 1) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            s += piles[i]
            for m in range(1, i // 2 + 2):
                if i + m * 2 >= n:  # 全拿
                    f[i][m] = s
                else:
                    f[i][m] = s - min(f[i + x][max(m, x)] for x in range(1, m * 2 + 1))
        return f[0][1]
```

```python
class Solution:
    def stoneGameII(self, s: List[int]) -> int:
        n = len(s)
        for i in range(n - 2, -1, -1):
            s[i] += s[i + 1]  # 后缀和

        @cache
        def dfs(i: int, m: int) -> int:
            if i + m * 2 >= n:  # 全拿
                return s[i]
            return s[i] - min(dfs(i + x, max(m, x)) for x in range(1, m * 2 + 1))

        return dfs(0, 1)
```
