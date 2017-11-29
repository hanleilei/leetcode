# decode ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

注意这个问题必然是动态规划来求解；

1. 初始化的值：dp[0] = 1; dp[1] = 1
2. 当s[i-2:i]这两个字符在10到26之间，但b不包括10 和 20 的时候，就有两种可能的编码方式。
3. 当s[i-2:i]为10 或者 20 时候，只有一种编码方式。
4. 此外，如果为09，则为0种编码方式，而31，则为dp[i] = dp[i-1]。

```Python
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="" or s[0]=='0': return 0
        dp=[1,1]
        for i in range(2,len(s)+1):
            if 10 <=int(s[i-2:i]) <=26 and s[i-1]!='0':
                dp.append(dp[i-1]+dp[i-2])
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:
                dp.append(dp[i-2])
            elif s[i-1]!='0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]
```
