# Minimum Total Distance Traveled

[[greedy]] [[dp]]

There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

Note that

    All robots move at the same speed.
    If two robots move in the same direction, they will never collide.
    If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
    If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
    If the robot moved from a position x to a position y, the distance it moved is |y - x|.

Example 1:

Input: robot = [0,4,6], factory = [[2,2],[6,2]]
Output: 4
Explanation: As shown in the figure:

- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
- The third robot at position 6 will be repaired at the second factory. It does not need to move.
The limit of the first factory is 2, and it fixed 2 robots.
The limit of the second factory is 2, and it fixed 1 robot.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.

Example 2:

Input: robot = [1,-1], factory = [[-2,1],[2,1]]
Output: 2
Explanation: As shown in the figure:

- The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
- The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
The limit of the first factory is 1, and it fixed 1 robot.
The limit of the second factory is 1, and it fixed 1 robot.
The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.

Constraints:

    1 <= robot.length, factory.length <= 100
    factory[j].length == 2
    -109 <= robot[i], positionj <= 109
    0 <= limitj <= robot.length
    The input will be generated such that it is always possible to repair every robot.

## 一、贪心性质

看上去，一个工厂修理一段连续的机器人是最优的。为什么？

先排序，设工厂的位置为 f1​<f2​<⋯<fn​，机器人的位置为 r1​<r2​<⋯<rm​。

    注：题目保证工厂的位置互不相同，机器人的位置互不相同。

对于序列中的两个工厂 fa​ 和 `fb​（a<b）`，两个机器人 ri​ 和 `rj​（i<j）`，对比如下两个方案：

    ri​ 去 fa​，rj​ 去 fb​，移动距离之和为 ∣ri​−fa​∣+∣rj​−fb​∣。
    ri​ 去 fb​，rj​ 去 fa​，移动距离之和为 ∣ri​−fb​∣+∣rj​−fa​∣。

用分类讨论可以证明，∣ri​−fa​∣+∣rj​−fb​∣≤∣ri​−fb​∣+∣rj​−fa​∣。

换句话说，存在这样的最优解，对于任意一对机器人 i 和 `j（i<j）`，机器人 i 去的工厂编号 ≤ 机器人 j 去的工厂编号。同一个工厂修理的机器人，在排序后的机器人序列里是连续的一段。

## 二、寻找子问题

在示例 1 中，我们要解决的问题（原问题）是：

    工厂下标区间 [0,1] 修理机器人下标区间 [0,2]，机器人移动的最小总距离。

从右往左思考，枚举最后一个工厂修多少个机器人：

    修 0 个机器人，问题变成：工厂 [0,0] 修理机器人 [0,2]，机器人移动的最小总距离。
    修 1 个机器人，问题变成：工厂 [0,0] 修理机器人 [0,1]，机器人移动的最小总距离。
    修 2 个机器人，问题变成：工厂 [0,0] 修理机器人 [0,0]，机器人移动的最小总距离。
    至多修 2 个，因为 limit1​=2。

这些问题都是和原问题相似的、规模更小的子问题，可以用递归解决。

    注：从右往左思考，主要是方便把递归翻译成递推。从左往右思考也是可以的。

三、状态定义与状态转移方程

根据上面的讨论，定义 dfs(i,j) 表示工厂下标区间 [0,i] 修理机器人下标区间 [0,j]，机器人移动的最小总距离。

枚举工厂 i 修 $k=0,1,2…,min(j+1,limit_i​)$ 个机器人，问题变成工厂下标区间 [0,i−1] 修理机器人下标区间 [0,j−k]，机器人移动的最小总距离，即 dfs(i−1,j−k)，再加上机器人 [j−k+1,j] 到工厂 i 的距离。

对所有 k 取最小值，就得到了 dfs(i,j)，即

$dfs(i,j) = \min_{0 \le k \le \min(j+1,limit_i)} \{ dfs(i-1,j-k) + \sum_{t=j-k+1}^{j} |robot[t] - factory[i] \}$。

由于 k 每增加 1，距离和 p=j−k+1∑j​∣robot[p]−position[i]∣ 就会新增一项 ∣robot[j−k+1]−position[i]∣，所以可以用一个变量 disSum 维护距离和，而不是对每个 k 都跑一个循环算距离和。

递归边界：

    dfs(i,−1)=0。没有机器人了，总移动距离为 0。
    dfs(−1,j)=∞ (j≥0)。没有工厂，但还有剩下的机器人，不合法。返回 ∞，这样上面公式中的 min 不会取到不合法的情况。

递归入口：dfs(n−1,m−1)，这是原问题，也是答案。

    注：题目保证所有机器人都可以被维修。

四、递归搜索 + 保存递归返回值 = 记忆化搜索

