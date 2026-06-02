# Number of Unequal Triplets in Array

You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:

    0 <= i < j < k < nums.length
    nums[i], nums[j], and nums[k] are pairwise distinct.
        In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].

Return the number of triplets that meet the conditions.

Example 1:

Input: nums = [4,4,2,4,3]
Output: 3
Explanation: The following triplets meet the conditions:

- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.

Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: No triplets meet the conditions so we return 0.

Constraints:

    3 <= nums.length <= 100
    1 <= nums[i] <= 1000

由于元素的位置是不重要的，我们可以直接用哈希表统计，方法一中的 a b c 重定义为：

    在 x 之前遍历过的数有 a 个；
    （当前遍历的）等于 x 的数有 b 个；
    在 x 之后遍历过的数有 c 个。

```python
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res, a, c = 0, 0, len(nums)
        for _, b in Counter(nums).items():
            c -= b
            res += a * b * c
            a += b
        return res
```

对于 x，设：

    小于 x 的数有 a 个；
    等于 x 的数有 b 个；
    大于 x 的数有 c 个。

那么 x 对答案的贡献是 abc。

累加所有贡献，得到答案。

代码实现时，通过排序可以快速求出 a b c。

```python
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        nums.sort()
        res = start = 0
        for i, (x, y) in enumerate(pairwise(nums)):
            if x != y:
                res += start * (i - start + 1) * (len(nums) - 1 - i)
                start = i + 1
        return res
```
