# Maximum Score of a Good Subarray

[[MonotonicStack]]

You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

## Example 1

```text
Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 
```

## Example 2

```text
Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
```

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length

## Explanation
We start with i = j = k, the score = A[k].
When increment the size of window,
we want to reduce the min(A[i]..A[j]) slowly.

To do this, we can check the values on both sides of the window.
If A[i - 1] < A[j + 1], we do j = j + 1
If A[i - 1] >= A[j + 1], we do i = i - 1

During this process,
there is sense that we reduce min(A[i]..A[j]) step by step.

```python
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = mini = nums[k]
        i, j, n = k, k, len(nums)
        while i > 0 or j < n - 1:
            if (nums[i - 1] if i else 0) < (nums[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            mini = min(mini, nums[i], nums[j])
            res = max(res, mini * ( j - i + 1))
        return res
        
```