# search insert position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

### 就是 binary search 的变体，注意最后一个 return left。

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid]  > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid +1
            else:
                return mid
        return left
```

或者可以直接用 Python 中的 bisect 模块实现：

```Python
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        from bisect import bisect
        index = bisect(nums, target)
        if nums[index-1] == target:
            return index -1
        else:
            return index
```

下面是几种据说速度也非常快的，大同小异，基本上都是用 binary search。不过 leetcode 的 OJ 略抽风：

```Python
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (j - i) // 2 + i
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return i if nums[i] > target else i + 1
```
