# Longest Palindrome by Concatenating Two Letter Words

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:

```
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
```

Example 2:

```
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
```

Example 3:

```
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
```

Constraints:

```
1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
```

对于‘aa'这样的测试用例比较麻烦，只能有一个这类的，但是如果这类组合有多个，再要得到整除法的结果。

```python
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        d = collections.Counter(words)
        cc = 0

        for w in words:
            if w[0] == w[1]:
                cc = max(cc, d[w] % 2)
                res += d[w] // 2 * 2
            else:
                res += min(d[w], d[w[::-1]]) * 2
            d.pop(w, None)
        return (res + cc) * 2
```
