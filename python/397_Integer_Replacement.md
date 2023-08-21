# Integer Replacement

Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

Example 1:

```
Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1
```

Example 2:

```
Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1
```

Example 3:

```
Input: n = 4
Output: 2
```

Constraints:

1 <= n <= 231 - 1

这样的题目，好难再面试过程中想出来，还是最后一个比较容易点。

```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n > 1:
            res += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return res
```

```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def f(n):
            if n==1:return 0
            if n<1:
                return 10**9+7
            if n & 1 ==0:
                return 1 + f(n>>1)
            else:
                return 1 + min(f(n+1),f(n-1))
        return f(n)
```

When n is even, the operation is fixed. The procedure is unknown when it is odd. When n is odd it can be written into the form n = 2k+1 (k is a non-negative integer.). That is, n+1 = 2k+2 and n-1 = 2k. Then, (n+1)/2 = k+1 and (n-1)/2 = k. So one of (n+1)/2 and (n-1)/2 is even, the other is odd. And the "best" case of this problem is to divide as much as possible. Because of that, always pick n+1 or n-1 based on if it can be divided by 4. The only special case of that is when n=3 you would like to pick n-1 rather than n+1.

```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                if (n + 1) % 4 == 0 and (n - 1 != 2):
                    n += 1
                else:
                    n -= 1
            res += 1
        return res
```
