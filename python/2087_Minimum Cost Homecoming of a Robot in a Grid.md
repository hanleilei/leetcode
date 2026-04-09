# Minimum Cost Homecoming of a Robot in a Grid

There is an m x n grid, where (0, 0) is the top-left cell and (m - 1, n - 1) is the bottom-right cell. You are given an integer array startPos where startPos = [startrow, startcol] indicates that initially, a robot is at the cell (startrow, startcol). You are also given an integer array homePos where homePos = [homerow, homecol] indicates that its home is at the cell (homerow, homecol).

The robot needs to go to its home. It can move one cell in four directions: left, right, up, or down, and it can not move outside the boundary. Every move incurs some cost. You are further given two 0-indexed integer arrays: rowCosts of length m and colCosts of length n.

    If the robot moves up or down into a cell whose row is r, then this move costs rowCosts[r].
    If the robot moves left or right into a cell whose column is c, then this move costs colCosts[c].

Return the minimum total cost for this robot to return home.

Example 1:

![](https://assets.leetcode.com/uploads/2021/10/11/eg-1.png)

Input: startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]
Output: 18
Explanation: One optimal path is that:
Starting from (1, 0)
-> It goes down to (2, 0). This move costs rowCosts[2] = 3.
-> It goes right to (2, 1). This move costs colCosts[1] = 2.
-> It goes right to (2, 2). This move costs colCosts[2] = 6.
-> It goes right to (2, 3). This move costs colCosts[3] = 7.
The total cost is 3 + 2 + 6 + 7 = 18

Example 2:

Input: startPos = [0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26]
Output: 0
Explanation: The robot is already at its home. Since no moves occur, the total cost is 0.

Constraints:

    m == rowCosts.length
    n == colCosts.length
    1 <= m, n <= 10^5
    0 <= rowCosts[r], colCosts[c] <= 10^4
    startPos.length == 2
    homePos.length == 2
    0 <= startrow, homerow < m
    0 <= startcol, homecol < n

脑筋急转弯：由于题目保证代价均为非负数，所以除了径直走以外，其它弯弯绕绕的策略都不可能更优，那么直接统计径直走的代价即可。

设起点为 (x0​,y0​)，终点为 (x1​,y1​)。

分别计算上下移动的代价，左右移动的代价，二者之和就是总代价。

    上下移动的代价：如果 x0​<x1​，那么从起点移动到终点，x0​+1,x0​+2,…,x1​ 这些行都要访问到，移动代价为 rowCosts 的子数组 [x0​+1,x1​] 的元素和。如果 x0​>x1​，那么移动代价为 rowCosts 的子数组 [x1​,x0​−1] 的元素和。
    左右移动的代价：如果 y0​<y1​，那么从起点移动到终点，y0​+1,y0​+2,…,y1​ 这些列都要访问到，移动代价为 colCosts 的子数组 [y0​+1,y1​] 的元素和。如果 y0​>y1​，那么移动代价为 colCosts 的子数组 [y1​,y0​−1] 的元素和。

代码实现时，不需要根据 x0​ 和 x1​ 的大小关系分情况讨论，而是计算 rowCosts 的子数组 [min(x0​,x1​),max(x0​,x1​)] 的元素和，再减去多算的起点代价 rowCosts[x0​]。对于 y0​ 和 y1​ 同理。

```python
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        x0, y0 = startPos
        x1, y1 = homePos

        # 起点的代价不计入，先减去
        ans = -rowCosts[x0] - colCosts[y0]

        # 累加代价（包含起点）
        ans += sum(rowCosts[min(x0, x1): max(x0, x1) + 1])
        ans += sum(colCosts[min(y0, y1): max(y0, y1) + 1])

        return ans
```
