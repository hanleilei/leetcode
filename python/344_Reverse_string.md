# reverse string

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

##### 很简单，回文。。

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

```
双指针
```python
class Solution:
   def reverseString(self, s):
       """
       :type s: str
       :rtype: str
       """
       s = [i for i in s]
       l, r = 0, len(s)-1

       while l < r:
           s[l], s[r] = s[r], s[l]
           l += 1
           r -= 1
       return ''.join(s)

```
