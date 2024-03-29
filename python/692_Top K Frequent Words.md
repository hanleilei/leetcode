# Top K Frequent Words

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

调试起来好烦，各种 corn case 不过..

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        # freq = heapq.nlargest(k, c.values())
        d = collections.defaultdict(list)
        res = list()

        for x, v in c.items():
            d[v].append(x)
        freq = heapq.nlargest(k, d.keys())


        for i in freq:
            if k > int(i) and k > len(d[i]):
                res.extend(sorted(d[i]))
            elif k > 0:
                res.extend(sorted(d[i])[:k])
            k -= len(d[i])

        return res
```

看看人家的算法：

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        res = sorted(c, key=lambda x: (-c[x], x))
        return res[:k]
```
