# Left and Right Sum Differences

You are given a 0-indexed integer array nums of size n.

Define two arrays leftSum and rightSum where:

    leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
    rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 10^5

类似的题目可以通过一次遍历来计算出 leftSum 和 rightSum 的值，并在同一遍历中计算出 answer 数组的值。首先计算出 nums 的总和，然后在遍历过程中逐步更新 leftSum 和 rightSum 的值，并计算出 answer[i] 的值。

```python
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        res = []
        left_sum = 0
        for i in range(len(nums)):
            total -= nums[i]
            res.append(abs(total - left_sum))
            left_sum += nums[i]
        return res
```
