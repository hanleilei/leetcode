# Longest Duplicate Substring

Given a string `s`, consider all *duplicated substrings*: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return **any** duplicated substring that has the longest possible length. If `s` does not have a duplicated substring, the answer is `""`.

**Example 1:**

**Input:** s = "banana"
**Output:** "ana"

**Example 2:**

**Input:** s = "abcd"
**Output:** ""

**Constraints:**

- `2 <= s.length <= 3 * 104`
- `s` consists of lowercase English letters.



这个居然可以用二分法。。


```python
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        a = [ord(c) - ord('a') for c in s]
        mod = 2 ** 63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, a[:L], 0)
            seen = {cur}
            for i in range(L, len(s)):
                cur = (cur * 26 + a[i] - a[i-L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
        
        res, lo, hi = 0, 0, len(s)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return s[res: res + lo]
```
