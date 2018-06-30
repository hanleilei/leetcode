# repeat dns sequence

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:
```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```

用Python的暴力解法

```python
class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        import collections
        sequences = collections.defaultdict(int) #set '0' as the default value for non-existing keys
        for i in range(len(s)):
            sequences[s[i:i+10]] += 1#add 1 to the count
        return [key for key, value in sequences.items() if value > 1] #extract the relevant keys
```

还有用集合的思路也是一样：

```Python
class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set([])
        results = set([])
        for i in range(len(s) - 9):
            curr = s[i:i+10]
            if curr in seen:
                results.add(curr)
            seen.add(curr)
        return list(results)
```
