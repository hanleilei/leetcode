# Check if Number is a Sum of Powers of Three

[[maths]]

Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false

Constraints:

1 <= n <= 10**7

纯粹的数学问题：如果 n 是 3 的幂，那么 n % 3 == 0，如果 n 是 3 的幂的倍数，那么 n % 3 == 2，所以我们只需要判断 n 是否是 3 的幂的倍数即可。

Steps to Solve:

1. Convert n to its base-3 representation.
2. Check if any digit in the base-3 representation is 2.
   - If yes, return false (because it's not possible to represent n as the sum of distinct powers of three).
   - If no, return true.

```python
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
```
