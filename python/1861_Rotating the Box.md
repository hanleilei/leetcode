# Rotating the Box

You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

Example 1:

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png)

Input: boxGrid = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
Example 2:

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png)

Input: boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png)

Input: boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

Constraints:

m == boxGrid.length
n == boxGrid[i].length
1 <= m, n <= 500
boxGrid[i][j] is either '#', '*', or '.'.

boxGrid 的每一行互相独立，可以分别计算。

单独看每一行，我们需要知道每个障碍物（*）的左边有多少个石头（#）。

具体地，设当前障碍物到上一个障碍物之间有 cnt 个石头。那么旋转后，当前障碍物的左边有连续 cnt 个石头。据此：

- 在遍历过程中，统计石头的个数 cnt。
- 如果下一个格子是障碍物，或者当前格子是最后一个格子，那么从当前格子往前填入连续 cnt 个石头，并重置计数器 cnt=0。

细节：第 i 行的格子旋转后在倒数第 i 列，第 j 列的格子旋转后在第 j 行。所以 (i,j) 旋转后位于 (j,m−1−i)。

```python
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        res = [["."] * m for _ in range(n)]

        for i, row in enumerate(boxGrid):
            cnt = 0
            for j, ch in enumerate(row):
                if ch == "#":
                    cnt += 1
                    ch = "."
                res[j][-1 - i] = ch
                if j == n - 1 or row[j + 1] == "*":
                    for k in range(j, j - cnt, -1):
                        res[k][-1 - i] = '#'
                    cnt = 0
        return res
```

对于每一行 row，倒着遍历，我们可以直接确定每个石头落入的位置：

- 如果 row[j] 是障碍物，那么它左边最近的石头，在旋转后掉落到 row[j−1]。我们用一个变量 k 维护石头掉落后的位置，如果 row[j] 是障碍物，那么更新 k=j−1。注：如果 row[j] 左边最近的不是石头而是障碍物，那么 k 会继续更新，无需担心石头落到错误的位置。
- 如果 row[j] 是石头，那么它掉落到 row[k]。然后把 k 减一，表示左边下一块石头掉落后的位置。

```python
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        res = [["."] * m for _ in range(n)]

        for i, row in enumerate(boxGrid):
            k = n - 1
            for j in range(n -1, -1, -1):
                if row[j] == "*":
                    res[j][-1 - i] = "*"
                    k = j - 1
                elif row[j] == "#":
                    res[k][-1 - i] = "#"
                    k -= 1
        return res
```
