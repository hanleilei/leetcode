# Unique Paths III

[[DFS]] [[backtracking]]

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:

![](https://assets.leetcode.com/uploads/2021/08/02/lc-unique1.jpg)

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:

1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

![](https://assets.leetcode.com/uploads/2021/08/02/lc-unique2.jpg)

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:

1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

![](https://assets.leetcode.com/uploads/2021/08/02/lc-unique3-.jpg)

Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2

There is exactly one starting cell and one ending cell.

方法一：回溯

前置知识：回溯

请看【基础算法精讲 14】。

算法

定义 dfs(x,y,left) 表示从 (x,y) 出发，还剩下 left 个无障碍方格（不含终点）需要访问时的不同路径个数：

- 如果出界，或者 grid[x][y]=−1，则返回 0，表示不合法的路径。
- 如果 grid[x][y]=2，说明到达终点。如果此时 left=0 则返回 1 表示找到了一条合法路径；否则返回 0 表示不合法的路径。
- 否则向上下左右移动，累加四个方向递归的返回值。
- 代码实现时，可以把 grid[x][y] 改成 −1，表示这个格子访问过，在返回前改回 0（恢复现场）。
设起点为 (sx,sy)，grid 中有 $cnt_0$ 个 0，那么递归入口为 $dfs(sx,sy,cnt_0 +1)$，这里 +1 是把起点这个格子也算上。

注意不存在中途经过终点的情况，因为题目要求「一条路径中不能重复通过同一个方格」，终点也必须只访问一次。（如果感觉题意不清楚可以看英文描述。）

```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int, left: int) -> int:
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] < 0:
                return 0  # 不合法
            if grid[x][y] == 2:  # 到达终点
                return left == 0  # 必须访问所有的无障碍方格
            grid[x][y] = -1  # 标记成访问过，因为题目要求「不能重复通过同一个方格」
            ans = dfs(x - 1, y, left - 1) + dfs(x, y - 1, left - 1) + \
                  dfs(x + 1, y, left - 1) + dfs(x, y + 1, left - 1)
            grid[x][y] = 0  # 恢复现场
            return ans

        cnt0 = sum(row.count(0) for row in grid)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:  # 起点
                    return dfs(i, j, cnt0 + 1)  # +1 把起点也算上
```

复杂度分析

- 时间复杂度：$O(3^{mn})$，其中 m 和 n 分别为 grid 的行数和列数。搜索树的高度为 $O(mn)$，除了根节点以外，其余节点至多有 3 个儿子（因为不能往回走），所以这棵搜索树至多有 $O(3^{mn})$ 个节点。由于不能重复访问同一个格子，实际节点个数远小于这里估计的上界。
- 空间复杂度：$O(mn)$。递归需要 O(mn) 的栈空间。

方法二：状态压缩+记忆化搜索

前置知识

从集合论到位运算，常见位运算技巧分类总结！
动态规划入门：从记忆化搜索到递推【基础算法精讲 17】
算法

整体思路和方法一类似，区别主要在位运算上（请先看前置知识中的位运算文章）。

- 用二进制数 vis 表示访问过的格子的坐标集合，替换方法一中的递归参数 left。我们在递归中去修改 vis，不去修改 grid[x][y]，做到无后效性，从而可以使用记忆化搜索。
- 为了方便用位运算实现，可以把二维坐标 (x,y) 映射为整数 nx+y。如果访问了 (x,y)，就把 vis 从低到高第 nx+y 个比特位标记成 1。
- 为了方便判断，可以在递归前把障碍方格也加到 vis 中，这样递归到终点时，只需要判断 vis 是否为全集 all，即所有格子的坐标集合。

另外，由于有大量状态是无法访问到的，相比数组，用哈希表记忆化更好。

注：实际上，并没有太多重复递归调用，使用哈希表反而拖慢了速度，方法一可能更快。

```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ALL = (1 << m * n) - 1  # 全集（所有格子的坐标集合）

        @cache
        def dfs(x: int, y: int, vis: int) -> int:
            if x < 0 or x >= m or y < 0 or y >= n or vis >> (x * n + y) & 1:
                return 0  # 不合法
            vis |= 1 << (x * n + y)  # 标记访问过 (x,y)，因为题目要求「不能重复通过同一个方格」
            if grid[x][y] == 2:  # 到达终点
                return vis == ALL  # 必须访问所有的无障碍方格
            return dfs(x - 1, y, vis) + dfs(x, y - 1, vis) + \
                   dfs(x + 1, y, vis) + dfs(x, y + 1, vis)

        vis = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v < 0:  # 把障碍方格算上
                    vis |= 1 << (i * n + j)
                elif v == 1:  # 起点
                    sx, sy = i, j
        return dfs(sx, sy, vis)
```

复杂度分析

- 时间复杂度：$O(mn2^{mn})$，其中 m 和 n 分别为 grid 的行数和列数。动态规划的时间复杂度 = 状态个数 × 单个状态的计算时间。本题中状态个数等于 $O(mn2^{mn})$，单个状态的计算时间为 O(1)，因此时间复杂度为 $O(mn2^{mn})$。由于很多状态无法访问到，实际时间远小于这里估计的上界。
- 空间复杂度：$O(mn2^{mn})$。
