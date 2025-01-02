# ransom note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        return not Counter(ransomNote) - Counter(magazine)
```

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = dict(Counter(ransomNote))
        mc = dict(Counter(magazine))
        for k, v in rc.items():
            if k not in mc or v> mc[k]:
                return False
        return True
```
