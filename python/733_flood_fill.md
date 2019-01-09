# flood fill

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
```
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
```
## Note:

1. The length of image and image[0] will be in the range [1, 50].
2. The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
3. The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

dfs版本：

```python
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        s = {(i, j) for i, row in enumerate(image) for j, col in enumerate(row) if col == image[sr][sc]}

        queue = [(sr, sc)]

        while queue:
            i, j = queue.pop()
            image[i][j] = newColor
            for item in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if item in s:
                    s.remove(item)
                    queue.append(item)
                    r, c = item
                    image[r][c] = newColor

        return image
```
