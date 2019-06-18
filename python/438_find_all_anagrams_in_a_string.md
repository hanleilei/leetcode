# find all anagrams in a string

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```
Example 2:
```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

简单而且直白的算法实现滑动窗口。

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s += "$"
        size = len(p)
        seen = dict()
        d = dict()
        res = list()
        for i in p:
            seen[i] = seen.get(i, 0) + 1

        for j in s[:size]:
            d[j] = d.get(j, 0) + 1

        for k in range(size, len(s)):
            if d == seen: #compare the 2 dict, if equal, there are anagram
                res.append(k - size)
            d[s[k]] = d.get(s[k], 0) + 1# this line and below are update the dict, make it as sliding window..
            if d[s[k-size]] == 1:
                del d[s[k-size]]
            else:
                d[s[k-size]] = d.get(s[k-size], 0) - 1

        return res
```