考虑到整个递归过程中有大量重复递归调用（递归入参相同）。由于递归函数没有副作用，同样的入参无论计算多少次，算出来的结果都是一样的，因此可以用记忆化搜索来优化：

    如果一个状态（递归入参）是第一次遇到，那么可以在返回前，把状态及其结果记到一个 memo 数组中。
    如果一个状态不是第一次遇到（memo 中保存的结果不等于 memo 的初始值），那么可以直接返回 memo 中保存的结果。

⚠注意：memo 数组的初始值一定不能等于要记忆化的值！例如初始值设置为 0，并且要记忆化的 dfs(i,j) 也等于 0，那就没法判断 0 到底表示第一次遇到这个状态，还是表示之前遇到过了，从而导致记忆化失效。一般把初始值设置为 −1。

    Python 用户可以无视上面这段，直接用 @cache 装饰器。

```python
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort(key=lambda f: f[0])
        robot.sort()

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if j < 0:  # 所有机器人都修完了
                return 0
            if i < 0:  # 还有机器人没修，但没有工厂了
                return inf

            # 工厂 i 不修机器人
            res = dfs(i - 1, j)

            position, limit = factory[i]
            dis_sum = 0
            # 枚举修 k 个机器人
            for k in range(1, min(j + 1, limit) + 1):
                dis_sum += abs(robot[j - k + 1] - position)
                res = min(res, dfs(i - 1, j - k) + dis_sum)

            return res

        return dfs(len(factory) - 1, len(robot) - 1)
```

复杂度分析

    时间复杂度：O(nm2+nlogn)，其中 n 是 factory 的长度，m 是 robot 的长度。由于每个状态只会计算一次，动态规划的时间复杂度 = 状态个数 × 单个状态的计算时间。本题状态个数等于 O(nm)，单个状态的计算时间为 O(m)，所以记忆化搜索的时间复杂度为 O(nm2)。剩下的 O(nlogn+mlogm) 是排序的时间复杂度，由于 O(mlogm) 比 O(nm2) 小，可以省略。
    空间复杂度：O(nm)。保存多少状态，就需要多少空间。

五、1:1 翻译成递推

我们可以去掉递归中的「递」，只保留「归」的部分，即自底向上计算。

具体来说，f[i+1][j+1] 的定义和 dfs(i,j) 的定义是一样的，都表示工厂下标区间 [0,i] 修理机器人下标区间 [0,j]，机器人移动的最小总距离。这里 +1 是为了把 dfs(i,−1) 和 dfs(−1,j) 也翻译过来，这样我们可以把 f[i][0] 和 f[0][j] 作为初始值。

相应的递推式（状态转移方程）也和 dfs 一样：$$f[i+1][j+1] = \min_{0 \le k \le \min(j+1,limit_i)} \{ f[i][j-k] + \sum_{t=j-k+1}^{j} |robot[t] - factory[i]| \}$$

初始值 f[i][0]=0 以及 f[0][j]=∞ (j≥1)，翻译自递归边界。

答案为 f[n][m]，翻译自递归入口.

```python
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort(key=lambda f: f[0])
        robot.sort()

        n, m = len(factory), len(robot)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        f[0][1:] = [inf] * m

        for i, (position, limit) in enumerate(factory):
            for j in range(m):
                # 工厂 i 不修机器人
                res = f[i][j + 1]

                # 枚举修 k 个机器人
                dis_sum = 0
                for k in range(1, min(j + 1, limit) + 1):
                    dis_sum += abs(robot[j - k + 1] - position)
                    res = min(res, f[i][j - k + 1] + dis_sum)

                f[i + 1][j + 1] = res

        return f[n][m]
```

为了方便大家阅读下一章（单调队列优化），先微调一下状态定义和状态转移方程。

把 j+1 替换成 j，定义 f[i+1][j] 表示工厂下标区间 [0,i] 修理机器人下标区间 [0,j−1]，机器人移动的最小总距离。

状态转移方程为：$$f[i+1][j] = \min_{0 \le k \le \min(j,limit_i)} \{ f[i][j-k] + \sum_{t=j-k}^{j-1} |robot[t] - factory[i]| \}$

这样可以少写很多 +1。

在 k 从 0 增大到 min(limiti​,j) 的过程中，j−k 从 j 减小到 max(j−limiti​,0)。

把 j−k 替换成 k，状态转移方程为：$$f[i+1][j] = \min_{k=\max(j-limit_i,0)}^{j} \{ f[i][k] + \sum_{t=k}^{j-1} |robot[t] - factory[i]| \}$$

这样转移方程就更干净了，从而方便我们进一步优化。

    注：这相当于在枚举工厂 i 修理的最左边的机器人的编号 k。

