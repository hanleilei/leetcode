# Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

## Example 1

```text
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
```

## Example 2

```text
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
```

## Example 3

```text
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
```

## Constraints

```text
1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
```

```python
class Solution:
    def closeStrings(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            ss = dict(Counter(s))
            tt = dict(Counter(t))
            return ss.keys() == tt.keys() and sorted(ss.values()) == sorted(tt.values())
        return False
```

再来一个速度快的：

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) == len(word2):
            count = defaultdict(int)
            for i in set(word1):
                count[word1.count(i)] += 1
                count[word2.count(i)] -= 1
            return not any(count.values())
        return False
```

再来一个速度最快的：

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1 = len(word1)
        l2 = len(word2)
        if l1 != l2: return False
        w1 = set(word1)
        if w1 != set(word2): return False
        wd1 = []
        wd2 = []
        for i in w1:
            wd1.append(word1.count(i))
            wd2.append(word2.count(i))
            
        if sorted(wd1) != sorted(wd2): return False
        

        return True
```
