# subset

[[dfs]] [[backtracking]]

Given an integer array nums of unique elements, return all possible

(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.

下面看一下这个backtrack方法：

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        # 枚举选哪个：在下标 i 到 n-1 中选一个数，加到 path 末尾
        def backtrack(i: int) -> None:
            ans.append(path.copy())  # 不选，把当前子集加入答案
            for j in range(i, n):  # 选，枚举选择的数字
                path.append(nums[j])
                backtrack(j + 1)  # 选 nums[j] 意味着 i 到 j-1 都跳过不选，下一个数从 j+1 开始选
                path.pop()  # 恢复现场

        backtrack(0)
        return ans
```

再来看看caikehe的方法：

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
```

把上面的代码转换成迭代的形式：

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        stack = [([], 0)]
        while stack:
            path, index = stack.pop()
            res.append(path)
            for i in range(index, len(nums)):
                stack.append((path + [nums[i]], i + 1))
        return res
```

感觉caikehe同学把这些的dfs，bfs的套路总结的很到位，不管什么样的问题，一把梭。

再来一个迭代的方法，还是caikehe同学的：

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]
        for num in nums:
            sol += [curr + [num] for curr in sol]
        return sol
```

这个是DFS的模板代码：

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = list()
        if nums == None:
            return self.res
        self.dfs(self.res, nums, list(), 0)
        return self.res

    def dfs(self, res, nums, lt, index):
        if index == len(nums):
            res.append(lt.copy())
            return

        # 不选当前元素
        self.dfs(res, nums, lt, index + 1)
        # 选当前元素
        lt.append(nums[index])
        self.dfs(res, nums, lt, index + 1)

        # restore state 回溯
        lt.pop()
```

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for n in nums:
            newset = []
            for s in subset:
                ns = s + [n]
                newset.append(ns)
            subset.extend(newset)
        return subset
```
