# Number of Substrings Containing All Three Characters

[[slidingwindow]] [[2points]]

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".

Example 3:

Input: s = "abc"
Output: 1

Constraints:

    3 <= s.length <= 5 x 10^4
    s only consists of a, b or c characters.

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {'a': -1, 'b': -1, 'c': -1}
        result = 0
        
        for i, ch in enumerate(s):
            last[ch] = i
            result += 1 + min(last['a'], last['b'], last['c'])
        
        return result
```

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mapping = defaultdict(int)
        res = left = 0
        for c in s:
            mapping[c] += 1
            while len(mapping) == 3:
                out = s[left]
                mapping[out] -= 1
                if mapping[out] == 0:
                    del mapping[out]
                left += 1
            res += left
        return res
```
