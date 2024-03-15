# Running Sum of 1d Array

[[prefixSum]]

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

```text
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

Example 2:

```text
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
```

Example 3:

```text
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

Constraints:

```text
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
```

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res [i - 1] + nums[i]
        return res
```
