# longest increasing subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
```
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

先来一个自己实现的二分查找：

```python
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = int((low + high) / 2)
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[x])
            else:
                dp[low] = nums[x]
        return len(dp)
```

```python

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []
        def insert(target):
            left, right = 0, len(LIS) - 1
            # Find the first index "left" which satisfies LIS[left] >= target
            while left <= right:
                mid = left + int((right - left) / 2)
                if LIS[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # If not found, append the target.
            if left == len(LIS):
                LIS.append(target);
            else:
                LIS[left] = target

        for num in nums:
            insert(num)

        return len(LIS)
```

上标准库：

```python
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        stack = []
        for n in nums:
            if not stack or n > stack[-1]:
                stack.append(n)
            else:
                idx = bisect.bisect_left(stack, n)
                stack[idx] = n
        return len(stack)
```
或者：
```python
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        res = []
        for n in nums:
            index = bisect.bisect_left(res, n)
            if index == len(res):
                res.append(n)
            else:
                res[index] = n
        return len(res)
```
