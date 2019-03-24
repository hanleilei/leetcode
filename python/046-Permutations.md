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

上面的这个标准库，很不合适，还是需要用backtrack的方法：

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            # e.g., [1, 2, 3]: 3! = 6 cases
            # idx -> nums, path
            # 0 -> [2, 3], [1] -> 0: [3], [1, 2] -> [], [1, 2, 3]
            #                  -> 1: [2], [1, 3] -> [], [1, 3, 2]
            #
            # 1 -> [1, 3], [2] -> 0: [3], [2, 1] -> [], [2, 1, 3]
            #                  -> 1: [1], [2, 3] -> [], [2, 3, 1]
            #
            # 2 -> [1, 2], [3] -> 0: [2], [3, 1] -> [], [3, 1, 2]
            #                  -> 1: [1], [3, 2] -> [], [3, 2, 1]
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
```
或者
```python
class Solution:
    def permute(self, nums:
        def backtracking(nums,res,cur):
            if len(nums) == 1:
                cur.append(nums[0])
                res.append(cur)
            else:
                for i in range(len(nums)):
                    backtracking(nums[:i]+nums[i+1:],res,cur+[nums[i]])
        res = []
        backtracking(nums,res,[])
        return res
```
