# Largest Substring Between Two Equal Characters

[[hash]]

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

## Example 1

```text
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
```

## Example 2

```text
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
```

## Example 3

```text
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
```

## Constraints

```text
1 <= s.length <= 300
s contains only lowercase English letters.
```

阅读理解。。

```python
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = defaultdict(list)
        res = -1
        for i, v in enumerate(s):
            d[v].append(i)
        for _, v in d.items():
            res = max(res, v[-1] - v[0] - 1)
        return res
```