# Decoded String at Index

You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

- If the character read is a letter, that letter is written onto the tape.
- If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.

## Example 1

```text
Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
```

## Example 2

```text
Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".
```

## Example 3

```text
Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".
```

## Constraints

- 2 <= s.length <= 100
- s consists of lowercase English letters and digits 2 through 9.
- s starts with a letter.
- 1 <= k <= 109
- It is guaranteed that k is less than or equal to the length of the decoded string.

The decoded string is guaranteed to have less than 263 letters.

来一个lee215的方案

We decode the string and N keeps the length of decoded string, until N >= K.
Then we go back from the decoding position.
If it's S[i] = d is a digit, then N = N / d before repeat and K = K % N is what we want.
If it's S[i] = c is a character, we return c if K == 0 or K == N

```python
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        N = 0
        for i, c in enumerate(s):
            N = N * int(c) if c.isdigit() else N + 1
            if k <= N: break
        for j in range(i, -1, -1):
            c = s[j]
            if c.isdigit():
                N /= int(c)
                k %= N
            else:
                if k == N or k == 0: return c
                N -= 1
```

注意这样的测试用例：

```text
s = "y959q969u3hb22odq595"
k = 222280369
```
