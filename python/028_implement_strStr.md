# Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## Example 1

```text
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

## Example 2

```text
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

## Constraints

```text
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
```

基本用的算是穷举法，非常土，下次有机会看下kmp算法。注意corner case

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

或者find方法：

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
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
