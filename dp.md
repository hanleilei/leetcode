# dynamic programming

1. 看wikipedia的定义：<https://en.wikipedia.org/wiki/Dynamic_programming>
2. simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner.
3. Divide& conquer: + optimal substructure + overlapping subproblems 分治 + 最优子结构 + 重叠子

关键点：

1. 动态规划和递归或者分治 没有根本上的区别（关键看有无最优子结构和重叠子问题）。动态规划是递归的优化版本，通常通过记忆化或者迭代来实现。
2. 共性：找到重复子问题
3. 差异性：最优子结构（optimal substructure）中途可以淘汰次优解，分治则需要保留所有解。

4. 最优子结构 opt[n] = best_of(opt[n-1], opt[n-2], ...)
5. 存储中间状态 opt[n] = ...
6. 递推公式（美其名曰：状态转移方程或者dp方程）fib: opt[n] = opt[n-1] + opt[n-2]
   二维路径：opt[i][j] = opt[i-1][j] + opt[i][j-1]（且判断a[i][j]是否为空）

## LCS类问题

1143/最长公共子序列
1035/不相交的线
583/删除操作使两个字符串相同
712/最小ASCII删除和

对于dp，我们可以用类似这样的latex语法来写状态转移方程：

$$
cnt_{i,j} =
\begin{cases}
    0, & \text{if } \text{isObs}(i, j) \\
    1, & \text{if } i = 0 \text{ and } j = 0 \\
    cnt_{i-1,j}, & \text{if } j = 0 \\
    cnt_{i,j-1}, & \text{if } i = 0 \\
    cnt_{i-1,j} + cnt_{i,j-1}, & \text{otherwise}
\end{cases}
$$

1. 递归+记忆化 -> 递推
2. 状态的定义：opt[n], dp[n], fib[n]
3. 状态转移方程：opt[n] = best_of(opt[n-1], opt[n-2], ...)
4. 最优子结构

---

1. 构造问题：问题的条件就是题目给出的所有条件。
2. 拆解子问题：将问题拆解成若干个子问题，子问题的解可以递归地构造出原问题的解。
3. 定义状态：确定子问题的状态变量，通常是一个或多个整数，用于唯一标识子问题。
4. 状态转移方程：根据子问题的解，建立状态转移方程，描述如何通过较小子问题的解来构造较大子问题的解。
5. 边界条件：确定初始状态和边界条件，确保递归或迭代过程能够正确终止。
6. 计算顺序：确定计算子问题的顺序，通常采用自底向上或自顶向下的方式。
7. 最终解：根据状态转移方程和边界条件，计算出原问题的解。

---

1. 构造问题：列出题目的所有条件和目标。
2. 拆解子问题：将问题分解为更小的子问题，也就是定义状态，确保子问题之间相互独立。
3. 求解子问题：通过递归或迭代的方式求解子问题，通常使用记忆化搜索或动态规划表格。
4. 通过已知的子问题的解，推到所有问题的解，即构建状态转移方程。
5. 判断复杂度，必须在千万级别以内。

---
