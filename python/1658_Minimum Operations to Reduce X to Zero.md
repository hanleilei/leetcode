# Minimum Operations to Reduce X to Zero

[[slidingWindow]] [[prefixSum]]

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

## Example 1

```text
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
```

## Example 2

```text
Input: nums = [5,6,7,8,9], x = 4
Output: -1
```

## Example 3

```text
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
```

## Constraints

- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 104`
- `1 <= x <= 109`

典型的sliding windows问题

首先，不管怎么选取，最终结果就是`sum(nums) - x`作为最后留下的切片之和target。所以这就将问题变成：求满足target的最大切片的数量。

再转换一下思路：是不是前缀和更合适呢？

```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        valid, res = 0, float('-inf')
        left, right = 0, 0

        while right < len(nums):
            valid += nums[right]
            right += 1
            while left < right and valid > target:
                valid -= nums[left]
                left += 1
            if valid == target:
                res = max(res, right - left)


        return len(nums) - res if res != float('-inf') else -1
```

下面是我肝了一个小时才搞定的前缀和+dict的方法，有点被恶心到了。

```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        prefix = dict()
        prefix[nums[0]] = 0
        ans = float('-inf')
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
            prefix[nums[i]] = i
        if target in prefix:
            ans = prefix[target] + 1  # 这个+1也是个细节
        if nums[-1] < x: # 排除边界条件，如果前缀和的最大元素比x还要小，那么没必要计算了。
            return -1

        for right in range(len(prefix)):
            if nums[right] - target in prefix:
                ans = max(ans, right - prefix[nums[right] - target]) # 这里要不要+1 呢？显然不需要

        return -1 if ans == float('-inf') else  len(nums) - ans
```

细节有点多，搅合在一起，思路要理顺，大的方向知道，但是细节抠起来就有点麻烦了，都是套路。。会想一下自己上次写前缀和是什么时候了？
