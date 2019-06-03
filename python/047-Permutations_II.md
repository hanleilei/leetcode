# Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
###### 方法：
注意使用什么样子的方式去除重复的元素

```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations

        d = dict()
        for i in permutations(nums,len(nums)):
            d[i]=1
        return d.keys()
```

标准库的算法，还是不要秀了：

```Python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.helper(nums, [])
        return self.result

    def helper(self, nums, temp):
        #print nums, temp, self.result
        if len(nums) == 0:
            self.result.append(temp)
            return
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                self.helper(nums[:i] + nums[i + 1:], temp + [nums[i]])
```

不用递归的方法：

```Python
class Solution:
    def permuteUnique(self, num: List[int]) -> List[List[int]]:
        if not num:
            return []
        num.sort()
        ret = [[]]
        for n in num:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):
                    if i < l and seq[i] == n:
                        break
                    new_ret.append(seq[:i] + [n] + seq[i:])
            ret = new_ret
        return ret
```

再来一个速度超级快的算法：

```Python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i < len(l) and l[i] == n:
                        break
            ans = new_ans
        return ans
```
