# container with most water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Subscribe to see which companies asked this question.

有个高度数组，就相当于隔板的高度，求数组中任意两隔板间盛水的最大量。隔板间的距离与较低隔板的高度乘积即为盛水的容量。这个有点像是贪心法

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height) # the size of height
        maxm = 0 # record the most water
        j = 0
        k = size - 1
        while j < k:
            if height[j] <= height[k]:
                maxm = max(maxm,height[j] * (k - j))
                j += 1
            else:
                maxm = max(maxm,height[k] * (k - j))
                k -= 1
        return maxm
```

或者：

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end, res = 0, len(height) -1 , 0

        while start < end:
            area = min(height[end], height[start]) * (end - start)
            res = max(res, area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return res
```
