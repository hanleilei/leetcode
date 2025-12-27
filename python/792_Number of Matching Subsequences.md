# Number of Matching Subsequences

Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.

```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = len(words)
        cnt = Counter(words)

        for w in cnt:
            i = 0
            for c in w:
                i = s.find(c,i) + 1
                if not i:
                    res -= cnt[w]
                    break
        return res
```

我们不妨将 words 中的所有单词根据首字母来分桶，即：把所有单词按照首字母分到 26 个桶中，每个桶中存储的是所有以该字母开头的所有单词。

比如对于 words = ["a", "bb", "acd", "ace"]，我们得到以下的分桶结果：

a: ["a", "acd", "ace"]
b: ["bb"]

然后我们从 s 的第一个字符开始遍历，假设当前字符为 'a'，我们从 'a' 开头的桶中取出所有单词。对于取出的每个单词，如果此时单词长度为 1，说明该单词已经匹配完毕，我们将答案加 1；否则我们将单词的首字母去掉，然后放入下一个字母开头的桶中，比如对于单词 "acd"，去掉首字母 'a' 后，我们将其放入 'c' 开头的桶中。这一轮结束后，分桶结果变为：

c: ["cd", "ce"]
b: ["bb"]

遍历完 s 后，我们就得到了答案。

```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(deque)
        for w in words:
            d[w[0]].append(w)
        ans = 0
        for c in s:
            for _ in range(len(d[c])):
                t = d[c].popleft()
                if len(t) == 1:
                    ans += 1
                else:
                    d[t[1]].append(t[1:])
        return ans
```

实际上，每个桶可以只存储单词的下标 i 以及该单词当前匹配到的位置 j，这样可以节省空间。

```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(deque)
        for i, w in enumerate(words):
            d[w[0]].append((i, 0))
        ans = 0
        for c in s:
            for _ in range(len(d[c])):
                i, j = d[c].popleft()
                j += 1
                if j == len(words[i]):
                    ans += 1
                else:
                    d[words[i][j]].append((i, j))
        return ans
```

方法二：二分查找

我们还可以先用数组或哈希表 d 存放字符串 s 每个字符的下标，即 d[c] 为 s 中所有字符 c 的下标组成的数组。

然后我们遍历 words 中的每个单词 w，我们通过二分查找的方法，判断 w 是否为 s 的子序列，是则答案加 1。判断逻辑如下：

定义指针 i 表示当前指向字符串 s 的第 i 个字符，初始化为 −1。
遍历字符串 w 中的每个字符 c，在 d[c] 中二分查找第一个大于 i 的位置 j，如果不存在，则说明 w 不是 s 的子序列，直接跳出循环；否则，将 i 更新为 d[c][j]，继续遍历下一个字符。
如果遍历完 w 中的所有字符，说明 w 是 s 的子序列。

```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def check(w):
            i = -1
            for c in w:
                j = bisect_right(d[c], i)
                if j == len(d[c]):
                    return False
                i = d[c][j]
            return True

        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        return sum(check(w) for w in words)
```
