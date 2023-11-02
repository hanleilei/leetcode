# Integer Break

[[dp]] [[math]]

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

## Example 1

```text
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
```

## Example 2

```text
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
```

## Constraints

```text
2 <= n <= 58
```

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        case = [0, 0, 1, 2, 4, 6, 9]
        if n < 7:
            return case[n]
        dp = case + [0]*(n-6)
        for i in range(7, n + 1):
            dp[i] = dp[i-3] * 3
        return dp[-1]
```

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        f = [1] * (n + 1)
        cur = 1

        for i in range(2, n+1):
            cur = f[n]
            for j in range(i, n + 1):
                f[j] = max(f[j], f[j-i]* i)
        return cur
```

或者：

```python
class Solution:
    def cuttingBamboo(self, n: int) -> int:
        dp = [1] * (n + 1)
        cur = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]*j, (i-j)*j) 
        return dp[n]
```

这破题目到最后就是数学问题了。。

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:return n - 1
        k = n // 3
        r = n % 3
        if r == 0: return pow(3, k)
        elif r == 1: return pow(3, k - 1) * 4
        else: return pow(3, k) * 2
        
```
