# Minimum Score Triangulation of Polygon


You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.

Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.

You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.

Return the minimum possible score that you can achieve with some triangulation of the polygon.

## Example 1

```text
Input: values = [1,2,3]

Output: 6

Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
```

## Example 2

```text
Input: values = [3,7,4,5]

Output: 144

Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.
```

## Example 3

```text
Input: values = [1,3,1,4,1,5]

Output: 13

Explanation: The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
```

## Constraints

```text
n == values.length
3 <= n <= 50
1 <= values[i] <= 100
```

```python
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        # dp[i][j] = 从 i 到 j 的最小三角剖分分数
        dp = [[0] * n for _ in range(n)]
        
        # L 表示子多边形的长度，从 3 开始（至少 3 个点才能成三角形）
        for L in range(3, n+1):
            for i in range(n - L + 1):  # 起点
                j = i + L - 1          # 终点
                best = float('inf')
                # 枚举中间点 k，选择最后一个三角形 (i, k, j)
                for k in range(i+1, j):
                    cost = dp[i][k] + dp[k][j] + values[i]*values[k]*values[j]
                    best = min(best, cost)
                dp[i][j] = best
        
        return dp[0][n-1]  # 整个多边形的最优解
```
