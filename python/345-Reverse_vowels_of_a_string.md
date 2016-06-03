# reversed vowels of a string

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

## 无题，easy

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        rtype = list()
        v = [i for i in s if i in vowels]
        for i in s:
            if i in vowels:
                rtype += v.pop()
            else:
                rtype += i
        return ''.join(rtype)



```
