# Valid Palindrome

[[string]] [[2points]]

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        ss = ''.join(re.split('\W',s)).lower()
        if ss == ss[::-1]:
            return True
        else:
            return False

```

来个差不多多，不用re模块：

```Python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        ss = [i for i in s.lower() if i in string.ascii_lowercase + string.digits]
        return ss == ss[::-1]
```

two pointers:

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] not in string.ascii_letters + string.digits:
                left += 1
                continue
            if s[right] not in string.ascii_letters + string.digits:
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
```
