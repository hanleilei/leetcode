# Maximum Building Height

You want to build n new buildings in a city. The new buildings will be built in a line and are labeled from 1 to n.

However, there are city restrictions on the heights of the new buildings:

    The height of each building must be a non-negative integer.
    The height of the first building must be 0.
    The height difference between any two adjacent buildings cannot exceed 1.

Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array restrictions where restrictions[i] = [idi, maxHeighti] indicates that building idi must have a height less than or equal to maxHeighti.

It is guaranteed that each building will appear at most once in restrictions, and building 1 will not be in restrictions.

Return the maximum possible height of the tallest building.

Example 1:

![](https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex1-1.png)

Input: n = 5, restrictions = [[2,1],[4,1]]
Output: 2
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.

Example 2:

![](https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex2.png)

Input: n = 6, restrictions = []
Output: 5
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of 5.

Example 3:

![](https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex3.png)

Input: n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
Output: 5
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3], and the tallest building has a height of 5.

Constraints:

    2 <= n <= 109
    0 <= restrictions.length <= min(n - 1, 105)
    2 <= idi <= n
    idi is unique.
    0 <= maxHeighti <= 109

```python
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions += [[1, 0], [n, inf]]
        restrictions.sort(key = lambda a: a[0])

        m = len(restrictions)
        h = [0] * m

        for i in range(1, m):
            h[i] = min(h[i-1] + restrictions[i][0] - restrictions[i - 1][0], restrictions[i][1])
        for i in range(m - 2, -1, -1):
            h[i] = min(h[i], h[i + 1] + restrictions[i + 1][0] - restrictions[i][0])
        return max(restrictions[i + 1][0] - restrictions[i][0] + h[i] + h[i + 1] for i in range(m - 1)) // 2
```

```python
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort(key=lambda i:i[0]+i[1])
        ans, b = 0, [1,0]
        for r in restrictions:
            ans = max(ans,(min(2*n-b[0]+b[1],r[0]+r[1])-(b[0]-b[1]))//2)
            if b[0]-b[1] < r[0]-r[1]: b = [r[0],r[1]]
        return max(ans,n-b[0]+b[1])
```

```python
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort(key = lambda x: x[0] + x[1])
        res = 0
        limit = 1
        for x, y in restrictions:
            li = x - y
            if limit < li :
                res = max(res, (x + y - limit) // 2)
                limit = li 
        return max(res, n - limit)
```
