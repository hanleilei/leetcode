# missing number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

#### 方法很多种，可以使用集合的方式，不过看网友的方式更简单，直接对于列表求和

```python
# 集合的方式 not passed in website: reported: type set error
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == max(nums) - min(nums) + 1:
            return nums[-1] +1
        else:
            return set([i for i in range(min(nums),max(nums)+1)]) - set(nums)

```
#### 用列表求和的方式
```python
# I make it done, got idea from others
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == max(nums) - min(nums) + 1:
            if min(nums) > 0:
                return min(nums) -1            
            else:
                return max(nums) + 1
        else:
            return sum([i for i in range(min(nums),max(nums)+1)]) - sum(nums)
```
