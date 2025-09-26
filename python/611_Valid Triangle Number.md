# Valid Triangle Number

[[2points]]

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:

Input: nums = [4,2,3,4]
Output: 4

Constraints:

- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000

第一个方法，同向双指针

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 3:
            return 0
        res = 0
        for k in range(2, len(nums)):
            left, right = 0, k - 1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    res += (right - left)
                    right -= 1
                else:
                    left += 1
        return res
```

可以实现两个优化：

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for k in range(len(nums) - 1, 1, -1):
            c = nums[k]
            if nums[0] + nums[1] > c:  # 优化一
                ans += (k + 1) * k * (k - 1) // 6
                break
            if nums[k - 2] + nums[k - 1] <= c:  # 优化二
                continue
            i = 0  # a=nums[i]
            j = k - 1  # b=nums[j]
            while i < j:
                if nums[i] + nums[j] > c:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans
```

第二个方法：枚举最短边 + 同向双指针

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = [i for i in nums if i > 0]
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            a = nums[i]
            j = i + 1
            for k in range(i + 2, n):
                while nums[k] - nums[j] >= a:
                    j += 1
                # 如果 a=nums[i] 和 c=nums[k] 固定不变
                # 那么 b 可以是 nums[j],nums[j+1],...,nums[k-1]，一共有 k-j 个
                ans += k - j
        return ans
```

