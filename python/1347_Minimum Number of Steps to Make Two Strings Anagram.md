# Minimum Number of Steps to Make Two Strings Anagram

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

## Example 1

```text
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
```

## Example 2

```text
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
```

## Example 3

```text
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
```

## Constraints

```text
1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.
```

理解一下python中字典的这类操作就很简单：

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a = Counter(s) - Counter(t)
        return sum(a.values())
```

再来一个正常人方法的，思路差不多：

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        memo = defaultdict(int)
        for char in s:
            memo[char] += 1
        count = 0

        for c in t:
            if memo[c]:
                memo[c] -= 1
            else:
                count+= 1
        return sum(memo.values())
```
