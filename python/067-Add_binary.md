# Add binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

#### 简单。。

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(eval('0b'+a) +eval('0b'+b))[2:]
```

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(str(a), 2) + int(str(b), 2))[2:]
```
