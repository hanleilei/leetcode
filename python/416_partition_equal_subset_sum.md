# Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

1. Each of the array element will not exceed 100.
2. The array size will not exceed 200.


Example 1:
```
Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

Example 2:
```
Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
```

dfs recursion + memo 版本：
```Python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(nums, target, cache):
            if target < 0: return False
            if target == 0: return True
            if target in cache: return False
            cache.add(target)
            for i, n in enumerate(nums):
                if dfs(nums[i+1:], target - n, cache): return True
            return False
        s = sum(nums)
        if s % 2 == 1: return False
        return dfs(nums, s // 2, set())

```


```Python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False

        target = total // 2   #target sum
        s = set([0])         #stores the sums of the subsets

        for n in nums:
            sums_with_n = []  #stores the sums of the subsets that contain n
            for i in s:
                if i + n == target: return True
                if i + n < target:
                    sums_with_n.append(i + n)
            s.update(sums_with_n)

        return False

```
