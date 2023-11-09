# Maximum Product of Word Lengths

Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

## Example 1

```text
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
```

## Example 2

```text
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
```

## Example 3

```text
Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
```

## Constraints

```text
2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
```

直接开搞，我都觉得肯定会TLE的，结果还通过了。。。

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if len(words) == 0:
            return 0
        max_product = 0
        mapping = {word:set(word) for word in words}
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(mapping[words[i]].intersection(mapping[words[j]])) == 0:
                    max_product = max(max_product, len(words[i]) *len(words[j]))
        return max_product
```

或者：

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if len(words) == 0:
            return 0
        max_product = 0
        mapping = [(set(i), len(i)) for i in words]
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if mapping[i][0] & mapping[j][0]: continue
                max_product = max(max_product, mapping[i][1] * mapping[j][1])
        return max_product
```

bit 运算长这样：

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = [0] * 1004
        for i in range(len(words)):
            for j in range(len(words[i])):
                mask[i] |= 1 << (ord(words[i][j]) - ord('a'))
        
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not mask[i] & mask[j]:
                    ans = max(ans, len(words[i]) * len(words[j]))
        
        return ans
```

来个最快的：

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
```

通过bit operation的所要实现的：

```text
现在来解释mask |= (1 << (ord(c) - 97))这个语句的作用：

该语句的目的是为单词中的每个字符建立一个掩码（mask）。掩码是一个整数，每个字符对应掩码中的一个位。这个位是1还是0取决于字符是否在单词中出现。

这里的ord(c) - 97是获取字符c的ASCII码减去97后的结果。ASCII码中，小写字母a到z的码值分别是97到122。因此，通过减去97，我们可以得到一个0到25的数字，代表了字母表的顺序。

1 << (ord(c) - 97)是将1左移ord(c) - 97位。这会生成一个二进制数字，其中只有一个位是1，位置就在字母表的顺序位置上。例如，如果字符是'a'，ord(c) - 97为0，那么1左移0位还是1，只有第1位是1；如果字符是'b'，ord(c) - 97为1，那么1左移1位是10（二进制），第1位和第2位都是1，以此类推。

mask |= (1 << (ord(c) - 97))这个语句的作用是将单词中每个字符对应的位加入到掩码中。这样，每个单词都会有一个与之对应的掩码，其中出现的字符对应的位为1，未出现的字符对应的位为0。

通过这样的方式，我们可以快速地判断两个单词是否只有一个字符不同，因为只需要检查它们的掩码是否有且仅有一个位不同。这也是代码中not x & y的条件的作用：它检查两个掩码是否有且仅有一个位不同。
```
