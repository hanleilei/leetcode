# Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
###### 方法：
注意使用什么样子的方式去除重复的元素

```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations

        d = dict()
        for i in permutations(nums,len(nums)):
            d[i]=1
        return d.keys()
```
