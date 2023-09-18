# Permutations

[[dfs]] [[backtrack]]

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

```text
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

Subscribe to see which companies asked this question

## 方法

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
    def permute(self, nums):
        def backtracking(nums, res, cur):
            if len(nums) == 1:
                cur.append(nums[0])
                res.append(cur)
            else:
                for i in range(len(nums)):
                    backtracking(nums[:i]+nums[i+1:],res,cur+[nums[i]])
        res = []
        backtracking(nums, res, [])
        return res
```

或者带上swap，这也是最快的方法，不用每次在一个列表中遍历。

```python
class Solution:
    def backtrack(self, nums, ind, result):        
        def swap(a,b):
            nums[a],nums[b]=nums[b],nums[a]
            
        if ind==len(nums)-1:
            result.append(nums[:])
            return
        
        for i in range(ind,len(nums)):
            swap(ind, i)
            self.backtrack(nums, ind+1, result)
            swap(i,ind)
            
    def permute(self, nums: List[int]) -> List[List[int]]: 
        result=[]
        self.backtrack(nums, 0, result)
        return result
```

再来一个, 这个方法非常之巧妙

```Python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        result = []
        self.dfs(nums, res, result)
        return result

    def dfs(self, nums, res, result):
        if len(res) == len(nums):
            result.append([i for i in res])
            return
        for num in nums:
            if num not in res:
                res.append(num)
                self.dfs(nums, res, result)
                res.pop()

```

和上面的巧妙方法类似，labuladong的模板方法：

```python
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 记录「路径」
        track = []
        # 「路径」中的元素会被标记为 true，避免重复使用
        used = [False] * len(nums)
        
        self.backtrack(nums, track, used)
        return self.res

    # 路径：记录在 track 中
    # 选择列表：nums 中不存在于 track 的那些元素（used[i] 为 false）
    # 结束条件：nums 中的元素全都在 track 中出现
    def backtrack(self, nums: List[int], track: List[int], used: List[bool]):
        # 触发结束条件
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        
        for i in range(len(nums)):
            # 排除不合法的选择
            if used[i]: 
                # nums[i] 已经在 track 中，跳过
                continue
            # 做选择
            track.append(nums[i])
            used[i] = True
            # 进入下一层决策树
            self.backtrack(nums, track, used)
            # 取消选择
            track.pop()
            used[i] = False
```

上面的算法复杂度很高O(N**2 * N!)

这个方法不是最快的，但是是最容易理解的。
