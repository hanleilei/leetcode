# Minimum Additions to Make Valid String

Given a string word to which you can insert letters "a", "b" or "c" anywhere and any number of times, return the minimum number of letters that must be inserted so that word becomes valid.

A string is called valid if it can be formed by concatenating the string "abc" several times.

## Example 1

```text
Input: word = "b"
Output: 2
Explanation: Insert the letter "a" right before "b", and the letter "c" right next to "a" to obtain the valid string "abc".
```

##Example 2

```text
Input: word = "aaa"
Output: 6
Explanation: Insert letters "b" and "c" next to each "a" to obtain the valid string "abcabcabc".
```

## Example 3

```text
Input: word = "abc"
Output: 0
Explanation: word is already valid. No modifications are needed. 
```

## Constraints

```text
1 <= word.length <= 50
word consists of letters "a", "b" and "c" only. 
```

脑筋急转弯。。

方法一：考虑相邻字母

下文将 word 简记为 s

对于两个相邻字符 x 和 y 在 y 左侧），使 s 有效的话需要插入 y−x−1 个字母。

考虑到这可能是个负数，可以通过如下技巧转换在 [0,2] 内：

(y−x−1+3) mod 3
例如 x=‘a’,y=‘c’, 则有 (‘c’−‘a’+2) mod 3=1, 意思是需要补一个字母 ‘b’。
例如 x=‘c’,y=‘a’，则有 (‘a’−‘c’+2) mod 3=0，无需补字母。
最后补齐开头的 s[0]−‘a’，和结尾的 ‘c’−s[n−1]。这俩可以合并为 s[0]−s[n−1]+2。

```python
class Solution:
    def addMinimum(self, s: str) -> int:
        ans = ord(s[0]) - ord(s[-1]) + 2
        for x, y in pairwise(map(ord, s)):
            ans += (y - x + 2) % 3
        return ans

```

方法二：考虑 abc 的个数

假设答案由 t 个 ‘abc’ 组成，那么需要插入的字符个数为 3t−n。

对于两个相邻字符 x 和 y 在 t\y 左侧）：

如果 x < y，那么 x 和 y 可以在同一个 ‘abc’ 内，否则一定不在。
如果 x ≥ y，那么 x 和 y 一定不在同一个 ‘abc 内。
例如 s = ‘caa’ 中的 s[0]≥s[1], s[1]≥s[2]，所以需要 t=3 个 ‘abc’，即 ‘abcabcabc’。

所以 t 就是 x≥y 的次数加一。

```python
class Solution:
    def addMinimum(self, word: str) -> int:
        n = 1 + sum(x >= y for x, y in pairwise(word))
        return 3 * n - len(word)
```

```python
class Solution:
    def addMinimum(self, word: str) -> int:
        dp = 2
        n = len(word)
        for i in range(1, n):
            if word[i - 1] < word[i]:
                dp -= 1
            else:
                dp += 2
        return dp
```
