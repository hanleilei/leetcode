# Count the Number of Special Characters I

You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

No character in word appears in uppercase.

Example 3:

Input: word = "abBCab"

Output: 1

Explanation:

The only special character in word is 'b'.

Constraints:

    1 <= word.length <= 50
    word consists of only lowercase and uppercase English letters.

一句话思路：用两个集合分别记录小写字母和大写字母（转成小写字母），两个集合的交集大小就是答案。

集合可以用二进制数表示，两个二进制数的 AND 即为交集，AND 结果中的 1 的个数即为答案。具体请看 [从集合论到位运算，常见位运算技巧分类总结](https://leetcode.cn/discuss/post/3571304/cong-ji-he-lun-dao-wei-yun-suan-chang-ji-enve/)。

附 ASCII 字符的性质：

    对于大写英文字母：二进制从右往左第 6 个比特一定是 0。
    对于小写英文字母：二进制从右往左第 6 个比特一定是 1。
    对于任何英文字母：小写字母的二进制低 5 位，等于其大写字母的二进制低 5 位。

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mask = [0] * 2
        for c in map(ord, word):
            mask[c >> 5 & 1] |= 1 << (c & 31)
        return (mask[0] & mask[1]).bit_count()
```

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        for c in word:
            if c.islower():
                lower.add(c)
            else:
                upper.add(c.lower())
        return len(lower & upper)
```

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        return sum(1 for i in range(26) if chr(97 + i) in s and chr(65 + i) in s)
```

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        words = set(word)
        res = 0
        for w in word:
            if w.lower() in words and w.upper() in words:
                res += 1
                words.remove(w.lower())
                words.remove(w.upper())
        return res
```
