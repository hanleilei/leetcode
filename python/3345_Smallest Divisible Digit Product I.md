# Smallest Divisible Digit Product I

You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

Example 1:

Input: n = 10, t = 2

Output: 10

Explanation:

The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

Example 2:

Input: n = 15, t = 3

Output: 16

Explanation:

The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.

Constraints:

    1 <= n <= 100
    1 <= t <= 10

从 n 开始，至多循环 10 次，一定会遇到个位数为 0 的数，其数位乘积为 0，一定是 t 的倍数。

所以暴力枚举 n,n+1,n+2,…,n+9 即可。

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for x in count(n):
            prod = reduce(mul, map(int, str(x)))
            if prod % t == 0:
                return x
```
