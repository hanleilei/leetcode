# Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
```
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

先直接看一个超快的答案吧，超过100%的提交，88ms
```python
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left=-1
        right = 0
        result = ""
        totalMatch = 0
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1

        for right in range(len(s)):
            c = s[right]
            d[c] = d.get(c, 0) - 1

            # good match
            if d[c] >=0:
                totalMatch +=1

                #over match 可以不移动left
                #total match, need to advance left
                if totalMatch == len(t):
                    totalMatch -= 1

                    left +=1
                    while d[s[left]]<0:
                        d[s[left]] += 1
                        left += 1

                    # we dec the count here so that next round right need to match one more s[left],
                    d[s[left]] += 1

                    if result == "" or len(result) > right - left:
                        result = s[left: right+1]

        return result
```
再来看看stepfan大大的算法：

```python
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        The current window is s[i:j] and the result window is s[I:J]. In need[c] I store how many times I need character c (can be negative) and missing tells how many characters are still missing. In the loop, first add the new character to the window. Then, if nothing is missing, remove as much as possible from the window start and then update the result.
        """
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
```
