# Delete Characters to Make Fancy String

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.


Example 1:

```text
Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
```

Example 2:

```text
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
```

Example 3:

```text
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
```

Constraints:

- `1 <= s.length <= 105`
- `s consists only of lowercase English letters.`

```python
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = list()
        for i in s:
            if len(res) >= 2 and res[-1] == i and res[-2] == i:
                continue
            else:
                res.append(i)

        return ''.join(res)
```

or:

```python
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = list()
        for i in s:
            if len(res) < 2 or not (res[-1] == i and res[-2] == i):
                res.append(i)
        return ''.join(res)
```

来个速度最快的：

```python
class Solution:
    def makeFancyString(self, s: str) -> str:
        ret = []
        cnt = 1
        prev = None
        for c in s:
            if c == prev:
                cnt += 1
            else:
                cnt = 1
            prev = c
            if cnt < 3:
                ret.append(c)
        return ''.join(ret)
```
