# Number of Paths with Max Score

[[dp]]

You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

Example 1:

Input: board = ["E23","2X2","12S"]
Output: [7,1]

Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]

Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]

Constraints:

    2 <= board.length == board[i].length <= 100

前置题目：

    如果只算路径和，则本题类似 64. 最小路径和，我的题解。
    如果只算方案数，则本题类似 63. 不同路径 II，我的题解。

本题是前置题目的综合题。

    如果往左走的路径和，严格大于往上走的路径和，那么计算方案数时，只需考虑往左走的方案数。
    如果往上走的路径和，严格大于往左走的路径和，那么计算方案数时，只需考虑往上走的方案数。
    如果二者一样大，那么根据加法原理，要把两种方案数相加。

本题还可以往左上移动，要额外考虑往左上走的路径和以及方案数。

注意取模。为什么可以在中途取模？原理见 模运算的世界：当加减乘除遇上取模。

```python
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10 ** 9 + 7
        m, n = len(board), len(board[0])
        res = [[-inf] * (n + 1) for _ in range(m + 1)]  # 定义同 64 题（改成最大路径和）
        ways = [[0] * (n + 1) for _ in range(m + 1)] # 定义同 63 题
        res[0][0] = 0
        ways[0][0] = 1

        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == "X":
                    continue
                 # 左上、正上、正左
                res[i+1][j+1] = s = max(res[i][j], res[i][j+1], res[i+1][j])
                # 如果路径和相同，则累加方案数（加法原理）
                if res[i][j] == s:
                    ways[i+1][j+1] += ways[i][j]
                if res[i][j+1] == s:
                    ways[i+1][j+1] += ways[i][j+1]
                if res[i+1][j] == s:
                    ways[i+1][j+1] += ways[i+1][j]
                ways[i+1][j+1] %= mod
                if ch.isdigit():
                    res[i+1][j+1] += int(ch)
        return [res[m][n], ways[m][n]] if res[m][n] != -inf else [0, 0]

```

```python
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10 ** 9 + 7
        n = len(board)
        res = [0] + [-inf] * n # 定义同 64 题（改成最大路径和）
        ways = [1] + [0] * n # 定义同 63 题

        for row in board:
            # 计算 res[i+1][j+1] 时，pre_s 表示 res[i][j]，pre_w 表示 ways[i][j]
            pre_s, pre_w = res[0], ways[0]
            res[0], ways[0] = -inf, 0
            for j, ch in enumerate(row):
                if ch == "X":
                    pre_s, pre_w = res[j + 1], ways[j+1]
                    res[j+1], ways[j+1] = -inf, 0
                    continue
                tmp_s, tmp_w = res[j+1], ways[j+1]
                # 左上、正上、正左
                s = max(pre_s, res[j + 1], res[j])
                 # 如果路径和相同，则累加方案数（加法原理）
                w = 0
                if pre_s == s:
                    w += pre_w
                if res[j+1] == s:
                    w += ways[j+1]
                if res[j] == s:
                    w += ways[j]
                ways[j+1] = w % mod
                res[j + 1] = s
                if ch.isdigit():
                    res[j+1]+= int(ch)# 加上当前格子的值
                pre_s, pre_w = tmp_s, tmp_w
        return [res[n], ways[n]] if res[n] != -inf else [0, 0]        
```
