# Walking Robot Simulation II

A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each step, it does the following.

    Attempts to move forward one cell in the direction it is facing.
    If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.

After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the Robot class:

    Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
    void step(int num) Instructs the robot to move forward num steps.
    int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
    String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".

Example 1:
example-1

Input
["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
Output
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

Explanation
Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2);  // It moves two steps East to (2, 0), and faces East.
robot.step(2);  // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.step(2);  // It moves one step East to (5, 0), and faces East.
                // Moving the next step East would be out of bounds, so it turns and faces North.
                // Then, it moves one step North to (5, 1), and faces North.
robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
                // Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return "West"

Constraints:

    2 <= width, height <= 100
    1 <= num <= 10^5
    At most 10^4 calls in total will be made to step, getPos, and getDir.

本文把 width 简称为 w，把 height 简称为 h。

根据题意，机器人只能在网格图的最外圈中移动，移动一整圈需要 2(w+h−2) 步。

设当前移动的总步数模 2(w+h−2) 的结果为 s。分类讨论：

    如果 s<w，机器人往右走了 s 步，位于 (s,0)，面朝东。
    如果 w≤s<w+h−1，机器人先往右走 w−1 步，再往北走 s−(w−1) 步，位于 (w−1,s−w+1)，面朝北。
    如果 w+h−1≤s<2w+h−2，机器人先往右走 w−1 步，再往北走 h−1 步，到达右上角 (w−1,h−1)，再往西走 s−(w−1)−(h−1) 步，位于 (w−1−(s−(w−1)−(h−1)),h−1)=(2w+h−s−3,h−1)，面朝西。
    否则，机器人先往右走 w−1 步，再往北走 h−1 步，再往西走 w−1 步，到达左上角 (0,h−1)，再往南走 s−2(w−1)−(h−1) 步，位于 (0,h−1−(s−2(w−1)−(h−1)))=(0,2(w+h)−s−4)，面朝南。

⚠注意：总步数为 0 时，机器人面朝东，但总步数为 2(w+h−2) 的正整数倍时，机器人面朝南。需要特判总步数为 0 的特殊情况吗？不需要，当总步数大于 0 时，我们可以把取模后的范围从 [0,2(w+h−2)−1] 调整到 [1,2(w+h−2)]，从而使原先模为 0 的总步数变成 2(w+h−2)，落入面朝南的分支中，这样就可以避免特判了。

```python
class Robot:
    def __init__(self, width: int, height: int) -> None:
        self.w = width
        self.h = height
        self.s = 0

    def step(self, num: int) -> None:
        # 由于机器人只能走外圈，那么走 (w+h-2)*2 步后会回到起点
        # 把 s 取模调整到 [1, (w+h-2)*2]，这样不需要特判 s == 0 时的方向
        self.s = (self.s + num - 1) % ((self.w + self.h - 2) * 2) + 1

    def _getState(self) -> Tuple[int, int, str]:
        w, h, s = self.w, self.h, self.s
        if s < w:
            return s, 0, "East"
        if s < w + h - 1:
            return w - 1, s - w + 1, "North"
        if s < w * 2 + h - 2:
            return w * 2 + h - s - 3, h - 1, "West"
        return 0, (w + h) * 2 - s - 4, "South"

    def getPos(self) -> List[int]:
        x, y, _ = self._getState()
        return [x, y]

    def getDir(self) -> str:
        return self._getState()[2]
```
