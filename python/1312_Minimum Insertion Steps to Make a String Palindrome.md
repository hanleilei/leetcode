# Minimum Insertion Steps to Make a String Palindrome

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

## Example 1

```text
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
```

## Example 2

```text
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
```

## Example 3

```text
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
```

## Constraints

- 1 <= s.length <= 500
- s consists of lowercase English letters.

先来一个lee215的方法：

## Intuition

Split the string s into to two parts,
and we try to make them symmetrical by adding letters.

The more common symmetrical subsequence they have,
the less letters we need to add.

Now we change the problem to find the length of longest common sequence.
This is a typical dynamic problem.

## Explanation

1. Step1.
Initialize `dp[n+1][n+1]`
where`dp[i][j]` means the length of longest common sequence between
i first letters in s1 and j first letters in s2.

2. Step2.
Find the the longest common sequence between s1 and s2,
where s1 = s and s2 = reversed(s)

3. Step3.
`return n - dp[n][n]`

## Complexity

Time O(N^2)
Space O(N^2)

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        def isPalindrome(s):
            return s == s[::-1]
        
        if isPalindrome(s):
            return 0
        
        n = len(s)
        dp = [[0] * (n + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j] + 1 if s[i] == s[~j] else max(dp[i][j + 1], dp[i + 1][j])
        return n - dp[n][n]
```

