# combination sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:
```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```
Example 2:
```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```


```Python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.res = list()
        candidates = [i for i in candidates if i <= target]
        candidates.sort()
        self.dfs(candidates, target, 0, list())
        return Solution.res

    def dfs(self, cand, target, start, res):
        length = len(cand)
        if target == 0 and res not in Solution.res:
            return Solution.res.append(res)
        for i in range(start, length):
            if target < cand[i]:
                return
            self.dfs(cand, target-cand[i], i+1,  res + [cand[i]])


```
