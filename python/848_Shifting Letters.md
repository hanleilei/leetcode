# Shifting Letters

[[prefixSum]]

You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.
Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
shifts.length == s.length
0 <= shifts[i] <= 109

思路：

1. shift的位移有点奇怪，需要逆序求前缀和。
2. 将s转换为数字，求前缀和，再转换为字母。

```python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = [ord(i) - 97 for i in s]
        for i in range(len(shifts) - 1, -1, -1):
            if i != len(shifts) - 1:
                shifts[i] += shifts[i + 1]
        for i in range(len(s)):
            s[i] = (s[i] + shifts[i]) % 26
        return ''.join([chr(i + 97) for i in s])
```

简化：

```python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts = list(accumulate(shifts[::-1]))[::-1]
        return ''.join(chr((ord(c) - 97 + shift) % 26 + 97) for c, shift in zip(s, shifts))
```

逆序的前缀和，原来这么简单。
