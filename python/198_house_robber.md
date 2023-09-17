# house robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Example 1

```text
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

## Example 2

```text
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

## Constraints

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

这类最优化问题，第一反应就是用动态规划的方法：

一般来说，给定一个规则，让我们求任意状态下的解，都是用动态规划。这里的规则是劫匪不能同时抢劫相邻的屋子，即我们在累加时，只有两种选择：

1. 如果选择了抢劫上一个屋子，那么就不能抢劫当前的屋子，所以最大收益就是抢劫上一个屋子的收益。
2. 如果选择抢劫当前屋子，就不能抢劫上一个屋子，所以最大收益是到上一个屋子的上一个屋子为止的最大收益，加上当前屋子里有的钱。

所以，我们只要判断一下两个里面哪个大就行了，同时也是我们的递推式。另外我们可以做一点优化，本来我们是要用一个dp数组来保存之前的结果的。但实际上我们只需要上一次和上上次的结果，所以可以用两个变量就行了。

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
            dp_pre_pre, dp_pre = dp_pre,max(dp_pre, dp_pre_pre+nums[i])

        return max(dp_pre_pre, dp_pre)
```

所有这些所谓的最快方法，就是放置一些判断条件，减少计算。然后剩下的就是运气了。。这也就是我运行这个所谓的最快的代码，永远达不到他那么少的时间。
