# daily Temperatures

[[stack]]

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

 绝妙的算法，原来可以用这样的方式遍历数组啊。。。之前还都是用 for i in range(size -1)，现在看来太土了

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

单调栈问题

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans
```
