# Reverse Only Letters

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        chars = [i for i, c in enumerate(s) if c in string.ascii_letters]
        left, right = 0, len(chars) - 1
        while left < right:
            # chars[left], chars[right] = chars[right], chars[left]
            s[chars[left]], s[chars[right]] = s[chars[right]], s[chars[left]]
            left += 1
            right -= 1
        return ''.join(s)
```
