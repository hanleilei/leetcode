# Single number

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

###### 想下算法复杂度，还是不要用大量的数值比较，那样肯定挂掉。。。直接上字典最棒棒了。。

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        d = dict()
        for k, v in c.items():
            d[v] = k

        return d[1]

```
