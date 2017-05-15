# group anagrams

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

Subscribe to see which companies asked this question.

## 需要用到setdefault就可以实现

```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d =dict()
        for s in strs:
            t = ''.join(sorted(s))
            d.setdefault(t,[]).append(s)
        return list(d.values())
```
