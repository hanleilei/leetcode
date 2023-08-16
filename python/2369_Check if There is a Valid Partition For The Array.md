# Check if There is a Valid Partition For The Array

You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.

Example 1:
```yaml
Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.
```

Example 2:
```yaml
Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.
```

Constraints:
```yaml
2 <= nums.length <= 105
1 <= nums[i] <= 106
```

```python
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False, False, False, True]
        for i in range(n):
            dp[i % 4] = False
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                dp[i % 4] = dp[(i - 2) % 4]
            if i - 2 >= 0 and nums[i] == nums[i-1] == nums[i-2]:
                dp[i % 4] |= dp[(i - 3) % 4]
            if i - 2 >= 0 and nums[i] == nums[i-1] + 1 == nums[i-2] + 2:
                dp[i % 4] |= dp[(i - 3) % 4]
        return dp[(n - 1) % 4]
```
