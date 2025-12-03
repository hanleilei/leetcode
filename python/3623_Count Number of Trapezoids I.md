# Count Number of Trapezoids I

You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3

Explanation:

![Desmos Graph 6 image](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-6.png)

There are three distinct ways to pick four points that form a horizontal trapezoid:

Using points [1,0], [2,0], [3,2], and [2,2].
Using points [2,0], [3,0], [3,2], and [2,2].
Using points [1,0], [3,0], [3,2], and [2,2].
Example 2:

Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:

![Desmos Graph 5 image](https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-5.png)

There is only one horizontal trapezoid that can be formed.

Constraints:

4 <= points.length <= 10^5
–108 <= xi, yi <= 10^8
All points are pairwise distinct.

```python
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        ans = s = 0
        count = Counter(p[1] for p in points)
        for c in count.values():
            k = c * (c - 1) // 2
            ans += s * k
            s += k
        return ans % mod
```

```cpp
class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        const int mod = 1000000007;

        unordered_map<int, int> count;
        for (const auto& p: points){
            count[p[1]]++;
        }
        long long ans = 0;
        long long s = 0;

        for (const auto& [_, c]: count){
            long long k = (long long)c * (c - 1) / 2;
            ans = (ans + s * k);
            s = (s + k);
        }
        return ans % mod;
    }
};
```

## Explanation

1. **Count Points by Y-Coordinate**: We use a `Counter` to count how many points share the same y-coordinate. This helps us identify potential horizontal sides of trapezoids.
2. **Calculate Combinations**: For each unique y-coordinate with `c` points, we calculate the number of ways to choose 2 points (which form a horizontal side) using the combination formula `C(c, 2) = c * (c - 1) / 2`.
3. **Accumulate Results**: We maintain a running sum `s` of all previously calculated combinations. For each new combination `k`, the number of new trapezoids that can be formed with previously counted combinations is `s * k`. We add this to our answer `ans`.
4. **Modulo Operation**: Since the result can be very large, we return the answer modulo `10^9 + 7`.

time complexity: O(n), where n is the number of points, as we traverse the list of points and the unique y-coordinates once.
space complexity: O(m), where m is the number of unique y-coordinates, due to the storage in the Counter.
