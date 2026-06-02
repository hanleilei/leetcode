# Super Egg Drop

[[dp]] [[dfs]]

You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.

Example 1:

Input: k = 1, n = 2
Output: 2

Explanation:
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.

Example 2:

Input: k = 2, n = 6
Output: 3

Example 3:

Input: k = 3, n = 14
Output: 4

Constraints:

    1 <= k <= 100
    1 <= n <= 10^4

动态规划的经典题目，状态转移方程是：

$$dp(K, N) = \min_{1 \le i \le N} \left( \max(dp(K-1, i-1),\; dp(K, N-i)) + 1 \right)$$

dfs(i−1,j−1)+1是鸡蛋碎了能确定的楼层数，dfs(i−1,j)+dfs(i−1,j−1)+1是鸡蛋没碎能确定的楼层数，两者取最大值就是dfs(i−1,j)+dfs(i−1,j−1)+1

```cpp
class Solution {
public:
    int superEggDrop(int k, int n) {
        //i次操作 j个鸡蛋
        vector<vector<int>> memo(1,vector<int>(k+1,-1));
        auto dfs = [&](auto&& dfs,int i, int j)->int
        {
            if (i == 0 || j == 0) return 0;
            if (memo[i][j] >= 0) return memo[i][j];
            int res = dfs(dfs, i - 1, j - 1) + 1 + dfs(dfs,i - 1, j);
            memo[i][j] = res;
            return res;
        };
        for (int i = 1;; i++)
        {
            vector<int> t(k+1, -1);
            memo.push_back(t);
            if (dfs(dfs, i, k) >= n) return i;
        }
        return -1;
    }
};
```

1:1递推：

```cpp
class Solution {
public:
    int superEggDrop(int k, int n) {
        //i次操作 j个鸡蛋
        vector<vector<int>> dp(1, vector<int>(k + 1));
        for (int i = 1;; i++)
        {
            vector<int> t(k + 1);
            dp.push_back(t);
            for (int j = 1; j <= k; j++)
            {
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] + 1;
            }
            if (dp[i][k] >= n) return i;
        }
        return -1;
    }
};

```

滚动数组优化：

```cpp
class Solution {
public:
    int superEggDrop(int k, int n) {
        //i次操作 j个鸡蛋
        vector<int> dp(k + 1);
        for (int i = 1;; i++)
        {
            for (int j = k; j >=1 ; j--)
            {
                dp[j] = dp[j] + dp[j - 1] + 1;
            }
            if (dp[k] >= n) return i;
        }
        return -1;
    }
};
```
