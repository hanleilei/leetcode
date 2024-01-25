# N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

## Example 1

```text
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

## Example 2

```text
Input: n = 25
Output: 1389537
```

## Constraints

```text
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
```

关爱智障。。都是阅读理解。。

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n):
            a, b, c = b, c, a + b + c
        return a + b + c
```

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        for _ in range(n - 2):
            t.append(sum(t[-3:]))
        return t[n]
```

再来一个速度快的。

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp[i % 3] = sum(dp)
        return dp[n % 3]
```
