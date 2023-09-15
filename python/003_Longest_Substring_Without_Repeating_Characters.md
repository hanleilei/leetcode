# Longest Substring Without Repeating Characters

[[sliding window]]

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question

找出最长序列的长度，一个可行的办法是转换成 ascii 码，然后遍历字符串，

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

下面的版本超级快，超过了 100%的提交：

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
                res = max(res, i - f)
                f = m[v] + 1
            m[v] = i
        return max(res, i + 1 - f)
```

再来一个非常容易理解的实现：

```Python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d, res, start, = {}, 0, 0
        for i, v in enumerate(s):
            if v in d:
                # update the res
                res = max(res, i-start)
                # here should be careful, like "abba"
                start = max(start, d[v]+1)
            d[v] = i
        # return should consider the last
        # non-repeated substring
        return max(res, len(s)-start)
```

再来一个我自己想出来的，用集合 + 队列的方法：

```Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq_chars = set()
        res = 0
        d = collections.deque()

        for i in s:
            if i in d:
                while len(d) > 0 and d[0] != i:
                    d.popleft()
                if len(d)>0:
                    d.popleft()
                # res = max(res, len(d))
            d.append(i)
            res = max(res, len(d))
        return res
```

再来一个labuladong的方法：

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        windows = defaultdict(int)
        res = 0
        size = len(s)

        while right < len(s):
            c = s[right]
            right += 1
            windows[c] += 1
            
            while windows[c] > 1:
                d = s[left]
                left += 1
                windows[d]-= 1
            res = max(res, right - left)
        return res
```
这里可以算是模板的简化版本。

## 总结

这道求最长无重复子串的题和之前那道 Isomorphic Strings 很类似，属于 LeetCode 的早期经典题目，博主认为是可以跟 Two Sum 媲美的一道题。给了我们一个字符串，让我们求最长的无重复字符的子串，注意这里是子串，不是子序列，所以必须是连续的。我们先不考虑代码怎么实现，如果给一个例子中的例子"abcabcbb"，让你手动找无重复字符的子串，该怎么找。博主会一个字符一个字符的遍历，比如 a，b，c，然后又出现了一个 a，那么此时就应该去掉第一次出现的 a，然后继续往后，又出现了一个 b，则应该去掉一次出现的 b，以此类推，最终发现最长的长度为 3。所以说，我们需要记录之前出现过的字符，记录的方式有很多，最常见的是统计字符出现的个数，但是这道题字符出现的位置很重要，所以我们可以使用 HashMap 来建立字符和其出现位置之间的映射。进一步考虑，由于字符会重复出现，到底是保存所有出现的位置呢，还是只记录一个位置？我们之前手动推导的方法实际上是维护了一个滑动窗口，窗口内的都是没有重复的字符，我们需要尽可能的扩大窗口的大小。由于窗口在不停向右滑动，所以我们只关心每个字符最后出现的位置，并建立映射。窗口的右边界就是当前遍历到的字符的位置，为了求出窗口的大小，我们需要一个变量 left 来指向滑动窗口的左边界，这样，如果当前遍历到的字符从未出现过，那么直接扩大右边界，如果之前出现过，那么就分两种情况，在或不在滑动窗口内，如果不在滑动窗口内，那么就没事，当前字符可以加进来，如果在的话，就需要先在滑动窗口内去掉这个已经出现过的字符了，去掉的方法并不需要将左边界 left 一位一位向右遍历查找，由于我们的 HashMap 已经保存了该重复字符最后出现的位置，所以直接移动 left 指针就可以了。我们维护一个结果 res，每次用出现过的窗口大小来更新结果 res，就可以得到最终结果啦。

这里我们可以建立一个 HashMap，建立每个字符和其最后出现位置之间的映射，然后我们需要定义两个变量 res 和 left，其中 res 用来记录最长无重复子串的长度，left 指向该无重复子串左边的起始位置的前一个，由于是前一个，所以初始化就是-1，然后我们遍历整个字符串，对于每一个遍历到的字符，如果该字符已经在 HashMap 中存在了，并且如果其映射值大于 left 的话，那么更新 left 为当前映射值。然后映射值更新为当前坐标 i，这样保证了 left 始终为当前边界的前一个位置，然后计算窗口长度的时候，直接用 i-left 即可，用来更新结果 res。

这里解释下程序中那个 if 条件语句中的两个条件 m.count(s[i]) && m[s[i]] > left，因为一旦当前字符 s[i]在 HashMap 已经存在映射，说明当前的字符已经出现过了，而若 m[s[i]] > left 成立，说明之前出现过的字符在我们的窗口内，那么如果要加上当前这个重复的字符，就要移除之前的那个，所以我们让 left 赋值为 m[s[i]]，由于 left 是窗口左边界的前一个位置（这也是 left 初始化为-1 的原因，因为窗口左边界是从 0 开始遍历的），所以相当于已经移除出滑动窗口了。举一个最简单的例子"aa"，当 i=0 时，我们建立了 a->0 的映射，并且此时结果 res 更新为 1，那么当 i=1 的时候，我们发现 a 在 HashMap 中，并且映射值 0 大于 left 的-1，所以此时 left 更新为 0，映射对更新为 a->1，那么此时 i-left 还为 1，不用更新结果 res，那么最终结果 res 还为 1re
