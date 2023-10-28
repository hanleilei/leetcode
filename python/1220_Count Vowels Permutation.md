# Count Vowels Permutation

Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

## Example 1

```text
Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
```

## Example 2

```text
Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
```

## Example 3

```text
Input: n = 5
Output: 68
```

Constraints:

1 <= n <= 2 * 10^4

![](https://assets.leetcode.com/users/elliotp/image_1570334689.png)

可以看到从上到下，每个字母能跟着几个字母；换个思路，比方说，a的个数在下一层，取决于上一层的eiu的个数，这下问题就很好理解了。

```python
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1,1,1,1,1
        for _ in range(n - 1):
            a, e, i, o, u = e+i+u, a + i, e+o, i, i+o
        return (a + e+ i+ o+u) % (10 **9 + 7)
```
