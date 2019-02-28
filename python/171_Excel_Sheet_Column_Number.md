# 171. Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
Credits:
Special thanks to @ts for adding this problem and creating all test cases.

###### 方法：
还是觉得pow函数是个关键，通过pow来建立计算模型

```python
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        arr = [i for i in range(1,27)]
        d = dict(zip(string.ascii_uppercase,arr))
        s = s[::-1]
        sum = 0
        for i in range(0,len(s)):
            sum += pow(26,i)*d[s[i]]
        return sum

```

上面的算法不是太好，看看下面的思路：

```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        d = dict(zip(string.ascii_uppercase, list(range(1, 27))))

        result = 0
        for i in range(len(s)) :
            result += d.get(s[i]) * 26 ** (len(s) - i - 1)

        return result

```
再来一个针对性的优化问题：

```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s[::-1]):
                total += (ord(char)-64)*26**i
        return total
```
