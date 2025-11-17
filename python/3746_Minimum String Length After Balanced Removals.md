# Minimum String Length After Balanced Removals

You are given a string s consisting only of the characters 'a' and 'b'.

You are allowed to repeatedly remove any substring where the number of 'a' characters is equal to the number of 'b' characters. After each removal, the remaining parts of the string are concatenated together without gaps.

Return an integer denoting the minimum possible length of the string after performing any number of such operations.

 

Example 1:

Input: s = "aabbab"

Output: 0

Explanation:

The substring "aabbab" has three 'a' and three 'b'. Since their counts are equal, we can remove the entire string directly. The minimum length is 0.

Example 2:

Input: s = "aaaa"

Output: 4

Explanation:

Every substring of "aaaa" contains only 'a' characters. No substring can be removed as a result, so the minimum length remains 4.

Example 3:

Input: s = "aaabb"

Output: 1

Explanation:

First, remove the substring "ab", leaving "aab". Next, remove the new substring "ab", leaving "a". No further removals are possible, so the minimum length is 1.

 

Constraints:

1 <= s.length <= 105
s[i] is either 'a' or 'b'.

只要 s 有不同字母，那么 s 一定存在相邻不同的字母，我们就可以把这两个字母（作为一个子串）移除，直到 s 只剩下一种字母为止。

比如有 3 个 a 和 2 个 b，每次消除 1 个 a 和 1 个 b，最终剩下 3−2=1 个 a。

设 s 有 k 个 a，那么有 n−k 个 b。

消除后，剩余字母个数为 ∣k−(n−k)∣=∣2k−n∣。


```python
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        return abs(s.count('a') * 2 - len(s))
```
