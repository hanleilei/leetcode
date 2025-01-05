# Largest Number At Least Twice of Others

You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

Constraints:

2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.

思路：

1. 找到最大数字和第二大数字
2. 如果第二大数字大于最大数字的两倍，返回最大数字的下标，否则返回-1

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        d = dict()
        for i, v in enumerate(nums):
            d[v] = i
        A = nlargest(2, nums)
        print(A)
        if A[1] * 2 <= A[0]:
            return d[A[0]]
        else:
            return -1
```

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        h = max(nums)
        for n in nums:
            if n != h and n * 2 > h:
                return -1
        return nums.index(h)
```
