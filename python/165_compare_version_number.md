# compare version number

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.

Example 1:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
Example 2:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".
Example 3:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.

按照版本比较的要求，没有用魔法方法，略恶心。。太多的 corner 用例。。

```python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        arr1 = version1.split('.')
        arr2 = version2.split('.')

        len1 = len(arr1)
        len2 = len(arr2)
        if len1>len2:
            for x in range(len1 - len2):
                arr2.append('0')
        elif len1<len2:
            for x in range(len2 - len1):
                arr1.append('0')

        for i in range(max(len1,len2)):
            if int(arr1[i]) > int(arr2[i]):
                return 1
            elif int(arr1[i]) < int(arr2[i]):
                return -1
            else:
                if [int(t) for t in arr1] == [int(p) for p in arr2]:
                    return 0
                else:
                    continue
```

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        reversions1 = version1.split(".")
        reversions2 = version2.split(".")

        for i in range(max(len(reversions1),len(reversions2))):
            rev1 = int(reversions1[i]) if i < len(reversions1) else 0
            rev2 = int(reversions2[i]) if i < len(reversions2) else 0

            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1 
        return 0
```

时隔多年，自己的方法：

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        res = 0
        while len(v1) != len(v2):
            if len(v1) > len(v2):
                v2.append(0)
            else:
                v1.append(0)
        for i in range(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) == int(v2[i]):
                res = 0
            else:
                return -1
        return res
```

```python

```
