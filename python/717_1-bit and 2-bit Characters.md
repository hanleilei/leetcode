# 1-bit and 2-bit Characters

We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

Constraints:

1 <= bits.length <= 1000
bits[i] is either 0 or 1.

还是阅读理解的问题。。

```python
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if not bits:
            return True
        n = len(bits)
        i = 0

        while i < n:
            if i == n - 1:   return True
            if bits[i] == 0:
                i += 1
            elif bits[i] == 1:
                i += 2
        return False
```

### 题意

有一个包含 a 和 b 的字符串 s，把其中的 a 替换成 0，b 替换成 1,0，得到一个 01 序列 bits。

你需要把 bits 还原回字符串 s，判断 s 的最后一个字符是不是 a。

### 思路

根据题意，两种字符替换后的第一个数字一定是不同的，一个是 0，另一个是 1。

换句话说，我们可以通过 bits[0] 确定字符串的第一个字符：

如果 bits[0]=0，那么是 a，把 bits[0] 去掉。
如果 bits[0]=1，那么是 b，把 bits[0] 和 bits[1] 去掉。
重复该过程，直到 bits 剩下至多一个数字。

### 分类讨论：

如果最后剩下一个数字，由于题目保证 bits[n−1]=0，所以字符串的最后一个字符是 a，返回 true。
如果最后没有剩下数字，说明字符串的最后一个字符是 b，返回 false。
示例 1 是 [1,0]+[0]，满足要求。

示例 2 是 [1,1]+[1,0]，不满足要求。


```python
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n - 1:  # 循环直到剩下至多一个数字
            i += bits[i] + 1  # 如果 bits[i] == 1 则跳过下一位
        return i == n - 1  # 注意题目保证 bits[n-1] == 0，无需判断
```
