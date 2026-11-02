# Maximize Sum of Squares of Digits

You are given two positive integers num and sum.

A positive integer n is good if it satisfies both of the following:

    The number of digits in n is exactly num.
    The sum of digits in n is exactly sum.

The score of a good integer n is the sum of the squares of digits in n.

Return a string denoting the good integer n that achieves the maximum score. If there are multiple possible integers, return the maximum ​​​​​​​one. If no such integer exists, return an empty string.

Example 1:

Input: num = 2, sum = 3

Output: "30"

Explanation:

There are 3 good integers: 12, 21, and 30.

    The score of 12 is 12 + 22 = 5.
    The score of 21 is 22 + 12 = 5.
    The score of 30 is 32 + 02 = 9.

The maximum score is 9, which is achieved by the good integer 30. Therefore, the answer is "30".

Example 2:

Input: num = 2, sum = 17

Output: "98"

Explanation:

There are 2 good integers: 89 and 98.

    The score of 89 is 82 + 92 = 145.
    The score of 98 is 92 + 82 = 145.

The maximum score is 145. The maximum good integer that achieves this score is 98. Therefore, the answer is "98".

Example 3:

Input: num = 1, sum = 10

Output: ""

Explanation:

There are no integers that have exactly 1 digit and whose digits sum to 10. Therefore, the answer is "".

Constraints:

    1 <= num <= 2 * 10^5
    1 <= sum <= 2 * 10^6

把 num 简记为 n。

首先判断无解的情况。如果所有位置都填 9，数位和 9n 仍然小于 sum，那么无解，返回空串。

否则有解。把 9 拆分成 9+0 还是 5+4？由于 $9^2>5^2+4^2$，拆分成 9+0 更好。一般地，由于 $f(x)=x^2$ 是凸函数，当元素分布最不均匀时，平方和最大。

为了最大化答案的字典序，我们可以：

    先填 ⌊sum/9⌋ 个 9。
    如果 sum mod9 > 0，那么再填一个 sum mod 9。
    最后填入 n−∣ans∣ 个 0，其中 ∣ans∣ 表示当前答案的长度。

```python
class Solution:
    def maxSumOfSquares(self, n: int, s: int) -> str:
        if n * 9 < s:
            return ''
        res = '9' * (s // 9)
        if s % 9:
            res += digits[s % 9]
        return res + '0' * (n - len(res))
```
