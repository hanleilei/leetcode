# Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:
```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```
Example 2:
```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

```Python
class Solution(object):
    def combinationSum(self, candidates, target):
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
        if target == 0:
            return Solution.res.append(res)
        for i in range(start, length):
            if target < cand[i]:
                return
            self.dfs(cand, target-cand[i], i,  res + [cand[i]])

```

再来一个速度快的：

```Python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return

            for item in candidates:
                if item > remain: break
                if stack and item < stack[-1]: continue
                else:
                    dfs(remain - item, stack + [item])

        dfs(target, [])
        return result
```
