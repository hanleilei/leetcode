# missing positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

#### 还是用哪个经典的替换方法来实现。

```python
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [i for i in nums if i > 0]
        if nums == []:
            return 1

        a = [0] * (max(nums)+2)
        for i in nums:
            a[i-1] = i
        for i in range(len(a)):
            if a[i] == 0:
                return i+1
```
