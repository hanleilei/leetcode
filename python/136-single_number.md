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

但是上面的方法还是略慢，还是看下面的方法：

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res = res^num
        return res
```

这个使用^的方法还是有点不太容易想得到，但是用下面的字典就很容易：

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for i in nums:
            if i in d:
                d.pop(i)
            else:
                d[i] = 1
        return list(d.keys())[0]
```
