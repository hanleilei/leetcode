# Longest Strictly Increasing or Strictly Decreasing Subarray

You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

## Example 1

```text
Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.
```

## Example 2

```text
Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.
```

## Example 3

```text
Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.
```

## Constraints

```text
1 <= nums.length <= 50
1 <= nums[i] <= 50
```

阅读理解，搓两次循环即可。

```python
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        t = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                t += 1
            else:
                t = 1
            res = max(res, t)   

        t = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                t += 1
            else:
                t = 1
            res = max(res, t)
        return res
```

```python
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length, inc, dec = 1, 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc, dec = 1, 1
            max_length = max(max_length, inc, dec)
        return max_length
```
