# First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

###### 我的算法是找到所有只出现一次的字母，然后取这些字母出现的最小位置

```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        lt = list()
        for i in range(len(s)):
            d[s[i]] = i
        from collections import Counter
        for k, v in Counter(s).items():
            if v == 1:
                lt.append(d[k])
        if lt == []:
            return -1
        return min(lt)




```
