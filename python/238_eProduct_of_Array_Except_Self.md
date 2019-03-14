# Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

### Example:
```
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
```
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

完全是思路问题，直接看注释，很直白。

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        {              1,         a[0],    a[0]*a[1],    a[0]*a[1]*a[2],  }
        { a[1]*a[2]*a[3],    a[2]*a[3],         a[3],                 1,  }
        """
        length = len(nums)
        pivot = 1
        ans = list()
        for i in range(length):
            ans.append(pivot)
            pivot = nums[i] * pivot
        pivot = 1

        for j in range(length-1, -1, -1):
            ans[j] = ans[j] * pivot
            pivot = nums[j] * pivot
        return ans

```
