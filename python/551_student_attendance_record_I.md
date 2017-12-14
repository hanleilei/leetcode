# student attendance record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False


```python
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        d = dict(Counter(s))
        if ('L' in d and d['L'] > 2) or ('A' in d and d['A'] > 1):
            return False
        else:
            return True
```
或者下面更简练的方法：

```python
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s.count('A') <= 1) and ('LLL' not in s)

```

```python
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return not (s.count('A') > 1 or 'LLL' in s)
```

```python
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return not re.search('A.*A|LLL', s)
```
