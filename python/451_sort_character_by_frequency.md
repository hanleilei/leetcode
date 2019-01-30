# sort character by frequency

Given a string, sort it in decreasing order based on the frequency of characters.

## Example 1:
```
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```
Example 2:
```
Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
```
Example 3:
```
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
```
Note that 'A' and 'a' are treated as two different characters.

来一个第一直觉的，用字典：

```Python
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        import operator
        from collections import Counter
        d = dict(Counter(s))
        res = ''
        for k, v in sorted(d.items(),key = operator.itemgetter(1), reverse=True):
            res += k*v
        return res

```

再来一个速度快的，28ms，超过99%的人：

```python
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = [(v, s.count(v)) for v in set(s)]

        table.sort(key = lambda x: x[1], reverse = True)

        return ''.join(map(lambda x: x[0] * x[1], table))
```
