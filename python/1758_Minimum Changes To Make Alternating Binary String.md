# Minimum Changes To Make Alternating Binary String

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

## Example 1

```text
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
```

## Example 2

```text
Input: s = "10"
Output: 0
Explanation: s is already alternating.
```

## Example 3

```text
Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
```

## Constraints

```text
1 <= s.length <= 104
s[i] is either '0' or '1'.
```

阅读理解，好可怕。。

```python
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        res_x, res_y = 0, 0
        x, y = 0, 0
        if n % 2 == 1:
            x = "01" * (n // 2) + "0"
            y = "10" * (n // 2) + "1"
        else:
            x = "01" * (n // 2)
            y = "10" * (n // 2)
        for i, j in zip(x, s):
            if i != j:
                res_x += 1
        for i, j in zip(y, s):
            if i != j:
                res_y += 1
        return min(res_x, res_y)
```

```python
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        c = s[::2].count("0") + s[1::2].count("1")
        return min(c, n - c)
```

```python
class Solution:
    def minOperations(self, s: str) -> int:
        change_1 = 0
        cur = True

        for c in s:
            if cur == (c == "0"):
                change_1 += 1
            
            cur = not cur
        return min(change_1, len(s) - change_1)
```
