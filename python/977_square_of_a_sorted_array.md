## square of a sorted array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

Example 2:

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

Constraints:

```
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
```

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

直接上一个 O(N)的方法：

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [0] * size
        i= 0
        j = size - 1
        for k in range(j, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i] * nums[i]
                i += 1
            else:
                res[k]  = nums[j] * nums[j]
                j -= 1
        return res
```

思路其实很简单，建立一个同样长度的数组，然后每个数组填充合适的值，每个值用双指针找到绝对值大的那个，直接一次扫描全部搞定。
