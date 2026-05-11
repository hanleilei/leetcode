# Maximum Number of Jumps to Reach the Last Index

[[dp]] [[segmenttree]]

You are given a 0-indexed array nums of n integers and an integer target.

You are initially positioned at index 0. In one step, you can jump from index i to any index j such that:

0 <= i < j < n
-target <= nums[j] - nums[i] <= target
Return the maximum number of jumps you can make to reach index n - 1.

If there is no way to reach index n - 1, return -1.

Example 1:

Input: nums = [1,3,6,4,1,2], target = 2
Output: 3
Explanation: To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:

- Jump from index 0 to index 1.
- Jump from index 1 to index 3.
- Jump from index 3 to index 5.

It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 3 jumps. Hence, the answer is 3.
Example 2:

Input: nums = [1,3,6,4,1,2], target = 3
Output: 5
Explanation: To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:

- Jump from index 0 to index 1.
- Jump from index 1 to index 2.
- Jump from index 2 to index 3.
- Jump from index 3 to index 4.
- Jump from index 4 to index 5.

It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 5 jumps. Hence, the answer is 5.
Example 3:

Input: nums = [1,3,6,4,1,2], target = 0
Output: -1
Explanation: It can be proven that there is no jumping sequence that goes from 0 to n - 1. Hence, the answer is -1.

Constraints:

2 <= nums.length == n <= 1000
-10^9 <= nums[i] <= 10^9
0 <= target <= 2 * 10^9

dp 自顶向下：

```python
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        @cache
        def dp(j: int) -> int:
            if j == 0:
                return 0
            res = -inf
            for i in range(j):
                if abs(nums[i] - nums[j]) <= target:
                    res = max(res, dp(i) + 1)
            return res
        
        res = dp(len(nums) - 1)
        return -1 if res < 0 else res
```

dp 自底向上：

```python
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp[j] 表示从某个起点跳到位置 j 的最大跳跃次数
        dp = [-inf] * n
        dp[0] = 0  # 起始位置不需要跳跃
        
        for j in range(1, n):
            for i in range(j):
                if abs(nums[i] - nums[j]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        ans = dp[n - 1]
        return -1 if ans < 0 else int(ans)
```

```python
# 完整的线段树模板见 https://leetcode.cn/circle/discuss/mOr1u6/
class SegmentTree:
    def __init__(self, n: int) -> None:
        self.t = [-inf] * (2 << (n - 1).bit_length())

    def update(self, node: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:  # 叶子
            self.t[node] = val
            return
        m = (l + r) // 2
        if i <= m:  # i 在左子树
            self.update(node * 2, l, m, i, val)
        else:  # i 在右子树
            self.update(node * 2 + 1, m + 1, r, i, val)
        self.t[node] = max(self.t[node * 2], self.t[node * 2 + 1])

    def query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:  # 当前子树完全在 [ql, qr] 内
            return self.t[node]
        m = (l + r) // 2
        if qr <= m:  # [ql, qr] 在左子树
            return self.query(node * 2, l, m, ql, qr)
        if ql > m:  # [ql, qr] 在右子树
            return self.query(node * 2 + 1, m + 1, r, ql, qr)
        return max(self.query(node * 2, l, m, ql, qr), self.query(node * 2 + 1, m + 1, r, ql, qr))


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # 去重排序，便于离散化
        sorted_nums = sorted(set(nums))

        n = len(nums)
        m = len(sorted_nums)
        t = SegmentTree(m)  # 值域线段树

        # nums[0] 对应的 f[0] = 0
        t.update(1, 0, m - 1, bisect_left(sorted_nums, nums[0]), 0)

        for j in range(1, n):
            l = bisect_left(sorted_nums, nums[j] - target)       # >= nums[j]-target 的第一个数
            r = bisect_right(sorted_nums, nums[j] + target) - 1  # <= nums[j]+target 的最后一个数
            # t.query 返回满足 nums[j]-target <= nums[i] <= nums[j]+target 的最大的 f[i]
            fj = t.query(1, 0, m - 1, l, r) + 1
            t.update(1, 0, m - 1, bisect_left(sorted_nums, nums[j]), fj)

        return -1 if fj < 0 else fj
```
