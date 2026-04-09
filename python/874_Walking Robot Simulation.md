# Walking Robot Simulation

A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot receives an array of integers commands, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.

Return the maximum squared Euclidean distance that the robot reaches at any point in its path (i.e. if the distance is 5, return 25).

Note:

There can be an obstacle at (0, 0). If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to (0, 0) due to the obstacle.
North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.

Example 1:

Input: commands = [4,-1,3], obstacles = []

Output: 25

Explanation:

The robot starts at (0, 0):

Move north 4 units to (0, 4).
Turn right.
Move east 3 units to (3, 4).
The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.

Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]

Output: 65

Explanation:

The robot starts at (0, 0):

Move north 4 units to (0, 4).
Turn right.
Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
Turn left.
Move north 4 units to (1, 8).
The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.

Example 3:

Input: commands = [6,-1,-1,6], obstacles = [[0,0]]

Output: 36

Explanation:

The robot starts at (0, 0):

Move north 6 units to (0, 6).
Turn right.
Turn right.
Move south 5 units and get blocked by the obstacle at (0,0), robot is at (0, 1).
The furthest point the robot ever gets from the origin is (0, 6), which squared is 62 = 36 units away.

Constraints:

1 <= commands.length <= 10^4
commands[i] is either -2, -1, or an integer in the range [1, 9].
0 <= obstacles.length <= 10^4
-3 *10^4 <= xi, yi <= 3* 10^4
The answer is guaranteed to be less than 2^31.

```python
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
mx = lambda x, y: x if x > y else y

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        ans = dir_p = cur_x = cur_y = 0
        for c in commands:
            if c < 0:
                dir_p += 1 if c == -1 else -1
                dir_p %= 4
            else:
                dy, dx = dirs[dir_p]
                for _ in range(c):
                    cur_x += dx
                    cur_y += dy
                    if (cur_x, cur_y) in obstacles:
                        cur_x -= dx
                        cur_y -= dy
                        break
                ans = mx(ans, cur_x * cur_x + cur_y * cur_y)
        return ans
```

```python
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = {(x, y) for x, y in obstacles}
        dist = 0
        x, y = 0, 0
        dx, dy = 0, 1

        for move in commands:
            if move == -2:
                dx, dy = -dy, dx
            elif move == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(move):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x, y = x + dx, y + dy
                dist = max(dist, x * x + y * y)
        return dist
```

总体思路：模拟机器人行走的过程。一步一步走，如果下一步是障碍物，则停止移动，继续执行下一个命令。

怎么表示机器人移动的方向？

我们可以用一个向量数组: dirs=[(0,1),(1,0),(0,−1),(−1,0)]

分别表示顺时针的上右下左（北东南西）四个方向。

用一个下标 k 表示当前机器人的方向为 dirs[k]，初始 k=0，表示初始方向为上。

- 右转：也就是顺时针转 90∘，把 k 增加一。如果 k=4，则绕回到 dirs 数组的最左边，即 k 更新为 0。我们可以把 k 统一更新为 (k+1)mod4，这样可以兼容 k=3 加一后变成 0 的情况。
- 左转：也就是逆时针转 90∘，把 k 减少一。如果 k=0，则绕回到 dirs 数组的最右边，即 k 更新为 3。我们可以把 k 统一更新为 (k+3)mod4，这是因为 dirs 是个循环数组，一个元素的左边相邻元素，相当于往右数 3 个元素。比如 dirs 中的 (1,0) 往右数 3 个元素，就是 (0,1)。

设 c=commands[i]。当 c>0 时，机器人要往 dirs[k] 方向移动 c 个单位长度。一步一步移动，如果发现下一步是障碍物，则停止移动，继续执行下一个命令。

为了快速判断某个坐标是否为障碍物（是否在 obstacles 数组中），我们可以把 obstacles 转成哈希集合，判断坐标是否在哈希集合中。

```python
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 上右下左（顺时针）

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        ans = x = y = k = 0
        for c in commands:
            if c == -1:  # 右转
                k = (k + 1) % 4
            elif c == -2:  # 左转
                k = (k + 3) % 4
            else:  # 直行
                while c > 0 and (x + DIRS[k][0], y + DIRS[k][1]) not in obstacle_set:
                    x += DIRS[k][0]
                    y += DIRS[k][1]
                    c -= 1
                ans = max(ans, x * x + y * y)
        return ans
```

设 c=commands[i]。

    右转时 c=−1，我们把 k 增加了 2c+3=1。
    左转时 c=−2，我们把 k 增加了 2c+3=−1。

因此，这两种情况可以进一步统一成，把 k 更新成 (k+2c+3)mod4。但是，当 k=0 且 2c+3=−1 时，k+2c+3=−1 是负数。对于模 4 运算，多增加 4 不影响结果，所以可以把 2c+3 改成 2c+7，也就把 k 更新成
`(k+2c+7) mod 4`

```python
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 上右下左（顺时针）

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        ans = x = y = k = 0
        for c in commands:
            if c < 0:
                k = (k + c * 2 + 7) % 4  # c=-2 左转，c=-1 右转
                continue
            while c > 0 and (x + DIRS[k][0], y + DIRS[k][1]) not in obstacle_set:
                x += DIRS[k][0]
                y += DIRS[k][1]
                c -= 1
            ans = max(ans, x * x + y * y)
        return ans
```
