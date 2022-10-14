# daily Temperatures

Given a list of daily nns T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

## 绝妙的算法，原来可以用这样的方式遍历数组啊。。。之前还都是用 for i in range(size -1)，现在看来太土了

```python
class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = list()
        if not T:
            return list()

        n = len(T)

        if n == 1:
            return [0]

        res = [0] * n

        for i in range(n):
            while len(stack) and T[stack[-1]] < T[i]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res
```
