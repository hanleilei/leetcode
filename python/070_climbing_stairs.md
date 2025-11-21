# climbing stairs

[[dp]]

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

用动态规划解决类似问题的方式了。

$$
[
dp_{i,j} =
\begin{cases} 
    dp_{i-1} + dp_{i-2}, & \text{if } i >= 2 \\
    1, & \text{if } i < 2 \\
\end{cases}
]
$$

```cpp
class Solution {
public:
    int climbStairs(int n) {
        int dp[n + 1];
        for (int i = 0; i <= n; i++){
            if (i < 2) dp[i] = 1;
            else dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
};
```

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(n + 1):
            if i >= 2:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
```

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current,
        return current
```
