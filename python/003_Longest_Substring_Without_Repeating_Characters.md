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

还有一个更巧妙的实现：

```Python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ind = {}
        w = 0
        m = 0
        for i in range(0, len(s)):
            c = s[i]
            if i == 0:
                ind[c] = 1
                m = 1
            else:
                if c not in ind or ind[c] < w:
                    ind[c] = i+1
                    d = i+1 - w
                    m = d if d > m else m  
                else:
                    w = ind[c]
                    ind[c] = i+1            
        return m
```

下面的版本超级快，超过了100%的提交：

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, f, i, m = 0, 0, -1, {}
        for v in s:
            i = i+1
            if v in m and m[v]>=f:
                if res<i-f:
                    res= i-f
                f = m[v] + 1
            m[v] = i
        if res < i+1-f:
            res=i+1-f
        return res
```
