# Greatest Sum Divisible by Three

Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).

Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4

```python

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        if s%3==0:
            return sum(nums)
        a1 = sorted(x for x in nums if x%3==1)
        a2 = sorted(x for x in nums if x%3==2)
        if s%3==2:
            a1, a2 = a2, a1
        res = s-a1[0] if a1 else 0
        if len(a2)>1:
            res = max(res, s-sum(a2[:2]))
        return res
```

```python
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for a in nums:
            for i in dp[:]:
                dp[(i+a)% 3] = max(dp[(i+a)%3], i + a)
        return dp[0]
```

7ms的极速冲锋：

```python
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = 0
        # 初始化变量：记录余1数的最小值和次小值，余2数的最小值和次小值
        min1_1 = float('inf')  # 最小余1数
        min1_2 = float('inf')  # 次小余1数
        min2_1 = float('inf')  # 最小余2数
        min2_2 = float('inf')  # 次小余2数

        # 一次遍历：计算总和，并更新余1/余2数的最小值
        for num in nums:
            s += num
            remainder = num % 3
            if remainder == 1:
                # 更新余1数的最小值和次小值
                if num < min1_1:
                    min1_2 = min1_1  # 原最小值变为次小值
                    min1_1 = num     # 更新最小值
                elif num < min1_2:
                    min1_2 = num     # 只更新次小值
            elif remainder == 2:
                # 更新余2数的最小值和次小值
                if num < min2_1:
                    min2_2 = min2_1
                    min2_1 = num
                elif num < min2_2:
                    min2_2 = num

        # 如果总和能被3整除，直接返回
        if s % 3 == 0:
            return s

        candidates = []  # 存储可能的候选总和（移除后余0的方案）

        if s % 3 == 1:
            # 方案1：移除1个最小的余1数（如果存在）
            if min1_1 != float('inf'):
                candidates.append(s - min1_1)
            # 方案2：移除2个最小的余2数（如果存在）
            if min2_1 != float('inf') and min2_2 != float('inf'):
                candidates.append(s - min2_1 - min2_2)
        elif s % 3 == 2:
            # 方案1：移除1个最小的余2数（如果存在）
            if min2_1 != float('inf'):
                candidates.append(s - min2_1)
            # 方案2：移除2个最小的余1数（如果存在）
            if min1_1 != float('inf') and min1_2 != float('inf'):
                candidates.append(s - min1_1 - min1_2)

        # 如果有有效方案，返回最大值；否则返回0（表示无法调整）
        return max(candidates) if candidates else 0
```
