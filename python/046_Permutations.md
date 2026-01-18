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
        return list(permutations(nums,len(nums)))
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
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 记录所有全排列
        res = []
        # 记录当前正在穷举的排列
        track = []

        # track 中的元素会被标记为 true，避免重复使用
        used = [False] * len(nums)

        # 主函数，输入一组不重复的数字，返回它们的全排列
        def backtrack(nums):
            # 到达叶子节点，track 中的元素就是一个全排列
            if len(track) == len(nums):
                res.append(track[:])
                return

            for i in range(len(nums)):
                # 排除不合法的选择
                if used[i]:
                    # nums[i] 已经在 track 中，跳过
                    continue
                # 做选择
                track.append(nums[i])
                used[i] = True

                # 进入递归树的下一层
                backtrack(nums)

                # 取消选择
                track.pop()
                used[i] = False

        backtrack(nums)
        return res
```

上面的算法复杂度很高O(N**2 * N!)

这个方法不是最快的，但是是最容易理解的。

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0] * n  # 所有排列的长度都是一样的 n
        on_path = [False] * n
        ans = []

        # 枚举 path[i] 填 nums 的哪个数
        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())  # 也可以写 path[:]
                return
            for j, on in enumerate(on_path):
                if not on:
                    path[i] = nums[j]  # 从没有选的数字中选一个
                    on_path[j] = True  # 已选上
                    dfs(i + 1)
                    on_path[j] = False  # 恢复现场
                    # 注意 path 无需恢复现场，因为排列长度固定，直接覆盖就行

        dfs(0)
        return ans
```
