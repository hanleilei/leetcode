# 191. Number of 1 Bits

[[bitManipulation]]

Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

## Example 1

```text
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```

## Example 2

```text
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
```

## Example 3

```text
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
```

## Constraints

```text
The input must be a binary string of length 32.
```

这类题目，如果用标准库之类的 `bin(n).count('1')` 得到答案，可能就不那么合适了，还是要用位运算。

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            n &= (n - 1)
            res += 1
        return  res
```

cpp版本：

```cpp
class Solution {
public:
    int hammingWeight(int n) {
        int res = 0;
        for (; n; n &= n - 1)
            ++res;
        return res;
    }
};
```

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        mask = 1
        for i in range(32):
            if n & mask:
                res += 1
            mask = mask << 1
        return res
```

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        for i in range(32):
            res+=(n>>i)&1
        return res
```
