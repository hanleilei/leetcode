# 174. Dungeon Game

## 问题描述

The demons had captured the princess `P` and imprisoned her in the
**bottom-right corner** of a dungeon. The dungeon consists of `m x n`
rooms laid out in a 2D grid. Our valiant knight `K` was initially
positioned in the **top-left room** and must fight his way through
the dungeon to rescue the princess.

The knight has an initial health point represented by a positive
integer. If at any point his health point drops to **0 or below**,
he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health
(negative integers) upon entering these rooms; other rooms are either
empty (0's) or contain magic orbs that increase the knight's health
(positive integers).

In order to reach the princess as quickly as possible, the knight
decides to move only **rightward or downward** in each step.

Write a function to determine the knight's **minimum initial health**
so that he is able to rescue the princess.

## 示例

**Example 1:**

```text
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7

Explanation:
The initial health of the knight must be at least 7 if he follows
the optimal path: RIGHT -> RIGHT -> DOWN -> DOWN

| -2(K) | -3  |  3  |
|-------|-----|-----|
|  -5   | -10 |  1  |
|  10   |  30 | -5(P)|

路径：(-2) -> (-3) -> (3) -> (1) -> (-5)
```

**Example 2:**

```text
Input: dungeon = [[0]]
Output: 1
```

## 约束条件

- m == dungeon.length
- n == dungeon[i].length
- 1 <= m, n <= 200
- -1000 <= dungeon\[i\]\[j\] <= 1000

## 解法

### 方法1：动态规划（从右下到左上）推荐

核心思想：从终点倒推，计算每个位置需要的最小初始血量。

关键洞察：必须从右下角反向推导，因为我们需要保证每一步
血量都 >= 1。

```python
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        逆向DP：从右下角倒推到左上角

        dp[i][j] 表示从(i,j)到达终点所需的最小初始血量

        时间复杂度：O(m*n)
        空间复杂度：O(m*n)
        """
        m, n = len(dungeon), len(dungeon[0])

        # 初始化dp数组，默认为无穷大
        dp = [[float('inf')] * n for _ in range(m)]

        # 终点：到达公主位置至少需要1点血
        # 如果dungeon[m-1][n-1]是负数（扣血），需要更多初始血量
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])

        # 从右下角往左上角填表
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue

                # 从下方或右方进入当前格子
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] - dungeon[i][j])
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] - dungeon[i][j])

                # 确保至少为1（不能死）
                dp[i][j] = max(1, dp[i][j])

        return dp[0][0]
```

### 方法2：空间优化（滚动数组）

使用一维数组优化空间复杂度。

```python
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        空间优化版本

        时间复杂度：O(m*n)
        空间复杂度：O(n)
        """
        m, n = len(dungeon), len(dungeon[0])

        # 只需要一行的空间
        dp = [float('inf')] * (n + 1)
        dp[n-1] = 1  # 哨兵：公主位置右边

        # 从最后一行开始往上遍历
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # dp[j]: 从下方来（上一次迭代的结果）
                # dp[j+1]: 从右方来（当前迭代刚更新的）
                dp[j] = max(1, min(dp[j], dp[j+1]) - dungeon[i][j])

            dp[n] = float('inf')  # 重置哨兵

        return dp[0]
```

### 方法3：极简写法

利用Python切片和列表推导的简洁写法。

```python
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        Python风格的简洁实现

        时间复杂度：O(m*n)
        空间复杂度：O(n)
        """
        n = len(dungeon[0])
        need = [float('inf')] * (n - 1) + [1]  # 初始化最后一列

        # 从最后一行往上遍历
        for row in dungeon[::-1]:
            for j in range(n - 1, -1, -1):
                # need[j:j+2] 取当前和右边的值，min得到最优路径
                need[j] = max(min(need[j:j+2]) - row[j], 1)

        return need[0]
```

## 算法分析

### 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 二维DP | O(m×n) | O(m×n) | 最直观 |
| 滚动数组 | O(m×n) | O(n) | 空间优化 |
| 极简写法 | O(m×n) | O(n) | 代码简洁 |

### 为什么必须逆向DP？

正向DP（从左上到右下）行不通的原因：

```python
# 错误的正向思路
# 无法同时追踪"最小初始血量"和"到达时的血量"
# 这两个目标相互冲突

例如：
路径A：初始7血，到达终点时剩1血
路径B：初始10血，到达终点时剩5血

到达某个中间点时：
- 路径A可能血量更少（但初始血量更优）
- 路径B血量更多（但初始血量更差）

无法判断哪条路径最优！
```

逆向DP的优势：

- 终点状态确定：必须至少1血
- 每个位置只需要知道"从这里到终点需要多少血"
- 状态转移清晰：
  `dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])`

### 状态转移方程

定义 $dp[i][j]$ 为从位置 $(i,j)$ 到达终点所需的最小初始血量。

边界条件：

```text
dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
```

状态转移：

```text
dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
```

解释：

- `min(dp[i+1][j], dp[i][j+1])`：选择下方或右方的最优路径
- 减去 `dungeon[i][j]`：当前格子的增益/损失
- `max(1, ...)`：确保血量至少为1

### 执行过程示例

以 `dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]` 为例。

Step 1：初始化终点

```text
dp[2][2] = max(1, 1 - (-5)) = max(1, 6) = 6
需要6点血才能进入最后一个房间（扣5血后剩1血）
```

Step 2：填充最后一行

```text
dp[2][1] = max(1, 6 - 30) = max(1, -24) = 1
（有30血的补充，只需1点初始血）

dp[2][0] = max(1, 1 - 10) = max(1, -9) = 1
（有10血的补充，只需1点初始血）
```

Step 3：填充倒数第二行

```text
dp[1][2] = max(1, 6 - 1) = 5
dp[1][1] = max(1, min(1, 5) - (-10)) = max(1, 11) = 11
dp[1][0] = max(1, min(11, 1) - (-5)) = max(1, 6) = 6
```

Step 4：填充第一行

```text
dp[0][2] = max(1, 5 - 3) = 2
dp[0][1] = max(1, min(11, 2) - (-3)) = max(1, 5) = 5
dp[0][0] = max(1, min(6, 5) - (-2)) = max(1, 7) = 7
```

最终DP表：

```text
|  7  |  5  |  2  |
|  6  | 11  |  5  |
|  1  |  1  |  6  |
```

最优路径：7 → 5 → 2 → 5 → 6（初始需要7点血）

## 常见错误

### 错误1：使用正向DP

```python
# 错误：从左上到右下
dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + dungeon[i][j]
```

问题：无法保证路径上每一步都 >= 1 的约束。

### 错误2：边界条件错误

```python
# 错误：忘记终点的特殊处理
dp[m-1][n-1] = 1  # 错误！
# 应该是：
dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
```

### 错误3：状态转移方向错误

```python
# 错误：从左上开始遍历
for i in range(m):
    for j in range(n):  # 应该从右下开始
```

### 错误4：忘记max(1, ...)约束

```python
# 错误：可能出现负数或0的血量
dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
# 正确：
dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
```

## 相关题目

- [0064. Minimum Path Sum](./064_minimum_path_sum.md)
- [0062. Unique Paths](./062_unique_paths.md)
- [0063. Unique Paths II](./063_unique_paths_II.md)
- [0120. Triangle](./120_triangle.md)
- [0931. Minimum Falling Path Sum](./931_minimum_falling_path_sum.md)
