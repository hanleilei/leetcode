# trapping rain water

[[MonotonicStack]] [[stack]] [[2points]]

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

## Example 1

![Rainwatertrap image](http://www.leetcode.com/static/images/problemset/rainwatertrap.png)

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

## Example 2

Input: height = [4,2,0,3,2,5]
Output: 9

## Constraints

n == height.length
1 <= n <= 2 * 10**4
0 <= height[i] <= 10**5

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

再来一个很巧妙的算法, 从两边向中间遍历，也就是相向双指针：

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

再来一个前缀和+后缀和的方法：

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])

        suf_max = [0] * n
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])

        res = 0
        for h, p, s in zip(height, pre_max, suf_max):
            res += min(p, s) - h
        return res
```

再来一个：

思路：

1. 先找到最高点，无所谓哪一个。
2. 最左指针，往最高点走，记录最大值，并且如果最大值大于当前值，累加最大值与当前值的差。
3. 最右指针，后面同理

```python
class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        highest = h.index(max(h))
        res = 0
        lmax, rmax = h[0], h[n-1]
        for i in range(highest):
            # lmax = max(lmax, h[i])
            if lmax < h[i]:
                lmax = h[i]

            res += lmax - h[i]
        for i in range(n-2, highest, -1):
            # rmax = max(rmax, h[i])
            if rmax < h[i]:
                rmax = h[i]

            res += rmax - h[i]
        return res
```

再来一个自底向上计算的单调栈方法：

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        for i, h in enumerate(height):
            while stack and h >= height[stack[-1]]:
                bottom_h = height[stack.pop()]
                if len(stack) == 0:
                    break

                left = stack[-1]
                dh = min(height[left], h) - bottom_h
                ans += dh * (i - left - 1)
            stack.append(i)
        return ans
```
