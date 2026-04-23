# Minimum Absolute Distance Between Mirror Pairs

You are given an integer array nums.

A mirror pair is a pair of indices (i, j) such that:

    0 <= i < j < nums.length, and
    reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed by reversing the digits of x. Leading zeros are omitted after reversing, for example reverse(120) = 21.

Return the minimum absolute distance between the indices of any mirror pair. The absolute distance between indices i and j is abs(i - j).

If no mirror pair exists, return -1.

Example 1:

Input: nums = [12,21,45,33,54]

Output: 1

Explanation:

The mirror pairs are:

    (0, 1) since reverse(nums[0]) = reverse(12) = 21 = nums[1], giving an absolute distance abs(0 - 1) = 1.
    (2, 4) since reverse(nums[2]) = reverse(45) = 54 = nums[4], giving an absolute distance abs(2 - 4) = 2.

The minimum absolute distance among all pairs is 1.

Example 2:

Input: nums = [120,21]

Output: 1

Explanation:

There is only one mirror pair (0, 1) since reverse(nums[0]) = reverse(120) = 21 = nums[1].

The minimum absolute distance is 1.

Example 3:

Input: nums = [21,120]

Output: -1

Explanation:

There are no mirror pairs in the array.

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9​​​​​​​

枚举 j，同时用哈希表维护 j 左边的 reverse(nums[i]) 的最大下标，哈希表的 key 是 reverse(nums[i])，value 是下标 i。

如果哈希表中有 nums[j]，获取对应的下标 i，用 j−i 更新答案的最小值。

⚠注意：请仔细读题，题目要求的是 reverse(nums[i]) == nums[j]，不是 reverse(nums[j]) == nums[i]，下标必须满足 i<j，不是对称的。

```python
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_index = {}
        res = inf

        for i, v in enumerate(nums):
            if v in last_index:
                res = min(res, i - last_index[v])
            v = int(str(v)[::-1])
            last_index[v] = i
        return res if res < inf else -1
```
