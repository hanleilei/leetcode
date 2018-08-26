# word break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:
```
Input:

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
```
Example 2:
```
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
```
Example 3:
```
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
```

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.S = s
        self.D = wordDict
        self.cache = {}
        return [' '.join(x) for x in self.by(len(s))]

    def by(self, n):
        if n == 0:
            return []
        if n in self.cache:
            return self.cache[n]
        r = []
        for w in self.D:
            l = len(w)
            if l <= n:
                if self.S[n - l:n] == w:
                    if l < n:
                        for pre in self.by(n - l):
                            r.append(pre + [w])
                    else:
                        r.append([w])
        self.cache[n] = r
        return r
```

DFS版本：
```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not wordDict:
            return []

        d={}
        ws=set(wordDict)

        mx_len=max(map(len, ws))

        def dfs(start):
            if start==len(s):
                return [[]]

            if start in d:
                return d[start]

            end=start+1
            out=[]
            while end <= len(s) and end-start <= mx_len:
                if s[start:end] in ws:
                    box=dfs(end)
                    if box is not None:
                        for b in box:
                            out.append(b+[s[start:end]])

                end+=1

            if not out:
                out=None
            d[start]=out
            return out

        out=dfs(0)
        if not out:
            return []
        return [' '.join(w for w in b[::-1]) for b in out]

```

再来一个呆萌的DFS+DP的版本，效率感人：

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        Solution.res = []
        self.dfs(s, wordDict, '')
        return Solution.res

    def check(self, s, wordDict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(0, i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]

    def dfs(self, s, wordDict, stringlist):
        if self.check(s, wordDict):
            if len(s) == 0: Solution.res.append(stringlist[1:])
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, stringlist+' '+s[:i])
```

超级骚的单行版本：

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        search = lambda i, wordDict, cache={len(s): [[]]}: cache[i] if i in cache else [[s[i: j]] + r for j in xrange(i + 1, len(s) + 1) if s[i: j] in wordDict for r in cache.setdefault(j, search(j, wordDict))]
        return map(lambda x: ' '.join(x), search(0, set(wordDict)))
```
