# combination sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

```text
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

```text
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

```Python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()                      
        result = []
        self.dfs(candidates, 0, [], result, target)
        return result

    def dfs(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider
        # it as a solution, and stop there
        if not target:
            result.append(path)
            return

        for i in range(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want
            # to count the first element in this recursive step even if it is the same
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.dfs(nums, i + 1, path + [nums[i]],
                               result, target - nums[i])
```

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]):
            # Base case: if target is 0, we've found a valid combination
            if target == 0:
                res.append(path[:])  # Add a copy of the current path to results
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # If current candidate is greater than target, no need to continue
                # (since candidates are sorted)
                if candidates[i] > target:
                    break
                
                # Include current candidate in the path
                path.append(candidates[i])
                
                # Recursively backtrack with updated target and start index
                backtrack(i + 1, target - candidates[i], path)
                
                # Backtrack: remove the current candidate to try next option
                path.pop()

        # Sort candidates to handle duplicates and enable early termination
        candidates = [i for i in candidates if i <= target]
        candidates.sort()
        
        # Initialize result list
        res = []
        
        # Start backtracking from index 0, with full target and empty path
        backtrack(0, target, [])
        
        return res
```
