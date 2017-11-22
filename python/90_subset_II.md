# subset II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

还是照旧用itertools的combination方法实现。注意一开始对于输入数组排序是关键。。。

```Python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import combinations

        t =list()
        t.append([])
        nums.sort()
        for n in range(len(nums)):
            for i in combinations(nums, n+1):
                if list(i) not in t:
                    t.append(list(i))
        return t
```
