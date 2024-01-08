# Arithmetic Slices II - Subsequence

Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

## Example 1

```text
Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
```

## Example 2

```text
Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.
```

## Constraints

```text
1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
```

来个速度快的：

```python
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        unused = Counter(nums)
        wait = defaultdict(Counter)
        used = Counter()
        total = 0
        for i, n in enumerate(nums):
            if n in wait:
                total += wait[n].total()
                for d in wait[n]:
                    if unused[n+d]:
                        wait[n+d][d] += wait[n][d]
            for m in used:
                d = n-m
                if n+d in unused and unused[n+d]:
                    wait[n+d][d] += used[m]
            used[n] += 1
            unused[n] -= 1
        return total
```

## Idea

Let `dp[i][d]` denotes the number of subsequences (have at least 2 numbers) that ends with nums[i] and its common difference is d.
For i in [1..n-1]
For j in [0..i-1]:
diff = nums[i] - nums[j]
`dp[i][diff] += dp[j][diff] + 1`
`ans += dp[j][diff] // We += dp[j][diff]` because it's the number of valid subsequences (have >= 3 elements). But `dp[i][diff]` is the number of valid subsequences (have >= 2 elements).

![1](https://assets.leetcode.com/users/images/603b70a0-196a-4ce6-bc89-28dfb3adc472_1631342659.9692721.png)

```python
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]

        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = 0
                if diff in dp[j]:
                    count = dp[j][diff]
                dp[i][diff] += count + 1
                ans += count
        return ans
```
