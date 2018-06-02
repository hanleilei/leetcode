# Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:
```
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```


```python
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def dfs(s, cut, l, r):
            if l >= 0 and r < len(s) and s[l] == s[r]:
                if l == 0:
                    cut[r] = 0
                else:
                    cut[r] = min(cut[r], cut[l-1] + 1)
                dfs(s, cut, l-1, r+1)
        n = len(s)
        if n <= 1:
            return 0;

        cut = [i for i in range(n)]
        for i in range(n):
            dfs(s, cut, i, i)
            dfs(s, cut, i, i+1)
        return cut[n-1]
```
下面的这个算法超级牛，只用了40ms，超过了100%的提交。。

```python
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # acceleration
        if s == s[::-1]: return 0
        if any(s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1] for i in range(1, len(s))): return 1
        # algorithm
        cut = [x for x in range(-1,len(s))]  # cut numbers in worst case (no palindrome)
        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge radius if a palindrome exists
            # odd palindrome
            while r1 <= i < len(s)-r1 and s[i-r1] == s[i+r1]:
                cut[i+r1+1], r1 = min(cut[i+r1+1], cut[i-r1]+1), r1 + 1
            # even palindrome
            while r2 <= i < len(s)-r2-1 and s[i-r2] == s[i+r2+1]:
                cut[i+r2+2], r2 = min(cut[i+r2+2], cut[i-r2]+1), r2 + 1
        return cut[-1]
```
