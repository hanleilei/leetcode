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

        for i in xrange(k):               # Time:  O(k)
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

        for i in xrange(k):               # Time:  O(k)
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
