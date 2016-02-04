# compare version number
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
Credits:
Special thanks to \@ts for adding this problem and creating all test cases.

#### 按照版本比较的要求，没有用魔法方法，略恶心。。太多的 corner 用例。。

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
