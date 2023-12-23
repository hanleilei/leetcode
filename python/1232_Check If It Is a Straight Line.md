# Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

![](https://assets.leetcode.com/uploads/2019/10/15/untitled-diagram-2.jpg)

```comment
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
```

Example 2:
![](https://assets.leetcode.com/uploads/2019/10/09/untitled-diagram-1.jpg)

```comment
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
```

Constraints:

- 2 <= coordinates.length <= 1000
- coordinates[i].length == 2
- -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
- coordinates contains no duplicate point.

```Python
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(2,len(coordinates)):
            if coordinates[i][1] * (coordinates[1][0]-coordinates[0][0]) != coordinates[i][0]*(coordinates[1][1]-coordinates[0][1]) + coordinates[1][0]*coordinates[0][1]-coordinates[0][0]*coordinates[1][1]:
                return False
        return True
```

拆开写好像更容易理解一点：

```python
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        for i in range(1, n-1):
            dx1, dy1 = coordinates[i][0] - coordinates[i-1][0], coordinates[i][1] - coordinates[i-1][1]
            dx2, dy2 = coordinates[i+1][0] - coordinates[i][0], coordinates[i+1][1] - coordinates[i][1]
            if dx1 * dy2 != dy1 * dx2:
                return False
        return True
```
