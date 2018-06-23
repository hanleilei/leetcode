# decode strings

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:
```
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
```

完全用stack解决，这类问题就是要理顺思路，一个小坑在于可能数字过大，需要乘法操作。

```Python
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, num, ss = list(), 0, ''
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '[':
                stack.append(ss)
                stack.append(num)
                ss = ''
                num = 0
            elif c == ']':
                cnum = stack.pop()
                ps = stack.pop()
                ss = ps + cnum * ss
            else:
                ss += c
        return ss
```
