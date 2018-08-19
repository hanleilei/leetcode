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

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        std::vector<int> dp;
        for(int i = 0; i <= amount; i++){
            dp.push_back(-1);
        }
        dp[0]=0;
        for (int i = 0; i <= amount; i++) {
            for (int j = 0; j < coins.size(); j++) {
                if(i-coins[j]>=0 && dp[i-coins[j]]!= -1){
                    if(dp[i] == -1 || dp[i]> dp[i-coins[j]]+1){
                        dp[i] = dp[i-coins[j]] + 1;
                    }
                }
            }
        }
        return dp[amount];
    }
};
```

再来一个快 的版本：

```c
int fast = [](){ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0); return 0;}();
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int res = INT_MAX;
        sort(coins.begin(), coins.end());
        dfs(res, coins, amount, coins.size() - 1, 0);
        return res == INT_MAX? -1: res;
    }
    void dfs(int& res, vector<int>& coins, int target, int idx, int count) {
        if (idx < 0) return;
        if (target % coins[idx] == 0) {
            res = min(res, count + target / coins[idx]);
            return;
        }
        if (count+ target / coins[idx] < res-1)
        for (int i = target / coins[idx]; i >= 0; i--) {
            //if (count + i >= res - 1) break; // pruing
            dfs(res, coins, target - i * coins[idx], idx - 1, count + i);
        }
    }
};
```
