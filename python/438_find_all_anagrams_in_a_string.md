# find all anagrams in a string

[[slidingwindow]]

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

## Example 1

```text
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

## Example 2

```text
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

简单而且直白的算法实现滑动窗口。

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windows, need = defaultdict(int), Counter(p)
        valid = 0
        left = 0
        res = []

        for right, c in enumerate(s):
            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left + 1 == len(p):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if windows[d] == need[d]:
                        valid -= 1
                    windows[d] -= 1
        return res
```

来自labuladong的模板：

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, 0
        windows, need = defaultdict(int), Counter(p)
        valid = 0
        res = list()

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left == len(p):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if windows[d] == need[d]:
                        valid -= 1
                    windows[d] -= 1
        return res
```

枚举子串 t 的右端点，如果发现 t 其中一种字母的出现次数大于 p 的这种字母的出现次数，则右移 t 的左端点（缩小窗口）。如果发现 t 的长度等于 p 的长度，则说明 t 的每种字母的出现次数，等于 p 的每种字母的出现次数，即 t 是 p 的异位词。

证明：内层循环结束后，t 的每种字母的出现次数，都小于等于 p 的每种字母的出现次数。如果 t 的其中一种字母的出现次数比 p 的小，那么 t 的长度必然小于 p 的长度。所以只要 t 的长度等于 p 的长度，就说明 t 的每种字母的出现次数，和 p 的每种字母的出现次数都相同，t 是 p 的异位词，把 t 左端点下标加入答案。

代码实现时，可以把 cntS 和 cntP 合并成一个 cnt：

对于 p 的字母 c，把 cnt[p] 加一。
对于 t 的字母 c，把 cnt[c] 减一。
如果 cnt[c]<0，说明窗口中的字母 c 的个数比 p 的多，右移左端点。

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数
        ans = []

        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # t 和 p 的每种字母的出现次数都相同（证明见上）
                ans.append(left)  # t 左端点下标加入答案

        return ans
```
