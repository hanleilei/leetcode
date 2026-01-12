# maximal rectangle

[[MonotonicStack]] [[stack]]

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

```
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```

看注释，这个思路很赞。。

```python
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        // The problem can be convert to the problem - "Largest Rectangle in Histogram"
        //   1) we can take each row to calculate each row's histogram.
        //   2) using the algorithm of "Largest Rectangle in Histogram" to find the largest area histogram.
        //   3) tracking the maximal area.
        //
        // For the 1), it's easy.
        //     heights[i][j] = 1,                     if (i==0)
        //     heights[i][j] = heights[i-1][j] + 1;,  if (i>0)
        //
        // For the 2), please referr to "Largest Rectangle in Histogram"
        //
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans
```

再来一个超过100%的：

```python
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        nums, area = [int(''.join(row), base=2) for row in matrix], 0
        for i in range(len(nums)):
            num = -1
            for j in range(i, len(nums)):
                num &= nums[j]
                if not num: break
                n, l = num, 0
                while n:
                    l += 1
                    n &= n << 1
                area = max(area, l * (j - i + 1))
        return area
```
