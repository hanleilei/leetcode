#reverse string II

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
Subscribe to see which companies asked this question

## 没难度，还是要看懂题目：每2k个字符中第前面k个字符翻转，其余的不变。

```python
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lt = list()
        for i in range(0, len(s), k*2):
            lt.append(s[i:i+k][::-1])
            lt.append(s[i+k:i+k*2])
        return "".join(lt)
```
