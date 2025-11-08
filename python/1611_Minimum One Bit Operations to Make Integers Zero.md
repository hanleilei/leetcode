# Minimum One Bit Operations to Make Integers Zero

Given an integer n, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.

## Example 1

```text
Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.
```

## Example 2

```text
Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.
```

## Constraints

```text
0 <= n <= 109
```

没思路，看lee215的方案：

Intuition
For 1XXXXXXX,
we need to transfer it
1XXXXXXX -> ... -> 11000000 -> 1000000 -> ... -> 0


## Observation 1

```text
The two operations are undo-able.
If a -> b needs k operation,
b -> a also needs k operation.
```

## Observation 2

```text
1 -> 0 needs 1 operation,
2 -> 0 needs 3 operations,
4 -> 0 needs 7 operations,
2^k needs 2^(k+1)-1 operations.

This can be easily proved.
```

## Solution 1: Recursion

```text
1XXXXXX -> 1100000 -> 100000 -> 0

1XXXXXX -> 1100000 needs minimumOneBitOperations(1XXXXXX ^ 1100000),
because it needs same operations 1XXXXXX ^ 1100000 -> 1100000 ^ 1100000 = 0.

1100000 -> 100000 needs 1 operation.
100000 -> 0, where 100000 is 2^k, needs 2^(k+1) - 1 operations.

In total,
f(n) = f((b >> 1) ^ b ^ n) + 1 + b - 1,
where b is the maximum power of 2 that small or equals to n.
```

Time O(logn)
Space O(logn)

```python
class Solution:
    dp = {0: 0}
    def minimumOneBitOperations(self, n: int) -> int:
        if n not in self.dp:
            b = 1
            while (b << 1) <= n:
                b = b << 1
            self.dp[n] = self.minimumOneBitOperations((b >> 1) ^ b ^ n) + 1 + b - 1
        return self.dp[n]
```

## Solution 2: Iterative Solution

```text
Inspired by @endlesscheng, can be proved based on solution 2.

We iterate the binary format of n,
whenever we meet bit 1 at ith position,
we increment the result by (1 << (i + 1)) - 1.

Time O(logn)
Space O(1)
```

这个方法速度最快

```python
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n-1
        return abs(res)
```

或者来一个速度慢一点的：

```python
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            res ^= n
            n = n>>1
        return res
```

这个也可以看作是gray code（格雷码）: `https://en.wikipedia.org/wiki/Gray_code`

```
Decimal Binary Gray
0 0000 0000
1 0001 0001
2 0010 0011
3 0011 0010
4 0100 0110
5 0101 0111
6 0110 0101
7 0111 0100
8 1000 1100
9 1001 1101
10 1010 1111
11 1011 1110
12 1100 1010
13 1101 1011
14 1110 1001
15 1111 1000
```

输入gray code，返回binary

```python
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            res ^= n
            n = n>>1
        return res
```

或者：

```python
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        n ^= n >> 16
        n ^= n >>  8
        n ^= n >>  4
        n ^= n >>  2
        n ^= n >>  1
        return n
```
