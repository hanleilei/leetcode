# Jump Game II

[[dp]]

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

```Comment
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

```python
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_max_reach, current_max_reach = 0 , 0
        njump , i = 0 , 0
        while current_max_reach < len(nums)-1:
            while i <= last_max_reach:
                current_max_reach = max(i+nums[i],current_max_reach)
                i+=1
            if last_max_reach == current_max_reach:
                return -1
            last_max_reach = current_max_reach
            njump+=1
        return njump
```

Explanation

The main idea is based on greedy. Let's say the range of the current jump is [curBegin, curEnd], curFarthest is the farthest point that all points in [curBegin, curEnd] can reach. Once the current point reaches curEnd, then trigger another jump, and set the new curEnd with curFarthest, then keep the above steps, as the following:

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, curEnd, curFarthest = 0, 0, 0

        for i in range(len(nums) - 1):
            curFarthest = max(curFarthest, i + nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = curFarthest
        return jumps
```
