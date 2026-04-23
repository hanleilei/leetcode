# Two Furthest Houses With Different Colors

There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

Example 1:

Input: colors = [1,1,1,6,1,1,1]
Output: 3
Explanation: In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.

Example 2:

Input: colors = [1,8,3,8,3]
Output: 4
Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
The furthest two houses with different colors are house 0 and house 4.
House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.

Example 3:

Input: colors = [0,1]
Output: 1
Explanation: The furthest two houses with different colors are house 0 and house 1.
House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.

Constraints:

    n == colors.length
    2 <= n <= 100
    0 <= colors[i] <= 100
    Test data are generated such that at least two houses have different colors.

完全脑筋急转弯啊，只要两端颜色不同，答案就是 n - 1，否则就从两端往中间找第一个不同颜色的房子，计算距离即可。

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        c = colors[0]
        if c != colors[-1]:
            return n - 1
        
        r = n - 2
        while colors[r] == c:
            r -= 1
        l = 1
        while colors[l] == c:
            l += 1
        return max(r, n - 1 - l)
```

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        for i in range(n):
            if colors[0] != colors[-i]:
                return n - i
            if colors[-1] != colors[i]:
                return n - 1 - i
```
