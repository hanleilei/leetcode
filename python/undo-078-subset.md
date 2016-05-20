# subset

Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:
```
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

###### 下面是我用的很pythonic的方法，但是很可惜，答案不认，原因是我把生成的子列表中元素顺序改变了。
```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import combinations
        lst = list()
        for i in range(len(nums)+1):
            lst += [list(j) for j in combinations(nums, i)]
        return lst
```
