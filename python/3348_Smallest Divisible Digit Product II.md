# Smallest Divisible Digit Product II

You are given a string num which represents a positive integer, and an integer t.

A number is called zero-free if none of its digits are 0.

Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".

Example 1:

Input: num = "1234", t = 256

Output: "1488"

Explanation:

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

Example 2:

Input: num = "12355", t = 50

Output: "12355"

Explanation:

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

Example 3:

Input: num = "11111", t = 26

Output: "-1"

Explanation:

No number greater than 11111 has the product of its digits divisible by 26.

Constraints:

    2 <= num.length <= 2 * 10^5
    num consists only of digits in the range ['0', '9'].
    num does not contain leading zeros.
    1 <= t <= 10^14

核心思想

1. 将 t 的整除条件转化为“各数位之积包含足够的质因数 2,3,5,7”，因为数字 1~9 的质因子仅来源于此。

2. 用四维 DP（完全背包）预处理出 达成任意需求的最小位数。例如 dp[a][b][c][d] 表示要凑齐至少 a 个 2、b 个 3、c 个 5、d 个 7 最少需要多少位数字（只用 1~9）。

3. 检查原数字是否已满足条件（且无 0），若满足直接返回。

4. 否则从右向左尝试增大某一位：
    - 前缀不能含 0（否则非法）。
    - 当前位尝试更大的数字 d，计算前缀已经贡献的因子 + d 的因子，得到剩余需求。

    - 用 DP 判断“剩余的位数”是否足以覆盖剩余需求，若能，则贪心地构造后缀：每位优先选最小的数字，使得剩余需求仍可在剩余位数内完成。
    - 若同长度无解，则位数 +1，同样用 DP 找到长度最小、字典序最小的答案。

复杂度

- DP 状态数 ≤ (cnt2+1)*(cnt3+1)*(cnt5+1)*(cnt7+1)，通常很小（例如 t ≤ 10^9 时上限约 30×20×10×7 ≈ 4 万）。
- 贪心扫描 O(n × 9)，构造后缀 O(L × 9)，其中 n 可达 10^5。整体非常高效。

优点

- 确定性构造，无递归回溯，适合极长的 num 和极大的 t。
- 时间复杂度与 num 长度线性相关，非常稳定。

```python
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # ---------- 1. 质因数分解 t ----------
        temp = t
        cnt2 = cnt3 = cnt5 = cnt7 = 0
        while temp % 2 == 0:
            cnt2 += 1
            temp //= 2
        while temp % 3 == 0:
            cnt3 += 1
            temp //= 3
        while temp % 5 == 0:
            cnt5 += 1
            temp //= 5
        while temp % 7 == 0:
            cnt7 += 1
            temp //= 7
        if temp > 1:          # 含有2,3,5,7之外的质因数，无解
            return "-1"

        # 每个数字提供的(2,3,5,7)个数
        factor = [(0,0,0,0)] * 10
        factor[1] = (0,0,0,0)
        factor[2] = (1,0,0,0)
        factor[3] = (0,1,0,0)
        factor[4] = (2,0,0,0)
        factor[5] = (0,0,1,0)
        factor[6] = (1,1,0,0)
        factor[7] = (0,0,0,1)
        factor[8] = (3,0,0,0)
        factor[9] = (0,2,0,0)

        INF = 10**9
        # dp[a][b][c][d] = 达到至少这些质因数个数需要的最少位数（只用1~9）
        dp = [[[[INF] * (cnt7 + 1) for _ in range(cnt5 + 1)]
               for _ in range(cnt3 + 1)] for _ in range(cnt2 + 1)]
        dp[0][0][0][0] = 0

        # 完全背包：每个数字可以无限使用
        for d in range(1, 10):
            f2, f3, f5, f7 = factor[d]
            for a in range(cnt2 + 1):
                for b in range(cnt3 + 1):
                    for c in range(cnt5 + 1):
                        for d7 in range(cnt7 + 1):
                            if dp[a][b][c][d7] != INF:
                                na = min(cnt2, a + f2)
                                nb = min(cnt3, b + f3)
                                nc = min(cnt5, c + f5)
                                nd = min(cnt7, d7 + f7)
                                if dp[na][nb][nc][nd] > dp[a][b][c][d7] + 1:
                                    dp[na][nb][nc][nd] = dp[a][b][c][d7] + 1

        n = len(num)
        # 前缀因子和（不包含当前位）
        pre2, pre3, pre5, pre7 = [0]*(n+1), [0]*(n+1), [0]*(n+1), [0]*(n+1)
        for i, ch in enumerate(num):
            d = int(ch)
            f2, f3, f5, f7 = factor[d] if d != 0 else (0,0,0,0)
            pre2[i+1] = pre2[i] + f2
            pre3[i+1] = pre3[i] + f3
            pre5[i+1] = pre5[i] + f5
            pre7[i+1] = pre7[i] + f7

        # 原数不含0且乘积已满足条件 → 直接返回
        if '0' not in num and pre2[n] >= cnt2 and pre3[n] >= cnt3 and pre5[n] >= cnt5 and pre7[n] >= cnt7:
            return num

        first_zero = num.find('0')   # 最左的0，若无则为-1

        # 构造最小字典序后缀（只用1~9）
        def build_suffix(need2, need3, need5, need7, length):
            res = []
            for _ in range(length):
                for d in range(1, 10):
                    f2, f3, f5, f7 = factor[d]
                    n2 = max(0, need2 - f2)
                    n3 = max(0, need3 - f3)
                    n5 = max(0, need5 - f5)
                    n7 = max(0, need7 - f7)
                    if dp[n2][n3][n5][n7] <= length - len(res) - 1:
                        res.append(str(d))
                        need2, need3, need5, need7 = n2, n3, n5, n7
                        break
            return "".join(res)

        # 贪心扫描：从右向左，但只能选前缀不含0的位置
        for i in range(n - 1, -1, -1):
            if first_zero != -1 and i > first_zero:  # 前缀有0，无效
                continue
            cur = int(num[i])
            start_d = cur + 1 if cur != 0 else 1     # 原数字为0则从1开始尝试
            for d in range(start_d, 10):
                f2 = pre2[i] + factor[d][0]
                f3 = pre3[i] + factor[d][1]
                f5 = pre5[i] + factor[d][2]
                f7 = pre7[i] + factor[d][3]
                need2 = max(0, cnt2 - f2)
                need3 = max(0, cnt3 - f3)
                need5 = max(0, cnt5 - f5)
                need7 = max(0, cnt7 - f7)
                if dp[need2][need3][need5][need7] <= n - 1 - i:
                    suffix = build_suffix(need2, need3, need5, need7, n - 1 - i)
                    return num[:i] + str(d) + suffix

        # 同长度无解 → 增加位数
        min_len = dp[cnt2][cnt3][cnt5][cnt7]
        L = max(n + 1, min_len)
        for d in range(1, 10):
            f2, f3, f5, f7 = factor[d]
            need2 = max(0, cnt2 - f2)
            need3 = max(0, cnt3 - f3)
            need5 = max(0, cnt5 - f5)
            need7 = max(0, cnt7 - f7)
            if dp[need2][need3][need5][need7] <= L - 1:
                suffix = build_suffix(need2, need3, need5, need7, L - 1)
                return str(d) + suffix

        return "-1"
```