```python
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort(key=lambda f: f[0])
        robot.sort()

        n, m = len(factory), len(robot)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        f[0][1:] = [inf] * m

        for i, (position, limit) in enumerate(factory):
            for j in range(1, m + 1):
                # 工厂 i 不修机器人
                res = f[i][j]

                # 修理下标在 [k, j-1] 中的机器人
                dis_sum = 0
                for k in range(j - 1, max(j - limit, 0) - 1, -1):
                    dis_sum += abs(robot[k] - position)
                    res = min(res, f[i][k] + dis_sum)

                f[i + 1][j] = res

        return f[n][m]
```

复杂度分析

    时间复杂度：O(nm2+nlogn)，其中 n 是 factory 的长度，m 是 robot 的长度。DP 的时间复杂度为 O(nm2)。剩下的 O(nlogn+mlogm) 是排序的时间复杂度，由于 O(mlogm) 比 O(nm2) 小，可以省略。
    空间复杂度：O(nm)。

## 六、单调队列优化

定义 di​[p]=∣robot[p]−position[i]∣。

设 di​ 数组的前缀和数组为 si​。关于 si​ 的定义，请看 前缀和。

状态转移方程为：

$$f[i+1][j] = \min_{k=\max(j-limit_i,0)}^{j} \{ f[i][k] + s_i[j] - s_i[k] \}$$
$$= s_i[j] + \min_{k=\max(j-limit_i,0)}^{j} \{ f[i][k] - s_i[k] \}$$

当 j 增大时，k 的范围是一个向右移动的滑动窗口，我们计算的是 f[i][k]−si​[k] 的滑动窗口最小值。上式的 min 可以用单调队列优化至均摊 O(1) 时间复杂度。
答疑

问：对于单调队列优化 DP，什么时候先把元素入队再计算 DP，什么时候先计算 DP 再把元素入队？

答：这取决于计算的 DP 是否包含要入队的元素。如果包含，那就先入队再计算 DP；如果不包含，那就先计算 DP 再入队。本题是前者。

```python
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort(key=lambda f: f[0])
        robot.sort()

        n, m = len(factory), len(robot)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        f[0][1:] = [inf] * m

        for i, (position, limit) in enumerate(factory):
            dis_sum = list(accumulate((abs(r - position) for r in robot), initial=0))  # 前缀和
            q = deque([(0, 0)])
            for j in range(1, m + 1):
                # 1. 入
                v = f[i][j] - dis_sum[j]
                while q and q[-1][1] >= v:
                    q.pop()
                q.append((j, v))

                # 2. 出
                while q[0][0] < j - limit:
                    q.popleft()

                # 3. 队首为滑动窗口最小值
                f[i + 1][j] = dis_sum[j] + q[0][1]

        return f[n][m]
```

复杂度分析

    时间复杂度：O(nm+nlogn+mlogm)，其中 n 是 factory 的长度，m 是 robot 的长度。对于三重循环里面的二重循环，站在每个元素的视角看，这个元素在二重循环中最多入队出队各一次，因此二重循环的循环次数之和是 O(m)，所以三重循环的时间复杂度是 O(nm)。剩下的 O(nlogn+mlogm) 是排序的时间复杂度。
    空间复杂度：O(nm)。

七、空间优化

观察上面的代码，计算 f[i+1][j] 只会用到 f[i][j]。

所以只需要一个长为 m+1 的一维数组 f，我们直接把计算结果覆盖到 f[j] 中。

此外，前缀和可以一边枚举 j 一边计算，从而优化成一个变量。

```python
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort(key=lambda f: f[0])
        robot.sort()

        m = len(robot)
        f = [0] + [inf] * m

        for position, limit in factory:
            dis_sum = 0
            q = deque([(0, 0)])
            for j, r in enumerate(robot, 1):  # r = robot[j - 1]
                dis_sum += abs(r - position)

                # 1. 入
                v = f[j] - dis_sum
                while q and q[-1][1] >= v:
                    q.pop()
                q.append((j, v))

                # 2. 出
                while q[0][0] < j - limit:
                    q.popleft()

                # 3. 队首为滑动窗口最小值
                f[j] = dis_sum + q[0][1]

        return f[m]
```

复杂度分析

    时间复杂度：O(nm+nlogn+mlogm)，其中 n 是 factory 的长度，m 是 robot 的长度。对于三重循环里面的二重循环，站在每个元素的视角看，这个元素在二重循环中最多入队出队各一次，因此二重循环的循环次数之和是 O(m)，所以三重循环的时间复杂度是 O(nm)。剩下的 O(nlogn+mlogm) 是排序的时间复杂度。
    空间复杂度：O(m)。忽略排序的栈开销。
