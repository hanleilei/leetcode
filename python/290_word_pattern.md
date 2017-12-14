# word pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Credits:
Special thanks to @minglotus6 for adding this problem and creating all test cases

维护一个字典和集合，或者将字典的键和值定义相互对调。

```python
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False

        d = {}
        s = set()
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if words[i] in s:
                    return False
                else:
                    d[pattern[i]] = words[i]
                    s.add(words[i])
            elif d[pattern[i]] != words[i]:
                return False
        return True
```
