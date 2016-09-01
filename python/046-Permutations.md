# Permutations

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Subscribe to see which companies asked this question

###### 方法
直接用itertools里面的方法迭代，注意生成的是元祖，需要转换成列表

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations

        lt = list()
        for i in permutations(nums,len(nums)):
            lt.append(list(i))
        return lt



```
