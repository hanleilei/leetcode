# Find Minimum in Rotated Sorted Array II

[[binarysearch]]

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.

Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

本题与 153 题的区别是有相同元素，这会导致在二分查找时，可能会遇到恰好二分元素 nums[mid] 与数组末尾元素 nums[n−1] 相同的情况，此时无法确定答案在左半区间中还是右半区间中。

既然无法确定最小值所在区间，那么干脆去掉 nums 的最后一个数，继续二分。换句话说，此时问题变成了一个规模为 n−1 的子问题。

你可能会有疑问：这会不会碰巧去掉了最小值？

这是不会的：

如果去掉的数是最小值，那么 `nums[mid]` 也是最小值，这说明最小值仍然在数组中。
如果去掉的数不是最小值，那么我们排除了一个错误答案。
为了方便写代码，我们可以把 `right` 当作「数组最后一个数的下标」：

如果 `nums[mid]=nums[right]`，那么和上面一样，去掉 `nums[right]`，也就是把 `right` 减一。
如果 `nums[mid]<nums[right]`，那么下标大于 `mid` 的数都在最小值的右边，都可以去掉，也就是把 `right` 更新为 `mid`。
如果 `nums[mid]>nums[right]`，和 153 题一样，把 `left` 更新为 `mid`。

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = -1, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        return nums[right]
```

或者：

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1
        return nums[l]
```
