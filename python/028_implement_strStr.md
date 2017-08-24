# Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

##### 基本用的算是穷举法，非常土，下次有机会看下kmp算法。注意corner case

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) <= 0:
            return 0
        if len(haystack) <= 0 or len(haystack) < len(needle) or needle not in haystack:
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
```

或者直接用python自带的index方法：

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = -1

        if needle in haystack:
            index = haystack.index(needle)

        return index        
```
