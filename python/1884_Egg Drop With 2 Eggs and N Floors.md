# Egg Drop With 2 Eggs and N Floors

[[math]] [[binarySearch]]

You are given two identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

In each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.

Example 1:

Input: n = 2
Output: 2
Explanation: We can drop the first egg from floor 1 and the second egg from floor 2.
If the first egg breaks, we know that f = 0.
If the second egg breaks but the first egg didn't, we know that f = 1.
Otherwise, if both eggs survive, we know that f = 2.

Example 2:

Input: n = 100
Output: 14
Explanation: One optimal strategy is:

- Drop the 1st egg at floor 9. If it breaks, we know f is between 0 and 8. Drop the 2nd egg starting from floor 1 and going up one at a time to find f within 8 more drops. Total drops is 1 + 8 = 9.
- If the 1st egg does not break, drop the 1st egg again at floor 22. If it breaks, we know f is between 9 and 21. Drop the 2nd egg starting from floor 10 and going up one at a time to find f within 12 more drops. Total drops is 2 + 12 = 14.
- If the 1st egg does not break again, follow a similar process dropping the 1st egg from floors 34, 45, 55, 64, 72, 79, 85, 90, 94, 97, 99, and 100.Regardless of the outcome, it takes at most 14 drops to determine f.

Constraints:

    1 <= n <= 1000

这个题目是887的一个特例，887题是k个鸡蛋和n层楼，k=2就是这个题。

$$dp(K, N) = \min_{1 \le i \le N} \left( \max(j, dp(i - j) + 1) \right)$$

```python
class Solution:
    def twoEggDrop(self, n: int) -> int:
        f = [0] * 1001
        for i in range(1, len(f)):
            f[i] = min(max(j, f[i - j] + 1) for j in range(1, i + 1))
        return f[n]
```

一般地，设答案为 x，必须满足
$$x+(x−1)+(x−2)+⋯+2+1 \ge n$$

即
$$2x(x+1)​\ge n$$

解一元二次不等式，得
$$x\ge \frac{-1+\sqrt{1+8n}}{2}$$

由于 x 是整数，所以最小的 x 为
$$\lceil\frac{-1+\sqrt{1+8n}}{2}\rceil$$

```python
class Solution:
    def twoEggDrop(self, n: int) -> int:
        # return ceil((sqrt(n * 8 + 1) - 1) / 2)
        return ceil(sqrt(n * 8 + 1)) // 2
```

```python
class Solution:
    def twoEggDrop(self, n: int) -> int:
        i = 0
        while i * (i + 1) // 2 < n:
            i += 1
        return i
```

```python
class Solution:
    def twoEggDrop(self, n: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int) -> int:
            if i == 0:
                return 0
            return min(max(j, dfs(i - j) + 1) for j in range(1, i + 1))
        
        return dfs(n)
```
