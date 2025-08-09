# Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

正则表达式问题

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        return " ".join(re.split("\s+", s.strip())[::-1])
```

经典的双指针，不用任何标准库：

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        res = ''
        left, right = 0, len(s) - 1
        while s[left] == " ":
            left += 1
        while s[right] == " ":
            right -= 1
        
        while left <= right:
            index = right
            while index >= left and s[index] != " ":
                index -= 1
            for i in range(index + 1, right + 1):
                res += s[i]
            
            if index > left:
                res += " "
            while index >= left and s[index] == " ":
                index -= 1
            right = index
        return res
```

标准库

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        strs = s.split()
        strs.reverse()
        return ' '.join(strs)
       
```
