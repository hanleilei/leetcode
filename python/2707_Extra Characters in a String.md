# Extra Characters in a String

[[dp]] [[trie]]

You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

## Example 1

```text
Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.
```

## Example 2

```text
Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
```

## Constraints

```text
1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words
```

一、寻找子问题

为了方便转成递推，从后往前考虑。

设 nnn 为 sss 的长度。我们可以：

直接跳过 sss 的最后一个字符，那么问题变成 s 的前 n−1 个字符的子问题。
考虑「枚举选哪个」，如果从 s[j] 开始的后缀在 dictionary 中，那么问题变成 s 的前 j−1 个字符的子问题。

二、记忆化搜索

根据上面的讨论，定义 dfs(i) 表示 sss 的前 i 个字符的子问题。

跳过 sss 的最后一个字符，有 dfs(i)=dfs(i−1)+1。
考虑「枚举选哪个」，如果从 s[j] 到 s[i] 的子串在 dictionary 中，有

```dfs(i)=```

这两种情况取最小值。

递归边界：dfs(−1)=0。

答案：dfs(n−1)。


```python
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        vis, length = set(dictionary), set(len(x) for x in dictionary)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for ln in length:
                if i - ln + 1 >= 0 and s[i - ln : i] in vis:
                    dp[i] = min(dp[i], dp[i - ln])

        return dp[n] 
```
