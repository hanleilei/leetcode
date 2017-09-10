# Longest continuous increasing subsequence

Given an unsorted array of integers, find the length of longest continuous increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000

很简单的一个动态规划思想，扫描一次就可以了。

```python
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        max_len = 1
        max_length = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                max_len += 1
            else:
                max_len = 1
            max_length = max(max_len, max_length)
        return max_length
```
