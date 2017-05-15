# Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

Credits:
Special thanks to @ts for adding this problem and creating all test cases

## 还是要理解python中的format函数和int函数实现格式转换和进制转换

```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = "{:0>32}".format(bin(n)[2:])
        s = s[::-1]
        return int(s, 2)
```
