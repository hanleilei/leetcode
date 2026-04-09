# Split Array Largest Sum

[[dp]] [[binarysearch]]

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= k <= min(50, nums.length)

```python
class Solution:
    def splitArray(self, nums: List[int], days: int) -> int:
        left = 0
        right = 1
        for w in nums:
            left = max(left, w)
            right += w

        while left < right:
            mid = left + (right - left) // 2
            if self.f(nums, mid) <= days:
                right = mid
            else:
                left = mid + 1

        return left

    # 定义：当运载能力为 x 时，需要 f(x) 天运完所有货物
    # f(x) 随着 x 的增加单调递减
    def f(self, weights: List[int], x: int) -> int:
        days = 0
        i = 0
        while i < len(weights):
            # 尽可能多装货物
            cap = x
            while i < len(weights):
                if cap < weights[i]:
                    break
                else:
                    cap -= weights[i]
                    i += 1
            days += 1
        return days
```

「元素和的最大值」越小，需要划分出的段数就越多；「元素和的最大值」越大，需要划分出的段数就越少。例如示例 1 的 nums=[7,2,5,10,8]，在最大和为 15 时，至少要划分 3 段，比如 [7,2,5],[10],[8]。而在最大和为 18 时，只需要划分 2 段，比如 [7,2,5],[10,8]。

套路：如果发现答案越小，越不能（能）满足要求；答案越大，越能（不能）满足要求，就可以尝试二分答案。

把二分中点 mid 记作 mx，我们可以贪心地计算要划分出的段数：

1. 初始化段数 cnt=1（第一段），当前这一段的元素和 s=0。
2. 遍历 nums。
3. 如果 s+nums[i]≤mx，则把 nums[i] 加到 s 中。否则我们必须新划分出一段，把 cnt 加一，s 替换成 nums[i]。如果在 cnt 加一之前有 cnt=k，则说明我们划分了超过 k 段，返回 false，表示不满足要求。
4. 遍历结束，返回 true，表示满足要求。

```python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mx: int) -> bool:
            cnt = 1
            s = 0
            for x in nums:
                if s + x <= mx:
                    s += x
                    continue
                if cnt == k:  # 不能继续划分
                    return False
                cnt += 1  # 新划分一段
                s = x
            return True

        left = max(nums) - 1
        right = sum(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right
```
