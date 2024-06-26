# trapping rain water

[[MonotonicStack]] [[stack]] [[2points]]

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![](http://www.leetcode.com/static/images/problemset/rainwatertrap.png)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

```python
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        解题思路：模拟法。开辟一个数组leftmosthigh，leftmosthigh[i]为A[i]之前的最高的bar值，然后从后面开始遍历，用rightmax来记录从后向前遍历遇到的最大bar值，那么min(leftmosthigh[i], rightmax)-A[i]就是在第i个bar可以储存的水量。例如当i=9时，此时leftmosthigh[9]=3,而rightmax=2，则储水量为2-1=1，依次类推即可。这种方法还是很巧妙的。时间复杂度为O(N)。
        """
        leftmostarr = [0] * len(height)
        lm = 0
        for i in range(len(height)):
            if height[i] > lm:
                lm = height[i]
            leftmostarr[i] = lm

        total = 0
        rightmax = 0
        for i in reversed(range(len(height))):
            if height[i] > rightmax:
                rightmax = height[i]
            if min(rightmax, leftmostarr[i]) > height[i]:
                total += min(rightmax, leftmostarr[i]) - height[i]
        return total


```

```Python
class Solution:
    def trap(self, A: List[int]) -> int:
        result = 0
        stack = []

        for i in range(len(A)):
            mid_height = 0
            while stack:
                [pos, height] = stack.pop()
                result += (min(height, A[i]) - mid_height) * (i - pos - 1)
                mid_height = height

                if A[i] < height:
                    stack.append([pos, height])
                    break
            stack.append([i, A[i]])

        return result
```

再来一个很巧妙的算法, 从两边向中间遍历:

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        lmax,rmax = 0,0
        res = 0
        while l<r:
            if height[l]<height[r]:
                lmax = max(lmax,height[l])
                res += lmax-height[l]
                l+=1
            else:
                rmax = max(rmax,height[r])
                res += rmax-height[r]
                r-=1
        return res
```

或者：

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        max_left, max_right = 0, 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    res += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right: 
                    max_right = height[right]
                else:
                    res += max_right - height[right]
                right -= 1
        return res
```
