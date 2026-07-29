# Find the Number of Subsequences With Equal GCD

[[dp]]

You are given an integer array nums.

Your task is to find the number of pairs of non-empty (seq1, seq2) of nums that satisfy the following conditions:

    The subsequences seq1 and seq2 are disjoint, meaning no index of nums is common between them.
    The of the elements of seq1 is equal to the GCD of the elements of seq2.

Return the total number of such pairs.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: nums = [1,2,3,4]

Output: 10

Explanation:

The subsequence pairs which have the GCD of their elements equal to 1 are:

    ([1, 2, 3, 4], [1, 2, 3, 4])
    ([1, 2, 3, 4], [1, 2, 3, 4])
    ([1, 2, 3, 4], [1, 2, 3, 4])
    ([1, 2, 3, 4], [1, 2, 3, 4])
    ([1, 2, 3, 4], [1, 2, 3, 4])
    ([1, 2, 3, 4], [1, 2, 3, 4])
    ([1, 2, 3, 4], [1, 2, 3, 4])
    ([1, 2, 3, 4], [1, 2, 3, 4])
    ([1, 2, 3, 4], [1, 2, 3, 4])
    ([1, 2, 3, 4], [1, 2, 3, 4])

Example 2:

Input: nums = [10,20,30]

Output: 2

Explanation:

The subsequence pairs which have the GCD of their elements equal to 10 are:

    ([10, 20, 30], [10, 20, 30])
    ([10, 20, 30], [10, 20, 30])

Example 3:

Input: nums = [1,1,1,1]

Output: 50

Constraints:

    1 <= nums.length <= 200
    1 <= nums[i] <= 200

每个子序列的 GCD 一定是某个数的约数 → 所有可能的 GCD 值最多几百个（≤200）。用 dp[j][k]表示：第一个子序列 GCD = j，第二个子序列 GCD = k​ 的方案数。j=0或 k=0表示对应子序列为空。

初始状态：dp[0][0] = 1（两个子序列都为空）。

遍历每个数 x：

- 不选：dp[j][k]保留
- 选入第一个子序列：dp[gcd(j,x)][k] += dp[j][k]
- 选入第二个子序列：dp[j][gcd(k,x)] += dp[j][k]

最终答案：所有 j>0, k>0, j==k的 dp[j][k]之和（两个子序列都非空且 GCD 相等）。

```python
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        # 1. 离散化所有可能的 GCD（含 0）
        divs = set([0])
        for x in nums:
            i = 1
            while i * i <= x:
                if x % i == 0:
                    divs.add(i)
                    divs.add(x // i)
                i += 1
        divs = sorted(divs)
        idx = {v: i for i, v in enumerate(divs)}
        d = len(divs)

        # 2. dp[j][k]：两个子序列的 GCD 分别为 j 和 k
        dp = [[0] * d for _ in range(d)]
        dp[0][0] = 1

        # 3. 逐个加入数字
        for x in nums:
            ndp = [row[:] for row in dp]
            for j_idx, j in enumerate(divs):
                for k_idx, k in enumerate(divs):
                    val = dp[j_idx][k_idx]
                    if val == 0:
                        continue
                    # 加入第一个子序列
                    nj = math.gcd(j, x)
                    ndp[idx[nj]][k_idx] = (ndp[idx[nj]][k_idx] + val) % MOD
                    # 加入第二个子序列
                    nk = math.gcd(k, x)
                    ndp[j_idx][idx[nk]] = (ndp[j_idx][idx[nk]] + val) % MOD
            dp = ndp

        # 4. 统计两个子序列都非空且 GCD 相等的方案
        ans = 0
        for i in range(1, d):
            ans = (ans + dp[i][i]) % MOD
        return ans
```

```python
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if i < 0:
                return 1 if j == k else 0
            return (dfs(i - 1, j, k) + dfs(i - 1, gcd(j, nums[i]), k) + dfs(i - 1, j, gcd(k, nums[i]))) % mod

        return (dfs(len(nums) - 1, 0, 0) - 1) % mod
```
