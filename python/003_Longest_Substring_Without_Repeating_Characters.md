# Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question

找出最长序列的长度，一个可行的办法是转换成ascii码，然后遍历字符串，

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxlen = 0
        hashtable = [-1 for i in range(256)]
        for i in range(len(s)):
            if hashtable[ord(s[i])] != -1:
                while start <= hashtable[ord(s[i])]:
                    hashtable[ord(s[start])] = -1
                    start += 1
            if i - start + 1 > maxlen:
                maxlen = i - start + 1
            hashtable[ord(s[i])] = i
        return maxlen
```
