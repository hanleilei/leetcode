# Sum of All Subset XOR Totals

The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

Example 1:

```text
Input: nums = [1,3]
Output: 6
Explanation: The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6
```

Example 2:

```text
Input: nums = [5,1,6]
Output: 28
Explanation: The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
```

Example 3:

```text
Input: nums = [3,4,5,6,7,8]
Output: 480
Explanation: The sum of all XOR totals for every subset is 480.
```

Constraints:

1 <= nums.length <= 12
1 <= nums[i] <= 20

就是第78题目：subset 的变体，类似的还有：对所有子集求和

```python
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        stack = [([], 0)]
        while stack:
            path, index = stack.pop()
            xor_sum = 0
            for i in path:
                xor_sum ^= i
            res += xor_sum
            for i in range(index, len(nums)):
                stack.append((path + [nums[i]], i + 1))
        return res
```

```python
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans |= i
        return ans << (len(nums)-1)
```

```python
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (1 << n) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range((1 << n)):
                dp[i][j] = dp[i - 1][j]
                dp[i][j ^ nums[i - 1]] += dp[i - 1][j]

        return sum(dp[n][j] * j for j in range((1 << n)))
```

标准库，这个方法大多数时候怕是要超时的，不推荐。

```python
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums) + 1):
            for j in itertools.combinations(nums, i):
                xor_sum = 0
                for k in j:
                    xor_sum ^= k
                res += xor_sum 
        return res
```
