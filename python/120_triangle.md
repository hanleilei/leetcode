# triangle

[[dp]]

## Problem Description

Given a `triangle` array, return *the minimum path sum from top to bottom*.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

**Example 1:**

**Input:** triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
**Output:** 11
**Explanation:** The triangle looks like:
```
   2
  3 4
 6 5 7
4 1 8 3
```
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

**Example 2:**

**Input:** triangle = [[-10]]
**Output:** -10

**Constraints:**

- `1 <= triangle.length <= 200`
- `triangle[0].length == 1`
- `triangle[i].length == triangle[i - 1].length + 1`
- `-10^4 <= triangle[i][j] <= 10^4`

**Follow up:** Could you do this using only `O(n)` extra space, where `n` is the total number of rows in the triangle?

### Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

还是直接上这个讨论吧：https://leetcode.com/problems/triangle/discuss/38730/DP-Solution-for-Triangle

This problem is quite well-formed in my opinion. The triangle has a tree-like structure, which would lead people to think about traversal algorithms such as DFS. However, if you look closely, you would notice that the adjacent nodes always share a 'branch'. In other word, there are overlapping subproblems. Also, suppose x and y are 'children' of k. Once minimum paths from x and y to the bottom are known, the minimum path starting from k can be decided in O(1), that is optimal substructure. Therefore, dynamic programming would be the best solution to this problem in terms of time complexity.

What I like about this problem even more is that the difference between 'top-down' and 'bottom-up' DP can be 'literally' pictured in the input triangle. For 'top-down' DP, starting from the node on the very top, we recursively find the minimum path sum of each node. When a path sum is calculated, we store it in an array (memoization); the next time we need to calculate the path sum of the same node, just retrieve it from the array. However, you will need a cache that is at least the same size as the input triangle itself to store the pathsum, which takes O(N^2) space. With some clever thinking, it might be possible to release some of the memory that will never be used after a particular point, but the order of the nodes being processed is not straightforwardly seen in a recursive solution, so deciding which part of the cache to discard can be a hard job.

'Bottom-up' DP, on the other hand, is very straightforward: we start from the nodes on the bottom row; the min pathsums for these nodes are the values of the nodes themselves. From there, the min pathsum at the ith node on the kth row would be the lesser of the pathsums of its two children plus the value of itself, i.e.:

```
minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
```

Or even better, since the row minpath[k+1] would be useless after minpath[k] is computed, we can simply set minpath as a 1D array, and iteratively update itself:

For the kth level:

```
minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i];
```

Thus, we have the following solution：

## Solution Approaches

### Approach 1: Bottom-Up DP with O(n) Space (Optimal)

**Key Insight:** 
- Start from the bottom row and work upwards
- Each position's minimum path = min(two children below) + current value
- Can reuse a 1D array since we only need the previous row

**State Transition:**
```
dp[i] = min(dp[i], dp[i+1]) + triangle[row][i]
```

**Time Complexity:** O(n²) where n is the number of rows
**Space Complexity:** O(n) - only one row of DP array

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Initialize dp array with bottom row
        dp = triangle[-1][:]
        
        # Iterate from second-to-last row to top
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Current min path = current value + min of two children below
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        
        return dp[0]
```

### Approach 2: Bottom-Up DP (Reverse Iteration)

**Alternative implementation** using reverse iteration through the triangle:

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        
        # Process triangle from bottom to top
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = min(dp[i], dp[i + 1]) + n
        
        return dp[0]
```

### Approach 3: Top-Down DP with Memoization

**Key Insight:**
- Use DFS with memoization to avoid recalculating subproblems
- Recursively find minimum path from each position

**Time Complexity:** O(n²)
**Space Complexity:** O(n²) for memo array + O(n) recursion stack

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Create memoization array
        memo = [[None] * len(row) for row in triangle]
        
        def dfs(row: int, col: int) -> int:
            # Base case: reached bottom of triangle
            if row == len(triangle):
                return 0
            
            # Return memoized result if available
            if memo[row][col] is not None:
                return memo[row][col]
            
            # Calculate minimum path: current value + min of two paths below
            memo[row][col] = triangle[row][col] + min(
                dfs(row + 1, col),
                dfs(row + 1, col + 1)
            )
            
            return memo[row][col]
        
        return dfs(0, 0)
```

### Approach 4: In-Place Modification (Space-Optimized)

**Warning:** Modifies input array

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from second-to-last row
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update current cell with minimum path
                triangle[row][col] += min(
                    triangle[row + 1][col],
                    triangle[row + 1][col + 1]
                )
        
        return triangle[0][0]
```

---

## Key Takeaways

1. **Bottom-up DP is more intuitive** for this problem than top-down
2. **Space optimization**: Only need to track one row at a time (O(n) space)
3. **Overlapping subproblems**: Adjacent nodes share branches, perfect for DP
4. **Optimal substructure**: Minimum path through parent = parent value + min(children paths)

## Related Problems

- LeetCode 64: Minimum Path Sum
- LeetCode 931: Minimum Falling Path Sum

```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<int> mini = triangle[triangle.size() - 1];
        for (int i = triangle.size() - 2; i >= 0; --i){
            for (int j = 0; j < triangle[i].size(); ++j){
                mini[j] = triangle[i][j] + min(mini[j], mini[j + 1]);
            }
        }
        return mini[0];
    }
};
```