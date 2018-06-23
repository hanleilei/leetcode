# climbing stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

## 算是大把用动态规划解决类似问题的方式了。

```cpp
class Solution {
public:
    int climbStairs(int n) {
        int a = 1, b = 2;
        if (n == 1) return a;
        if (n == 2) return b;
        int fn;
        for (int i = 3; i <= n; i++){
            fn = a + b;
            a = b;
            b = fn;
        }
        return fn;
    }
};
```

再来一个是用vector容器的版本：

```cpp
class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n+3, 0);
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i<= n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];

    }
};
```
