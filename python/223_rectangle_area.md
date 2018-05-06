# rectangel area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
![](https://leetcode.com/static/images/problemset/rectangle_area.png)
## Example:
```
Input: -3, 0, 3, 4, 0, -1, 9, 2
Output: 45
```
## Note:
Assume that the total area is never beyond the maximum possible value of int.

```python
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        overlap = max(0, min(C, G)-max(A, E)) * max(0, min(D, H)-max(B, F))
        return (C-A)*(D-B)+(G-E)*(H-F)-overlap

```
