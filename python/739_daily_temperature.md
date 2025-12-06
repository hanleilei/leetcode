# daily Temperatures

[[stack]] [[monotonic stack]]

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

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100

单调栈的经典题目

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

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 用 单调递减栈 来优化查找
        n = len(temperatures)
        answer = [0] * n  # 初始化结果数组，全为 0
        stack = []
        # 遍历每一天  我们从左到右遍历气温，用一个栈存索引，
        # 栈中的索引对应的温度始终是按照递减的顺序保存。
        # 遇到一个新的温度，如果它比栈顶的温度高：
        # 说明这个新温度是栈顶那天的“下一个更高的温度”
        # 弹出栈顶索引，计算两者之间的距离，存到 answer 中
        # 把当前天的索引压栈，继续遍历
        for i, temp in enumerate(temperatures):
             # 如果当前温度比栈顶存的那天温度高
            while stack and temp > temperatures[stack[-1]]:
                # 栈顶那天的索引
                prev_index= stack.pop()
                # 当前温度是栈顶那天的下一个更高温度
                answer[prev_index] = i - prev_index  # 间隔天数
            # 当前天进栈
            stack.append(i)
        return answer
```

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 用 单调递减栈 来优化查找
        n = len(temperatures)
        res = [0] * n  # 初始化结果数组，全为 0
        s = []

        for i in range(n-1, -1, -1):
            while s and temperatures[s[-1]] <= temperatures[i]:
                s.pop()
            # 得到索引间距
            res[i] = 0 if not s else s[-1] - i
            # 将索引入栈，而不是元素
            s.append(i)
        return res
```
