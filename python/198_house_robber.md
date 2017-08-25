# house robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.

这类最优化问题，第一反应就是用动态规划的方法


```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now

```

下面是看到的速度最快的方法：

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]

        dp_pre_pre = nums[0]
        dp_pre = max(nums[:2])

        for i in range(2,l):
            dp_pre_pre,dp_pre = dp_pre,max(dp_pre, dp_pre_pre+nums[i])

        return max(dp_pre_pre, dp_pre)
```

所有这些所谓的最快方法，就是放置一些判断条件，减少计算。然后剩下的就是运气了。。这也就是我运行这个所谓的最快的代码，永远达不到他那么少的时间。
