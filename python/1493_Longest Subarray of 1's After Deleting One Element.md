# Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

解释：

1. prev表示之前的连续1的个数
2. current表示当前的连续1的个数
3. res表示结果，记录最长的连续1的个数
4. 如果整个数组都是1，则需要删除一个1，所以返回res-1
5. 这里的思路巧妙在如果连续的0，则prev也会因为之前current变为0而更新为0.

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev, current, res = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                if current + prev > res:
                    res = current + prev
            else:
                prev = current
                current = 0
        return res if len(nums) > res else res - 1
```
