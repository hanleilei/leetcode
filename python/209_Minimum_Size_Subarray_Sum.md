# Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

### Example:
```
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```
### Follow up:
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
看下lee215的方法, 非常巧妙:

```python
class Solution:
    def minSubArrayLen(self, s, A): # List[int]) -> int:
        i, res = 0, len(A) + 1
        for j in range(len(A)):
            s -= A[j]
            while s <= 0:
                res = min(res, j - i + 1)
                s += A[i]
                i += 1
        return res % (len(A) + 1)
```

我的方法, 有点low, 破坏了输入条件来避免数组越界:

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, right = 0, 0
        res = 0
        ans = float("inf")
        nums.append(0)
        
        while left <= right < len(nums):
            if res >= s:
                ans = min(ans, right - left)
                res -= nums[left]
                left += 1
                if left > right:
                    right += 1
            else:
                res += nums[right]
                right += 1

        return ans if ans < float("inf") else 0
```
