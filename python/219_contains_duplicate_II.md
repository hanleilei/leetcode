# contains duplicate II

[[sliding_window]] [[hash_table]] [[array]]

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5

巧用enumerate和字典

前面加上一个判断，速度一下超过99%的提交用户，简直了。。

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or k<0 or len(nums)==len(set(nums)):
            return False

        d = dict()
        for m,  n in enumerate(nums):
            if n in d and m - d[n] <=k:
                return True
            d[n] = m
        return False
```

自制

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, 0
        window = dict()

        while right < len(nums):
            c = nums[right]
            right += 1

            if c in window:
                if right - window[c]<= k:
                    return True
            window[c] = right
        return False
```

来自labuladong

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        right = 0
        window = set()
        # 滑动窗口算法框架，维护一个大小为 k 的窗口
        while right < len(nums):
            # 扩大窗口
            if nums[right] in window:
                return True
            window.add(nums[right])
            right += 1

            if right - left > k:
                # 当窗口的大小大于 k 时，缩小窗口
                window.remove(nums[left])
                left += 1

        return False
```
