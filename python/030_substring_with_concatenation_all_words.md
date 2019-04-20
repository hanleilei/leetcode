# Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

```
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
```

Example 2:

```
Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
```

```python
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result, m, n, k = [], len(s), len(words), 0
        if m < n*k:
            return result
        if len(words) > 0:
            k = len(words[0])

        lookup = collections.defaultdict(int)
        for i in words:
            lookup[i] += 1                # Space: O(n * k)

        for i in range(k):               # Time:  O(k)
            left, count = i, 0
            tmp = collections.defaultdict(int)
            for j in range(i, m-k+1, k): # Time:  O(m / k)
                s1 = s[j:j+k];            # Time:  O(k)
                if s1 in lookup:
                    tmp[s1] += 1
                    if tmp[s1] <= lookup[s1]:
                        count += 1
                    else:
                        while tmp[s1] > lookup[s1]:
                            s2 = s[left:left+k]
                            tmp[s2] -= 1
                            if tmp[s2] < lookup[s2]:
                                count -= 1
                            left += k
                    if count == n:
                        result.append(left)
                        tmp[s[left:left+k]] -= 1
                        count -= 1
                        left += k
                else:
                    tmp = collections.defaultdict(int)
                    count = 0
                    left = j+k
        return result
```

```python
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result, m, n, k = [], len(s), len(words), 0
        if m < n*k:
            return result
        if len(words) > 0:
            k = len(words[0])

        lookup = collections.defaultdict(int)
        for i in words:
            lookup[i] += 1                # Space: O(n * k)

        for i in range(k):               # Time:  O(k)
            left, count = i, 0
            tmp = collections.defaultdict(int)
            for j in range(i, m-k+1, k): # Time:  O(m / k)
                s1 = s[j:j+k];            # Time:  O(k)
                if s1 in lookup:
                    tmp[s1] += 1
                    if tmp[s1] <= lookup[s1]:
                        count += 1
                    else:
                        while tmp[s1] > lookup[s1]:
                            s2 = s[left:left+k]
                            tmp[s2] -= 1
                            if tmp[s2] < lookup[s2]:
                                count -= 1
                            left += k
                    if count == n:
                        result.append(left)
                        tmp[s[left:left+k]] -= 1
                        count -= 1
                        left += k
                else:
                    tmp = collections.defaultdict(int)
                    count = 0
                    left = j+k
        return result
```

和上面的方法类似：

```Python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if words == []:
            return []
        counts = dict(collections.Counter(words))
        res = set([])

        n, num, word_len = len(s), len(words), len(words[0])
        for i in range(n - num * word_len + 1):
            seen = dict()
            j = 0
            while j < num:
                word = s[i + j * word_len:i + (j + 1) * word_len]
                if word in counts:
                    seen[word] = seen.get(word, 0) + 1
                    if seen[word] > counts[word]:
                        break
                else:
                    break
                j += 1
            if j == num:
                res.add(i)

        return list(res)
```

再来一个sliding window:

```Python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        # initialize d, l, ans
        l = len(words[0])
        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1
        i = 0
        ans = []

        # sliding window(s)
        for k in range(l):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s)-l+1, l):
                tword = s[j:j+l]
                # valid word
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + l
                    subd = {}
                    count = 0

        return ans
```
