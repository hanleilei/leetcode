# 016 3 sum closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Subscribe to see which companies asked this question

思路与3Sum基本相同，现在要额外维护一个表示之前三元组中与目标值的差最小值的变量，这个变量的初始化值应该很大，防止把有意义的三元组直接排除了。此外，由于题目中明确说只有唯一的一组最优解，所有不用考虑重复数字了。

```python
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i = 0
        result = 0
        distance = pow(2, 32) - 1
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1

            while j < k:
                l = [nums[i], nums[j], nums[k]]
                s = sum(l)
                if s == target:
                    return target
                if abs(s - target) < distance:
                    result = s
                    distance = abs(s - target)
                elif s > target:
                    k-= 1
                else:
                    j += 1
        return result
```
