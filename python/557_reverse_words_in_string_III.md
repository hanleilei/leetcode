# Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

Subscribe to see which companies asked this question.

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = list()
        for i in s.split(" "):
            a.append(i[::-1])
        return ' '.join(a)
```

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split(" ")])
```
