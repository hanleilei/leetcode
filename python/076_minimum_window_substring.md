# Minimum Window Substring

[[sliding window]]

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

## Example

```text
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

## Note

- If there is no such window in S that covers all characters in T, return the empty string "".
- If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

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
        d = collections.Counter(t)

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

                    # we dec the count here so that next round right need to match one more s[left]

                    d[s[left]] += 1

                    if result == "" or len(result) > right - left:
                        result = s[left: right+1]

        return result
```

再来看看 stepfan 大大的算法：

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # The current window is s[i:j] and the result window is s[I:J]. In need[c] I store how many times I need character c (can be negative) and missing tells how many characters are still missing. In the loop, first add the new character to the window. Then, if nothing is missing, remove as much as possible from the window start and then update the result.

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

上面的两个算法已经非常好了，下面我们看一下以下 jiuzhang 的方法：

```python
class Solution:

    def minWindow(self, source , target):
        if source is None:
            return ""

        targetHash = collections.Counter(target)
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
```

参考labuladong的方法，实现了sliding windows。

注意我们是怎么实现对于t中有多个重复字符串的，用了valid的变量，只有满足数量时，才会进行变化。

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        windows, need = defaultdict(int), Counter(t)
        valid = 0 #用来判断t中不管有多少个重复元素，某个重复元素满足条件则加一
        start = 0
        size = float('inf')

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                windows[c] += 1
                if windows[c] == need[c]: # 判断元素数量来决定是否增加或者减少。
                    valid += 1 
            
            while valid == len(need): # 所以用valid 等于need就可以判断开始窗口缩小，这思路牛逼。
                if right - left < size:
                    start = left
                    size = right - left
                
                d = s[left]
                left += 1
                if d in need:
                    if windows[d] == need[d]:
                        valid -= 1
                    windows[d] -= 1
        return "" if size == float('inf') else s[start:start + size]
```