核心思想

1. 同样先将 t 分解，若含其他质因数则返回 -1。
2. 在原数字前补若干个 '0' 作为占位符，数量由质因数总个数和原长估算，以允许最终答案长度可能增加。
3. 使用深度优先搜索（DFS）逐位确定数字，状态为 (i, t_remain, is_limit)：

    - i：当前处理到的位置。
    - t_remain：当前剩余需要被整除的 t（经过与已选数字的 gcd 不断约简）。
    - is_limit：是否仍受原数字上界限制。

4. 记忆化：对 (i, t_remain) 在没有 is_limit 限制时进行缓存，避免重复搜索。
5. 每一位尝试从 max(low, 1) 到 9 的数字，递归判断可行性。
6. 最终答案去掉前导零得到结果。

复杂度

- 状态空间取决于 t_remain 的可能取值。t_remain 在搜索中会被不断约简，其不同的值不会太多（通常 ≤ 几千），加上位数的维度，总状态数可接受。
- 但由于有递归和回溯，在 n 极大时（如 10^5）可能导致深度过大或常数过大，不如解法一稳定。

优点

- 代码非常简洁，数位 DP 框架清晰易懂。
- 通过补前导零巧妙处理了位数增加的问题，无需单独构造。
- 对于一般范围的 num 和 t，实际运行速度也很快。

```python
class Solution:
    def smallestNumber(self, s: str, t: int) -> str:
        tmp = t
        cnt = 0
        for p in 2, 3, 5, 7:
            while tmp % p == 0:
                tmp //= p
                cnt += 1
        if tmp > 1:  # t 包含其他质因子
            return "-1"

        # 补前导零（至少一个）
        cnt = max(cnt - len(s) + 1, 1)
        s = '0' * cnt + s

        n = len(s)
        ans = ['0'] * n
        vis = [set() for _ in range(n)]

        def dfs(i: int, t: int, is_limit: bool) -> bool:
            if i == n:
                return t == 1

            if not is_limit:
                if t in vis[i]:
                    return False
                vis[i].add(t)

            if is_limit and i < cnt and dfs(i + 1, t, True):  # 填 0（跳过）
                return True

            low = int(s[i]) if is_limit else 0
            for d in range(max(low, 1), 10):
                if dfs(i + 1, t // gcd(t, d), is_limit and d == low):
                    ans[i] = str(d)
                    return True
            return False

        dfs(0, t, True)
        return ''.join(ans).lstrip('0')  # 去掉前导零
```

| 维度 | 第一段（你的 DP + 贪心） | 第二段（DFS + GCD） |
| --- | --- | --- |
| 本质模型 | 质因数计数背包 | 整除性状态压缩 |
| 状态定义 | 还差多少个 2/3/5/7 | 当前 t 还剩多少没被整除 |
| 搜索目标 | 构造最小字典序数字 | 搜索满足条件的数字 |
| 剪枝方式 | DP 预计算最少位数 | memo + gcd 快速收敛 |
| 复杂度 | 四维 DP，稳定可控 | 指数级，依赖 GCD 剪枝 |
| 风格 | 工程化、偏数学 | 竞赛风、偏技巧 |

这两段代码的差异，本质上是“数学建模派” vs “算法技巧派”的区别，也是你之前 TLE 的根本原因所在。我直接点透核心差异，再逐层展开。
