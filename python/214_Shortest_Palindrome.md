## Shortest Palindrome

You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

Example 1:

```
Input: s = "aacecaaa"
Output: "aaacecaaa"
```

Example 2:

```
Input: s = "abcd"
Output: "dcbabcd"
```

Constraints:

```
0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
```

还是一个比较复杂的题目，但是被 stefan 大佬直接 hack 的方法搞定了：

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

```
