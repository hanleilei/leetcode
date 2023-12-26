# Minimum Garden Perimeter to Collect Enough Apples

[[binary search]]

In a garden represented as an infinite 2D grid, there is an apple tree planted at every integer coordinate. The apple tree planted at an integer coordinate (i, j) has |i| + |j| apples growing on it.

You will buy an axis-aligned square plot of land that is centered at (0, 0).

Given an integer neededApples, return the minimum perimeter of a plot such that at least neededApples apples are inside or on the perimeter of that plot.

The value of |x| is defined as:

x if x >= 0
-x if x < 0

## Example 1

![1](https://assets.leetcode.com/uploads/2019/08/30/1527_example_1_2.png)

```text
Input: neededApples = 1
Output: 8
Explanation: A square plot of side length 1 does not contain any apples.
However, a square plot of side length 2 has 12 apples inside (as depicted in the image above).
The perimeter is 2 * 4 = 8.
```

## Example 2

```text
Input: neededApples = 13
Output: 16
```

## Example 3

```text
Input: neededApples = 1000000000
Output: 5040
```

## Constraints

```text
1 <= neededApples <= 1015
```

来自 lee215：

Explanation
Assume the vertex is (r,r),(r,-r),(-r,r) and (-r,-r).
Split the apples into 4 rectangles,
each rectangle is r * (r + 1).

![](https://assets.leetcode.com/users/images/dc5d184f-3187-4036-962c-e54f58294a98_1627798845.9067092.png)


Put two blue matrix together
and merge apples tiles at the same position,
each tile become r + r + 1.
The total apples in blue is,
r * (r + 1) * (r + r + 1)

Put two green matrix together
and merge apples tiles at the same position,
each tile become r + r + 1.
The total apples in green is,
r * (r + 1) * (r + r + 1)

The total apples is:
r * r * r * 4 + r * r * 6 + r * 2.

Then we apply binary search.


Complexity
Time O(logX^(1/3)), where X is the range of input
Space O(1)

这都能想得到二分。。

```python
class Solution:
    def minimumPerimeter(self, x: int) -> int:
        l, r = 1, 1000000
        while l < r:
            b = (l + r) // 2
            if b * b * b * 4 + b * b * 6 + b * 2 >= x:
                r = b
            else:
                l = b + 1
        return l * 8
```

来一个速度最快的：

```python
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def calcnum(n):
            return n * (n + 1) * (4 * n + 2)
        
        left = 1
        right = 70000
        while left < right:
            mid = left + (right - left) // 2
            if calcnum(mid) >= neededApples:
                right = mid
            else:
                left = mid + 1
        return left * 8
```

再来一个O(1)的方法，有点黑魔法。。可怕

```python
class Solution:
    def minimumPerimeter(self, x: int) -> int:
        a = int((x * 2) ** (1 / 3.))
        a += a * (a + 1) * (a + 2) // 2 < x
        a += a % 2
        return a * 4
```
