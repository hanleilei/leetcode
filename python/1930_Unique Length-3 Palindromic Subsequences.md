# Unique Length-3 Palindromic Subsequences

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

## Example 1

```text
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
```

## Example 2

```text
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
```

## Example 3

```text
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
```

## Constraints

```text
3 <= s.length <= 105
s consists of only lowercase English letters.
```

直接翻译题目含义：

Explanation

For each palindromes in format of "aba", we enumerate the character on two side.

We find its first occurrence and its last occurrence, all the characters in the middle are the candidate for the midd char.

Complexity
Time O(26n)
Space O(26n)

```python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in string.ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i+1:j]))
        return res
```

改进一点：

```python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = defaultdict(list)
        res = 0
        for i, v in enumerate(s):
            d[v].append(i)
        
        for c in d.keys():
            i, j = d[c][0], d[c][-1]
            if i > -1:
                res += len(set(s[i+1:j]))
        return res
```

思路：
1. 确定每个字符的第一次出现和最后一次出现的位置
2. 确定中间的字符的个数
3. 遍历所有的字符，把中间的字符的个数加起来.

```python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        mapping = defaultdict(list)
        for index, val in enumerate(s):
            mapping[val].append(index)
        
        for k, vals in mapping.items():
            if len(vals) == 1:
                continue
            start, end = vals[0], vals[-1]
            res += len(set(s[start+1:end]))
        return res
```
