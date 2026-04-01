# interval overlapping

[435 Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals)
[452 Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons)

贪心: 当下做局部最优判断
回溯：能够回退
动态规划：最优判断 + 回退

贪心和动态规划的不同之处：

- 贪心对于每个子问题的解决方案都做出选择，不能回退。
- 动态规划会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

贪心解决最优化问题，如图中的最小生成树，哈夫曼编码等。对于工程和生活中的问题，贪心法一般不能的到我们所要求的答案。

一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好方法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。
