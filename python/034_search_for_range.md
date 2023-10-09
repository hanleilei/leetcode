# search for range

[[binary search]]

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

主要还是想清楚问题怎么解决， 这里用了collections里面的Counter库。或者二分法。

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [i for i, v in enumerate(nums) if v == target]
        if len(res) >0:
            return [res[0], res[-1]]
        else:
            return [-1, -1]
```

二分法：

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        res = [-1, -1]

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                res = [mid, mid]

                i = mid - 1
                while i >= 0 and nums[i] == target:
                    res[0] = i
                    i -= 1
                i = mid + 1
                while i < len(nums) and nums[i] == target:
                    res[1] = i
                    i += 1
                break
        return res
```

再来一个标准库的：

```python
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        if not nums:
            return [-1, -1]

        l = bisect.bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            l = -1
        r = bisect.bisect_right(nums, target) - 1
        if nums[r] != target:
            r = -1

        return [l, r]
```

最后再来一个速度最快的：

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, -1
        i = 0
        j = len(nums)-1
        flag = 0
        while i <= j:
            m = (i+j) // 2
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
            else:
                i = m + 1
                flag = 1
        right = i - 1

        i = 0
        j = right - 1

        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
            else:
                j = m - 1
                flag = 1
        left = j + 1
        return [left, right] if flag else [-1, -1]
```

再来一个很好理解的：

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 0:
            return [-1, -1]
        
        if nums[0] <= target and nums[-1] >= target:
            left, right = 0, size - 1
            while left <= right:
                mid = left + (right - left ) // 2
                if nums[mid] == target:
                    right = left = mid
                    while left - 1 >= 0 and nums[left-1] == target:
                        left -= 1
                    while right + 1 <= size - 1 and nums[right + 1] == target:
                        right += 1
                    return [left, right]
                elif num[mid] < target:
                    left = mid += 1
                else:
                    right = mid - 1
        return [-1, -1]
```
