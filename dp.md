数位 DP 题单（右边数字为难度分）

    788. 旋转数字（题解）
    902. 最大为 N 的数字组合（题解）1990
    233. 数字 1 的个数（题解）
    面试题 17.06. 2 出现的次数（题解）
    600. 不含连续 1 的非负整数（题解）
    2376. 统计特殊整数（题解）2120
    1012. 至少有 1 位重复的数字（题解）2230
    357. 统计各位数字都不同的数字个数
    2999. 统计强大整数的数目
    2827. 范围中美丽整数的数目 2324
    2801. 统计范围内的步进数字数目 2367
    1397. 找到所有好字符串 2667
    1215. 步进数（会员题）1675
    1067. 范围内的数字计数（会员题）2025
    1742. 盒子中小球的最大数量 *请使用非暴力做法解决
    2719. 统计整数数目

    1744. Number of Digit One
    1745. Numbers At Most N Given Digit Set
    1746. Numbers With Repeated Digits
    1747. Find All Good Strings (Very tough, prerequi site-KMP)

对于dp，我们可以用类似这样的latex语法来写状态转移方程：

$$
[
cnt_{i,j} =
\begin{cases}
    0, & \text{if } \text{isObs}(i, j) \\
    1, & \text{if } i = 0 \text{ and } j = 0 \\
    cnt_{i-1,j}, & \text{if } j = 0 \\
    cnt_{i,j-1}, & \text{if } i = 0 \\
    cnt_{i-1,j} + cnt_{i,j-1}, & \text{otherwise}
\end{cases}
]
$$


1. 递归+记忆化 -> 递推
2. 状态的定义：opt[n], dp[n], fib[n]
3. 状态转移方程：opt[n] = best_of(opt[n-1], opt[n-2], ...)
4. 最优子结构
