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
        if needle in haystack:
            return haystack.index(needle)

        return -1        
```

再来一个简单粗暴的：

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except:
            return -1
```

似乎做一下很小的修改，就可以将速度提高到最快：

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1

        length_needle = len(needle)
        for i in range(0,len(haystack) - length_needle + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i+length_needle] == needle:
                    return i
        return -1
```
