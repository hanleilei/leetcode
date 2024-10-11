# Maximum Average Subarray I

[[sliding window]]

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

以下代码，可以作为滑动窗口模板使用：

- 初始化将滑动窗口压满，取得第一个滑动窗口的目标值
- 继续滑动窗口，每往前滑动一次，需要删除一个和添加一个元素

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = windows = sum(nums[:k])

        for i in range(len(nums) - k):
            windows = windows - nums[i] + nums[i+k]
            res = max(res, windows )
        return res / k
```
