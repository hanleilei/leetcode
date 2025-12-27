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

不推荐这样做：

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

标准库很多时候还是要少用，下面看一下这个方法：

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []

        nums.sort()
        def backtrack(i):
            result.append(temp[:])

            for j in range(i,len(nums)):

                temp.append(nums[j])
                backtrack(j+1)
                temp.pop()

        backtrack(0)
        return result
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
