# Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

## Example

```text
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```

### Follow up

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

套用九章的模版，算法复杂度为O(n)，思路一下就很清晰了：

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums == []:
            return 0
        size = len(nums)
        j = 1
        res = float('inf')
        total = nums[0]

        for i in range(size):
            while j < size and total < s:
                total += nums[j]
                j += 1
            if total >= s:
                res = min(res, j - i)
            total -= nums[i]

        return res if res != float('inf') else 0
```

再来一个O(n)的方案：

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0
```

灵神的写法：

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        s = 0
        left = 0
        for right, x in enumerate(nums):
            s += x
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                ans = min(ans, right - left + 1)
        return ans if ans <= n else 0
```

时隔多年，再来自己手搓的一个滑动窗口的标准写法：

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        total = 0
        res = float('inf')
        while right < len(nums):
            c = nums[right]
            right += 1
            total += c

            while total >= target and left < right:
                res = min(res, right - left)
                d = nums[left]
                left += 1
                total -= d
        return res if res != float('inf') else 0
```
