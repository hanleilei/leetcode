# XOR After Range Multiplication Queries I

You are given an integer array nums of length n and a 2D integer array queries of size q, where queries[i] = [li, ri, ki, vi].

For each query, you must apply the following operations in order:

    Set idx = li.
    While idx <= ri:
        Update: nums[idx] = (nums[idx] * vi) % (109 + 7)
        Set idx += ki.

Return the bitwise XOR of all elements in nums after processing all queries.

Example 1:

Input: nums = [1,1,1], queries = [[0,2,1,4]]

Output: 4

Explanation:

    A single query [0, 2, 1, 4] multiplies every element from index 0 through index 2 by 4.
    The array changes from [1, 1, 1] to [4, 4, 4].
    The XOR of all elements is 4 ^ 4 ^ 4 = 4.

Example 2:

Input: nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]

Output: 31

Explanation:

    The first query [1, 4, 2, 3] multiplies the elements at indices 1 and 3 by 3, transforming the array to [2, 9, 1, 15, 4].
    The second query [0, 2, 1, 2] multiplies the elements at indices 0, 1, and 2 by 2, resulting in [4, 18, 2, 15, 4].
    Finally, the XOR of all elements is 4 ^ 18 ^ 2 ^ 15 ^ 4 = 31.​​​​​​​​​​​​​​

Constraints:

    1 <= n == nums.length <= 10^3
    1 <= nums[i] <= 10^9
    1 <= q == queries.length <= 10^3
    queries[i] = [li, ri, ki, vi]
    0 <= li <= ri < n
    1 <= ki <= n
    1 <= vi <= 10^5

算法一：暴力

暴力处理每个询问，把下标为 l,l+k,l+2k,… 的数都乘以 v。

最坏情况每次需要 O(n / k​) 的时间，整体 O(nq/ k​) 时间。其中 n 是 nums 的长度，q 是 queries 的长度。

特点：当 k 比较大时，算法比较快。

算法二：差分数组（商分数组）

前置知识：差分数组

如果 k=1，我们可以用差分数组（准确来说叫商分数组）记录询问，然后计算商分数组的前缀积，即可得到最终的数组。

商分数组 d 与差分数组的区别是，初始值每一项都是 1（乘法单位元）；记录询问时，d[l] 乘以 v，d[r+1] 除以 v，即乘以 v 的逆元。关于逆元，请看 模运算的世界：当加减乘除遇上取模。

对于其他 k 呢？

比如 k=3。我们可以把所有询问分为 k=3 组：

    作用在下标 0,3,6,… 上的询问。
    作用在下标 1,4,7,… 上的询问。
    作用在下标 2,5,8,… 上的询问。

比如 l=1，r=9，更新的下标是 1,4,7。在左端点 1 处乘以 v，右端点 7+k=10 处除以 v（乘以 v 的逆元）。这样我们计算 1,4,7,10,… 的前缀积，就可以正确地得到最终数组每一项要乘的数了。

这里的 7 是怎么算的？我们要找 ≤r 的最大的 3k+1，或者说，要把 r 减少多少。这个减少量等同于当 l=0，r=8 时，r 到 ≤r 的最近的 k 的倍数的距离，即 8modk=2。一般地，更新的最大下标是 r−(r−l)modk。再加上 k，得到要做商分标记的位置。

一般地，在左端点 l 处乘以 v，右端点 r−(r−l) mod k + k 处除以 v（乘以 v 的逆元）。

处理每个询问只需要 O(logM) 时间计算逆元，其中 M=10^9+7。然而，我们需要遍历 O(K) 个长为 O(n) 的商分数组，总体需要 $O(nK+qlogM)$ 的时间。其中 K 是 ki​ 的最大值。

特点：当 K 比较小时，算法比较快。

「平衡」两个算法

根据这两个算法的特点，我们可以规定一个阈值 B：

    对于 k≥B 的询问，使用算法一，即暴力计算。
    对于 k<B 的询问，使用算法二，即用商分数组记录询问。

总体时间复杂度为 $O(Bn/q​+nB+qlogM)$

根据基本不等式，当 B=q​ 时，上式取到最小值O(nq​+qlogM) 足以通过本题。

把懒初始化的想法进一步扩展。比如 k=3 时，没有遇到 lmodk=2 的组，那么这一组的商分数组全为 1，无需遍历。

用二维布尔数组记录询问是否有 (k, l mod k)。

```python
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        B = isqrt(len(queries))
        diff = [None] * B
        has = [None] * B

        for l, r, k, v in queries:
            if k < B:
                # 懒初始化
                if not diff[k]:
                    diff[k] = [1] * (n + k)
                    has[k] = [False] * k
                has[k][l % k] = True
                diff[k][l] = diff[k][l] * v % MOD
                r = r - (r - l) % k + k
                diff[k][r] = diff[k][r] * pow(v, -1, MOD) % MOD
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % MOD

        for k, d in enumerate(diff):
            if not d:
                continue
            for start, b in enumerate(has[k]):
                if not b:
                    continue
                mul_d = 1
                for i in range(start, n, k):
                    mul_d = mul_d * d[i] % MOD
                    nums[i] = nums[i] * mul_d % MOD

        return reduce(xor, nums)
```

复杂度分析

    时间复杂度：$O(n * sqrt(q) + q*logM)$，其中 n 是 nums 的长度，q 是 queries 的长度，M=10^9+7。
    空间复杂度：$O(n * sqrt(q))$。

写法二

把询问按照 (k,l mod k) 分组，对于每一组计算商分。这样空间复杂度更小。如果询问的前三项是一样的，就把这样的询问合并在一起。

```python
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1_000_000_007
        prod = defaultdict(lambda: 1)
        for l, r, k, v in queries:
            t = (l, r, k)
            prod[t] = prod[t] * v % MOD

        n = len(nums)
        B = isqrt(len(prod))
        groups = [[] for _ in range(B)]

        for (l, r, k), v in prod.items():
            if k < B:
                groups[k].append((l, r, v))
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % MOD

        for k, g in enumerate(groups):
            if not g:
                continue

            buckets = [[] for _ in range(k)]
            for t in g:
                buckets[t[0] % k].append(t)

            for start, bucket in enumerate(buckets):
                if not bucket:
                    continue
                if len(bucket) == 1:
                    # 只有一个询问，直接暴力
                    l, r, v = bucket[0]
                    for i in range(l, r + 1, k):
                        nums[i] = nums[i] * v % MOD
                    continue

                m = (n - start - 1) // k + 1
                diff = [1] * (m + 1)
                for l, r, v in bucket:
                    diff[l // k] = diff[l // k] * v % MOD
                    r = (r - start) // k + 1
                    diff[r] = diff[r] * pow(v, -1, MOD) % MOD

                mul_d = 1
                for i in range(m):
                    mul_d = mul_d * diff[i] % MOD
                    j = start + i * k
                    nums[j] = nums[j] * mul_d % MOD

        return reduce(xor, nums)
```

复杂度分析

    时间复杂度：$O(n * sqrt(q) ​+qlogM)$，其中 n 是 nums 的长度，q 是 queries 的长度，M=10^9+7。
    空间复杂度：$O(n + q)$。
