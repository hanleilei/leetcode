## Largest Perimeter Triangle

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:

```
Input: nums = [2,1,2]
Output: 5
```

Example 2:

```
Input: nums = [1,2,1]
Output: 0
```

Constraints:

```
3 <= nums.length <= 104
1 <= nums[i] <= 106
```

好简单的动态规划。。

```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                res = max(res, nums[i] + nums[i + 1] + nums[i + 2])
        return res
```

据说很快，但是实际上稍微快那么一点点：

```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        for i in range(len(nums) - 2):
            a = nums[i+2]
            b = nums[i+1]
            c = nums[i]
            if a + b > c:
                return a + b + c
        return 0
```
