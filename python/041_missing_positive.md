# missing positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

还是用哪个经典的替换方法来实现。简单，但是好慢。。

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

再来一个讨论群用 cpp 写，点赞最多的：

```python
class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        for i in range(len(nums)):
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1 # key point
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
```

再来一个速度不但快，而且是最简单的：

```python
class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        n=1
        nums = set(nums)
        while n in nums:
            n=n+1
        return n
```

感觉自己的智商被碾压了。。
