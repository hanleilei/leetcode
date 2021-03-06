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

这个毫无疑问是最优解, 76ms：

```python
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 构建target的字典
        mem = collections.defaultdict(int)
        for c in t:
            mem[c] += 1
        t_len = len(t)

        minL, minR = 0, float('inf')

        l = 0

        for i, c in enumerate(s):
            # 看stefan的写法：t_len -= mem[c] > 0 也是牛。。
            if mem[c] > 0:
                t_len -= 1

            mem[c] -= 1

            # 找到了全部的t
            if t_len == 0:
                # 左边的指针向右,找到第一个在t中的字符位置
                while mem[s[l]] < 0:
                    mem[s[l]] += 1
                    l += 1
                # 获取字符串范围
                if i - l < minR - minL:
                    minR, minL = i, l

                mem[s[l]] += 1
                t_len += 1
                l += 1
        return '' if minR == float('inf') else s[minL:minR+1]
```

先直接看一个超快的答案吧，88ms
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

上面的两个算法已经非常好了，下面我们看一下以下jiuzhang的方法：

```python
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        if source is None:
            return ""

        targetHash = self.getTargetHash(target)
        targetUniqueChars = len(targetHash)
        matchedUniqueChars = 0

        hash = {}
        n = len(source)
        j = 0
        minLength = n + 1
        minWindowString = ""
        for i in range(n):
            while j < n and matchedUniqueChars < targetUniqueChars:
                if source[j] in targetHash:
                    hash[source[j]] = hash.get(source[j], 0) + 1
                    if hash[source[j]] == targetHash[source[j]]:
                        matchedUniqueChars += 1
                j += 1

            if j - i < minLength and matchedUniqueChars == targetUniqueChars:
                minLength = j - i
                minWindowString = source[i:j]

            if source[i] in targetHash:
                if hash[source[i]] == targetHash[source[i]]:
                    matchedUniqueChars -= 1
                hash[source[i]] -= 1
        return minWindowString

    def getTargetHash(self, target):
        hash = {}
        for c in target:
            hash[c] = hash.get(c, 0) + 1
        return hash
```
