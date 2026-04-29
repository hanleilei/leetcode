# Reverse Bits

Reverse bits of a given 32 bits signed integer.

Example 1:

Input: n = 43261596

Output: 964176192

Explanation:

Integer Binary
43261596 00000010100101000001111010011100
964176192 00111001011110000010100101000000

Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:

Integer Binary
2147483644 01111111111111111111111111111100
1073741822 00111111111111111111111111111110

Constraints:

0 <= n <= 2^31 - 2
n is even.

还是要理解python中的format函数和int函数实现格式转换和进制转换

```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = "{:0>32}".format(bin(n)[2:])
        s = s[::-1]
        return int(s, 2)
```

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # 确保处理32位
        for i in range(32):
            # 将当前结果左移一位，为新位腾出位置
            res <<= 1
            # 取n的最低位加到res
            res |= (n & 1)
            # n右移一位
            n >>= 1
        return res
```

从低到高逐个检查n的第i位，如果是1，则在res的第(31 - i)位置上设置1。最后返回res即可。

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res, mask = 0, 1
        for i in range(32):
            if n & mask:
                res |= 1 << (31 - i)
            mask <<= 1
        return res
```
