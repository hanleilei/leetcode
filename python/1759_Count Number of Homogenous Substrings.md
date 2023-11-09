# Count Number of Homogenous Substrings

Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

## Example 1

```text
Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
```

## Example 2

```text
Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".
```

## Example 3

```text
Input: s = "zzzzz"
Output: 15
```

## Constraints

```text
1 <= s.length <= 105
s consists of lowercase letters.
```

还是用groupby的方式最好，想一下之前遇到的题目，压缩字符串，如果按照那样的方式写，很麻烦。

```python
class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        for c, g in itertools.groupby(s):
            n = len(list(g))
            res += (n + 1) * n // 2
        return res % (10 ** 9 + 7)
```
