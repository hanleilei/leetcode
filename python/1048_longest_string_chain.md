# longest string chain

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.



Example 1:
```
Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
```

### Note:

1. 1 <= words.length <= 1000
2. 1 <= words[i].length <= 16
3. words[i] only consists of English lowercase letters.

```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # build graph
        from collections import defaultdict

        graph = defaultdict(dict)

        for word in words:
            graph[len(word)][word] = 1

        max_l = max(graph.keys())
        ans = 1
        for i in range(1, max_l + 1):
            if not len(graph[i]) or not len(graph[i - 1]):
                continue

            for word in graph[i]:
                for p_word in self.get_p_word(word, graph[i - 1]):
                    graph[i][word] = max(graph[i][word], graph[i - 1][p_word] + 1)
                    ans = max(ans, graph[i][word])
        return ans

    def get_p_word(self, word, p_set):
        ret = []
        for i in range(len(word)):
            d_w = word[:i] + word[i + 1:]
            if d_w in p_set:
                ret.append(d_w)

        return ret

```

```Python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        by_length = collections.defaultdict(set)
        for word in words:
            by_length[len(word)].add(word)

        longest = 1
        seen = {*()} # set()
        mx = len(by_length)
        mn = min(by_length)

        # in descending order
        for length in sorted(by_length, reverse=True):
            if length == mn: return 1
            if length - mn < longest:
                break
            for word in by_length[length]:
                if length - mn < longest:
                    break
                if word in seen:
                    continue
                stk = [(word, length, 1)]
                while stk:
                    word, k, n = stk.pop()
                    seen.add(word)
                    if n > longest:
                        longest = n
                    for i in range(k):
                        pre = word[:i] + word[i+1:]
                        if pre not in seen and pre in by_length[k-1]:
                            stk.append((pre, k-1, n+1))
                if longest == mx:
                    return longest

        return longest   

```

再来看下lee215的方案， 超级慢，但是很短。。
Sort the words by word's length. (also can apply bucket sort)
For each word, loop on all possible previous word with 1 letter missing.
If we have seen this previous word, update the longest chain for the current word.
Finally return the longest word chain.


Complexity
Time O(NlogN) for sorting,
Time O(NSS) for the for loop, where the second S refers to the string generation and S <= 16.
Space O(NS)

```Python
def longestStrChain(self, words):
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
        return max(dp.values())
```
