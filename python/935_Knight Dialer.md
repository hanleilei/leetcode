# Knight Dialer

[[dp]]

The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

![](https://assets.leetcode.com/uploads/2020/08/18/chess.jpg)

We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).

![](https://assets.leetcode.com/uploads/2020/08/18/phone.jpg)

Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.

## Example 1

```text
Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
```

## Example 2

```text
Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
```

## Example 3

```text
Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.
```

## Constraints

```text
1 <= n <= 5000
```

比较惭愧，我都想到了每一个数字对应的两种结果，但是没有进一步往下走。。

思路简单清晰明了，直接模拟操作：

```python
class Solution:
    def knightDialer(self, N: int) -> int:
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        for i in range(N - 1):
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = \
                x6 + x8, x7 + x9, x4 + x8, \
                x3 + x9 + x0, 0, x1 + x7 + x0, \
                x2 + x6, x1 + x3, x2 + x4, \
                x4 + x6
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10**9 + 7)
```

bottom up DP:

```python
class Solution:
    def knightDialer(self, n: int) -> int:
        transitions = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        dp = [[0 for _ in range(10)] for _ in range(n)]
        
        # base case
        for i in range(10):
            dp[-1][i] = 1
        
        for i in range(n-2, -1, -1):
            for d in range(10):
                for reach_d in transitions[d]:
                    dp[i][d] = (dp[i][d] + dp[i+1][reach_d]) % (10**9+7)
        return sum([i  for i in dp[0]])% (10 ** 9 + 7 )
```

再把二维数组变一维：

```python
class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        current_counts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for _ in range(n-1):
            next_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for src_key in range(10):
                for dst_key in neighbors[src_key]:
                    next_counts[dst_key] = (next_counts[dst_key] + current_counts[src_key]) % (10**9 + 7)
            current_counts = next_counts
        return sum(current_counts) % (10**9 + 7)
```

This is former Google interview question. It was leaked over a year ago and was soon after blacklisted. Because of this, a former Google interviewer decided to write an excellent blog post breaking down how he asked this question and what he expected from candidates who attempt it.

This blog post explains the background of this question, common pitfalls candidates encounter, four different ways to solve it, and how a Google interviewer will evaluate your solution. This article is a gold mine for anyone considering interviewing at Google.
`https://medium.com/@alexgolec/google-interview-questions-deconstructed-the-knights-dialer-f780d516f029`

According to the article, four possible solutions are (1) naive recursive number generation, (2) naive recursive counting, (3) recursion + memoization, and (4) dynamic programming. A candidate who coded either the memoization or DP solution is likely to receive a "strong hire" recommendation.

