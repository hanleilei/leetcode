# container with most water

[[greedy]] [[2points]]

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 10**5
0 <= height[i] <= 10**4

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
