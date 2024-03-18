# Minimum Number of Arrows to Burst Balloons

[[greedy]] [[interval overlapping]]

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:

- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:

- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:

1 <= points.length <= 105
points[i].length == 2
-231 <= xstart < xend <= 231 - 1

贪心，方法很妙：

```python
class Solution:
    def findMinArrowShots(self, points: 'List[List[int]]') -> 'int':
        points = sorted(points, key = lambda x: x[1])
        res, end = 0, -float('inf')
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
        return res
```

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res, shoot = 0, float('inf')
        for s, e in sorted(points, reverse=True):
            if shoot > e:
                shoot = s
                res += 1
        return res
```

有点奇怪的事情就是, 为什么下面的速度很快？

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])

        res, right = 0, float("-inf")

        for i in points:
            if i[0] > right:
                res += 1 
                right = i[1]

        return res
```
