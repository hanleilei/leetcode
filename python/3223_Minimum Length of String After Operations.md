# Minimum Length of String After Operations

[[maths]]

You are given a string s.

You can perform the following process on s any number of times:

Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
Delete the closest character to the left of index i that is equal to s[i].
Delete the closest character to the right of index i that is equal to s[i].
Return the minimum length of the final string s that you can achieve.

Example 1:

Input: s = "abaacbcbb"

Output: 5

Explanation:
We do the following operations:

Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".
Example 2:

Input: s = "aa"

Output: 2

Explanation:
We cannot perform any operations, so we return the length of the original string.

Constraints:

1 <= s.length <= 2 * 105
s consists only of lowercase English letters.

操作次数取决于每种字母的出现次数，与字母的位置无关。

假设某个字母出现了 c 次，那么操作后该字母最少能剩下多少？

根据题意，只有当 c≥3 时才能操作，每次操作可以把 c 减少 2。

如果 c=3,5,7,⋯ 是奇数，那么不断减 2，最终 c=1。
如果 c=4,6,8,⋯ 是偶数，那么不断减 2，最终 c=2。

这两种情况可以合并，最终剩下 `( c − 1 ) mod 2 + 1` 个字母。注意上式同时兼顾 c=0,1,2 的情况。

累加每种字母最终剩下的 c，即为答案。

```python
class Solution:
    def minimumLength(self, s: str) -> int:
        # c = Counter(s)
        # res = 0
        # for _, v in c.items():
        #     res += (v - 1 ) % 2 + 1
        # return res
        return sum((c - 1) % 2 + 1 for c in Counter(s).values())
```
