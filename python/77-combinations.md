# combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

###### 枚举数组里面的内容，还是要用标准库

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from itertools import combinations

        # def combinations(iterable, r):
        #     pool = list(iterable)
        #     n = len(pool)
        #     for indices in permutations(range(n), r):
        #         if sorted(indices) == list(indices):
        #             yield list(pool[i] for i in indices)
        return [list(i) for i in combinations([j for j in range(1,n+1)],k)]
```
