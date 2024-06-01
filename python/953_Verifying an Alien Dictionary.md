# Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

直接利用了python的语言特性：可以对于两个列表进行比较和排序：

```shell
In [15]: [0,1] < [1,2]
Out[15]: True

In [16]: [1,1] < [1,2]
Out[16]: True

In [17]: [2,1] < [1,2]
Out[17]: False

In [18]: [2,1] < [1,2,3]
Out[18]: False

In [19]: [1,1] < [1,2,3]
Out[19]: True

In [20]: [1,2] < [1,2,3]
Out[20]: True

In [21]: [1,2,5] < [1,2,3]
Out[21]: False
```

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = dict(zip(order, range(26)))
        words_reform = [[d[i] for i in word] for word in words]
        return words_reform == sorted(words_reform)
```

再来一个lee215的方案：

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda w: map(order.index, w))
```
