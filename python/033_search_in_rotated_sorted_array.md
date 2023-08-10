# search in rotated sorted array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

不要用语言自带的库来解决，这个就是用二分法实现的，还是来个实在的：

```python
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if target in nums[lo:lo+1] else -1
```

这个异或用的实在是屌。。

再来个好理解的：

```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) -1
        
        while low <= high:
            mid = (high + low) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
```

再来一个九章课程上的使用模板的方法：

```Python
class Solution:
    def search(self, A, target):
        if len(A) == 0:
            return -1
        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid


        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
```
