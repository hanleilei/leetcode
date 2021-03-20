Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

### Example 1:
```
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
```

### Example 2:
```
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
```

### Example 3:
```
Input: s = "triplepillooooow"
Output: 5
```

### Example 4:
```
Input: s = "hooraaaaaaaaaaay"
Output: 11
```

### Example 5:
```
Input: s = "tourist"
Output: 1
```

先来一个标准库的groupby版本

```Python
class Solution:
    def maxPower(self, s: str) -> int:
        return max(len(list(b)) for a, b in itertools.groupby(s))
```

再来一个类似题目的移植。

```Python
class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        s += "#"
        i = 1
        counter = 1
        while i < len(s):
            if s[i] == s[i-1]:
                counter += 1
            else:
                ans = max(ans, counter)
                counter = 1
            i += 1
        return ans
```
