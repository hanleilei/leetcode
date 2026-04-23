# Reach a Number

[[math]]

You are standing at position 0 on an infinite number line. There is a destination at position target.

You can make some number of moves numMoves so that:

    On each move, you can either go left or right.
    During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.

Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) to reach the destination.

Example 1:

Input: target = 2
Output: 3
Explanation:
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to -1 (2 steps).
On the 3rd move, we step from -1 to 2 (3 steps).

Example 2:

Input: target = 3
Output: 2
Explanation:
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to 3 (2 steps).

Constraints:

    -10^9 <= target <= 10^9
    target != 0

分类讨论：

1. target = 10， 这恰好到达。
2. 如果越过终点，并且相距偶数，例如target = 8， 则解决方法为：如果相距2，第一步反向走，如果相距4，第二步反向走，如果相距6，第三步反向走，以此类推。
3. 如果越过终点，并且相距奇数，例如target = 9，则解决方法为：多走一步，如果相距变为偶数，则按照第二种情况处理，否则按照情况四处理。
4. 如果越过终点，并且相距奇数，并且多走一步后仍然相距奇数，例如target = 11，则解决方法为：再多走一步，此时相距变为偶数，按照第二种情况处理。

为方便描述，如果终点 target<0，根据对称性，可将其变为 −target，这不影响结果。

问：对于情况四，为什么多走两步一定可以把到终点的距离变为偶数？

答：此时相距为奇数，多走两步，奇数再加上两个相邻数字（必定一偶一奇），即奇数+偶数+奇数，可以得到偶数。

问：为什么相距为偶数时，一定可以通过把某些步反向，恰好到达终点？

答：设走了 n 步后，步长之和 s=1+2+⋯+n=2n(n+1)​。
这里需要一个小结论：[1,s] 内的每个数字都可以由若干个不同的 [1,n] 内的数组成。
证明：n=1,2 时显然。假设 n=k (k≥2) 时结论成立，此时已经得到了 [1,s] 内的每个数字（这里 s=2k(k+1)​），我们可以用 [s−k,s] 内的数字加上 k+1，从而得到 [s+1,s+k+1] 内的每个数字，即得到了 [1,s+k+1] 内的每个数字，即证明了当 n=k+1 时结论也成立。根据数学归纳法，原结论成立。
由于相距 `d=s−target<s`，根据结论，在 d 为偶数时，一定可以选择某些步，满足这些步长的和为 2d​，将这些步反向，就能恰好到达终点。

问：为什么按图中的方法，走的步数一定是最小的？

答：将原问题转换成一个等价问题「先一直往终点走，然后选择某些步反向，所需要的最小步数」，然后在该问题上讨论。
情况一二可以用反证法，不走 n 步根本无法到达终点（这里第 n 步恰好到达或越过终点）。
情况三四，由于反向操作只能将 s 减少偶数，无法处理相距奇数的情况，必须多走一两步，将相距变为偶数，才能处理。

代码实现时，我们可以不断循环，累加当前步长 n，当到达（越过）终点且相距偶数时停止。最后一步的步长即为答案。

```python
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        s = n = 0
        while s < target or (s - target) % 2:
            n += 1
            s += n
        return n
```
