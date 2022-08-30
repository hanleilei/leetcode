## Count Numbers with Unique Digits

Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

Example 1:

```
Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
```

Example 2:

```
Input: n = 0
Output: 1
```

Constraints:

```
0 <= n <= 8
```

下面是网上投票最多的是解释：

This is a digit combination problem. Can be solved in at most 10 loops.

When n == 0, return 1. I got this answer from the test case.

When n == 1, \_ can put 10 digit in the only position. [0, ... , 10]. Answer is 10.

When n == 2, \_ \_ first digit has 9 choices [1, ..., 9], second one has 9 choices excluding the already chosen one. So totally 9 \* 9 = 81. answer should be 10 + 81 = 91

When n == 3, \_ \_ \_ total choice is 9 _ 9 _ 8 = 684. answer is 10 + 81 + 648 = 739

When n == 4, \_ \_ \_ \_ total choice is 9 _ 9 _ 8 \* 7.

...

When n == 10, \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ total choice is 9 _ 9 _ 8 _ 7 _ 6 _ 5 _ 4 _ 3 _ 2 \* 1

When n == 11, \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ \_ total choice is 9 _ 9 _ 8 _ 7 _ 6 _ 5 _ 4 _ 3 _ 2 _ 1 _ 0 = 0

```python
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        ans = 10
        base = 9

        for i in range(2, n+1):
            base = base * (9 - i + 2)
            ans += base
        return ans
```
