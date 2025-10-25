# Contiguous Array

[[prefixSum]]

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

一句话思路：把 0 看成 −1，计算和为 0 的最长子数组。

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # [ 0,1,1,1,1,1,0,0,0]
        # [-1,0,1,2,3,4,3,2,1]
        h = {0: -1}
        presum = 0
        maxval = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                presum -= 1
            else:
                presum += 1
            
            if presum not in h:
                h[presum] = i
            else:
                if i - h[presum] > maxval:
                    maxval = i - h[presum]
        return maxval
```

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 把 0 当作 -1
        nums = [1 if x else -1 for x in nums]

        # 计算 nums 的前缀和
        s = list(accumulate(nums, initial=0))

        pos = {}
        ans = 0
        for i, x in enumerate(s):
            if x in pos:
                # 找到一对相等元素，下标分别为 pos[x] 和 i，距离为 i - pos[x]
                ans = max(ans, i - pos[x])
            else:
                pos[x] = i
        return ans
```

优化一下：

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 前缀和数组的首项 0 相当于在 -1 下标
        pos = {0: -1}
        ans = s = 0
        for i, x in enumerate(nums):
            s += 1 if x else -1
            if s in pos:
                ans = max(ans, i - pos[s])
            else:
                pos[s] = i
        return ans
```
