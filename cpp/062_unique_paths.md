# unique path

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![](https://leetcode.com/static/images/problemset/robot_maze.png)

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100

```c++
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n + 1, 0);
        dp[1] = 1;

        for (int i = 0; i < m; ++i) {
            for (int j = 1; j <= n; ++j) {
                dp[j] += dp[j - 1];
            }
        }
        return dp.back();
    }
};
```

题目可以转化为下面的问题：

求m - 1个白球，n - 1个黑球的排列方式
公式为：C(m + n - 2, n - 1)

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            m, n = n, m
        mul = lambda x, y: reduce(operator.mul, range(x, y), 1)
        return mul(m, m + n - 1) / mul(1, n)
```
