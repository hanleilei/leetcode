# Uncommon Words from Two Sentences

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



### Example 1:
```
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
```
### Example 2:
```
Input: A = "apple apple", B = "banana"
Output: ["banana"]
```

Note:

1. 0 <= A.length <= 200
2. 0 <= B.length <= 200
3. A and B both contain only spaces and lowercase letters.

这个是第一感觉的方法：


```python
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter
        a = dict(Counter(A.split(' ')))
        b = dict(Counter(B.split(' ')))

        res = list()

        for k, v in a.items():
            if v == 1 and k not in b:
                res.append(k)
        for k, v in b.items():
            if v == 1 and k not in a:
                res.append(k)
        return res
```

```python
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        t = A.split() +B.split()
        return [i for i in t if t.count(i) == 1]
```

再来一个：

```python
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        c = collections.Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]
```
