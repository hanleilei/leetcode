# Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

#### 我只想说，用了collections，解决这类问题，一次性代码写好就ok


```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        d = Counter(nums)
        for k in d.keys():
            if d[k]> len(nums) * 0.5:
                return k
```
