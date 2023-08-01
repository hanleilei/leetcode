# combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

枚举数组里面的内容，还是要用标准库， 用时170ms，超过100%的人。。

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        return list(combinations(list(range(1, n+1)), k))
```

如果用backtrack的方法：

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backTracking(curr_lst, first_num):
            if len(curr_lst) == k:
                res.append(curr_lst.copy())
                return
            
            need = k - len(curr_lst)
            remain = n - first_num + 1
            available = remain - need
            #first_num 代表当前所看的数
            for num in range(first_num, first_num+available+ 1):
                curr_lst.append(num)
                #回溯时候，num+1在这里的意义是我继续从他后面开始找。就不找他前面的数了。避免重复
                backTracking(curr_lst, num+1)

                curr_lst.pop()

        if n < 1 or k < 1:
            return []
        res = []
        backTracking([], 1)
        return res
```