# Concatenation of Consecutive Binary Numbers

[[math]]

Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1.

Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.

Constraints:

    1 <= n <= 10^5

```python
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7 
        res = 0
        
        for i in range(1, n + 1):
            # 计算当前数的二进制长度
            length = i.bit_length()
            # 将结果左移 length 位，然后加上 i
            res = ((res << length) + i) % mod
            
        return res
```

我的脑子只能想到上面的暴力解法，直接把 1 到 n 的二进制字符串拼接起来，然后转换成十进制数，最后取模。

对于下面的解法，首先要理解一下数学公式：
$$\sum_{i=l}^{r} i \cdot q^i = r \cdot \frac{q^{r+1} - 1}{q - 1} - \frac{q - m \cdot q^{r+1} + (m - 1) \cdot q^{r+2}}{(q - 1)^2}$$  

其中 $m = r - l + 1$，$q$ 是一个大于 1 的整数。
更详细的内容，看灵神的解答：`https://leetcode.cn/problems/concatenation-of-consecutive-binary-numbers/solutions/511016/golang-jian-ji-xie-fa-by-endlesscheng-2cg5/`

```python
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 0
        w = 1
        while (1 << (w - 1)) <= n:
            l = 1 << (w - 1)
            r = min((1 << w) - 1, n)
            m = r - l + 1
            q = 1 << w
            pow_q = pow(q, m, MOD)
            inv_q1 = pow(q - 1, -1, MOD)
            s = r * (pow_q - 1) * inv_q1 - (q - m * pow_q + (m - 1) * pow_q * q) * inv_q1 * inv_q1
            ans = ans * pow_q + s
            w += 1
        return ans % MOD
```
