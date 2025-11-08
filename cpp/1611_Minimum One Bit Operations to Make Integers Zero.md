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


```c++
class Solution {
public:
    int minimumOneBitOperations(int n) {
        return minimumOneBitOperations_multi(n, 0);
    }
    int minimumOneBitOperations_multi(int n, int res = 0) {
        if (n == 0) return res;
        int b = 1;
        while ((b << 1) <= n)
            b = b << 1;
        return minimumOneBitOperations_multi((b >> 1) ^ b ^ n, res + b);
    }
};
```
