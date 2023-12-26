# decode ways

[[dp]]

A message containing letters from A-Z can be encoded into numbers using the following mapping:

    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

* "AAJF" with the grouping (1 1 10 6)
* "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

## Example 1

```text
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

## Example 2

```text
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

## Example 3

```text
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```

## Constraints

```text
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
```

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)] 
        
        # base case initialization
        # Handling s starting with '0'. Alternative: I would recommend treating as an error condition and immediately returning 0. It's easier to keep track and it's an optimization.
        dp[0] = 1 
        dp[1] = 0 if s[0] == "0" else 1   #(1)

        # Pay close attention to your comparators. For (1) you want 0 <, not 0 <= . For (2) you want 10 <=, not 10 <
        for i in range(2, len(s) + 1): 
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:    #(2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
        return dp[len(s)]
```

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

再来看看stepfan大大的解法：

```Python
def numDecodings(self, s):
    v, w, p = 0, int(s>''), ''
    for d in s:
        v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
    return w
# w tells the number of ways
# v tells the previous number of ways
# d is the current digit
# p is the previous digit
```
