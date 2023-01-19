# Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

Hint:

How many majority elements could it possibly have?

#### 无他，和第一版没差别，就是返回一个列表

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        d = Counter(nums)
        l = []
        for k in d.keys():
            if d[k]> len(nums) / 3:
                l.append(k)
        return l
```
