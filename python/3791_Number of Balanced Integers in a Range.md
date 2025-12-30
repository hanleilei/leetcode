# Number of Balanced Integers in a Range

[[dp]]

You are given two integers low and high.

An integer is called balanced if it satisfies both of the following conditions:

It contains at least two digits.
The sum of digits at even positions is equal to the sum of digits at odd positions (the leftmost digit has position 1).
Return an integer representing the number of balanced integers in the range [low, high] (both inclusive).

 

Example 1:

Input: low = 1, high = 100

Output: 9

Explanation:

The 9 balanced numbers between 1 and 100 are 11, 22, 33, 44, 55, 66, 77, 88, and 99.

Example 2:

Input: low = 120, high = 129

Output: 1

Explanation:

Only 121 is balanced because the sum of digits at even and odd positions are both 2.

Example 3:

Input: low = 1234, high = 1234

Output: 0

Explanation:

1234 is not balanced because the sum of digits at odd positions (1 + 3 = 4) does not equal the sum at even positions (2 + 4 = 6).

 

Constraints:

1 <= low <= high <= 10^15

数位DP

```python
class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def count(n):
            if n < 10: return 0
            s = str(n)
            
            @lru_cache(None)
            def dp(i, tight, diff, started):
                if i == len(s):
                    return started and diff == 0
                
                res = 0
                for d in range((int(s[i]) if tight else 9) + 1):
                    if not started and d == 0:
                        res += dp(i + 1, tight and d == int(s[i]), 0, False)
                    else:
                        new_diff = diff + (d if (i + 1) % 2 else -d)
                        res += dp(i + 1, tight and d == int(s[i]), new_diff, True)
                return res
            
            return dp(0, True, 0, False)
        
        return count(high) - count(low - 1)
```

TODO：Digital DP问题，需要看下面的视频理解掌握

见[视频](https://www.bilibili.com/video/BV1Fg4y1Q7wv/?t=31m28s)讲解,其中有更详细的解释。还有[视频](https://www.bilibili.com/video/BV1rS4y1s721/?t=19m36s&vd_source=87d6dd47dbb44dd80e0f5eb84dd30767)讲解数位DP的基础知识。

```python
class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        # 最小的满足要求的数是 11
        if high < 11:
            return 0

        low = max(low, 11)
        low_s = list(map(int, str(low)))  # 避免在 dfs 中频繁调用 int()
        high_s = list(map(int, str(high)))
        n = len(high_s)
        diff_lh = n - len(low_s)

        @cache
        def dfs(i: int, diff: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if diff == 0 else 0

            lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
            hi = high_s[i] if limit_high else 9

            res = 0
            start = lo

            # 通过 limit_low 和 i 可以判断能否不填数字，无需 is_num 参数
            if limit_low and i < diff_lh:
                # 不填数字，上界不受约束
                res = dfs(i + 1, diff, True, False)
                start = 1  # 下面填数字，至少从 1 开始填

            for d in range(start, hi + 1):
                res += dfs(i + 1,
                           diff + (d if i % 2 else -d),
                           limit_low and d == lo,
                           limit_high and d == hi)

            return res

        return dfs(0, 0, True, True)

```

```python
class Solution:
    def solve(self, num: int) -> int:
        digits = [0, *map(int, str(num))]

        @cache
        def dp(i: int = 0, diff: int = 0, digitlim: bool = True) -> int:
            # We reached end of number
            if i == len(digits):
                return int(diff == 0)

            # Calculate current digit values
            maxdigit = digits[i] if digitlim else 9
            possign = (2 * int(i % 2) - 1)

            result = 0
            for digit in range(maxdigit + 1):
                # Update state and call dp for the next digit
                diff_next = diff + digit * possign
                digitlim_next = digit == maxdigit and digitlim
                result += dp(i + 1, diff_next, digitlim_next)

            return result

        return dp()

    def countBalanced(self, low: int, high: int) -> int:
        return self.solve(high) - self.solve(low - 1)
```
