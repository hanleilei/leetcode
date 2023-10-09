# Build Array Where You Can Find The Maximum Exactly K Comparisons

[[dp]] [[dfs]]

You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:

![](https://assets.leetcode.com/uploads/2020/04/02/e.png)

You should build the array arr which has the following properties:

- arr has exactly n integers.
- 1 <= arr[i] <= m where (0 <= i < n).

After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.

## Example 1

```text
Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
```

## Example 2

```text
Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisfy the mentioned conditions.
```

## Example 3

```text
Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
```

## Constraints

- `1 <= n <= 50`
- `1 <= m <= 100`
- `0 <= k <= n`

这是一个 DFS + DP的问题。。直接上 hiepit 的方案

TODO
这个一定要理解透彻才行

```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """Returns the number of valid arrays that can be built with the given constraints.

        Args:
            n: The length of the array.
            m: The maximum element that can be in the array.
            k: The maximum search cost.

        Returns:
            The number of valid arrays.
        """

        dp = [[[None for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
        return self.dfs(n, m, k, 0, 0, 0, dp)

    def dfs(self, n: int, m: int, k: int, i: int, curr_max: int, curr_cost: int, dp: list[list[list[int]]]) -> int:
        """Recursively calculates the number of valid arrays that can be built with the given constraints.

        Args:
            n: The length of the array.
            m: The maximum element that can be in the array.
            k: The maximum search cost.
            i: The current index in the array.
            curr_max: The maximum element in the array up to this point.
            curr_cost: The current search cost.
            dp: A memoization table to store the results of previous calculations.

        Returns:
            The number of valid arrays that can be built with the given constraints.
        """

        if i == n:
            return 1 if k == curr_cost else 0

        if dp[i][curr_max][curr_cost] is not None:
            return dp[i][curr_max][curr_cost]

        ans = 0
        # Case 1: num in range [1, curr_max], newMax = currMax, newCost = currCost
        ans += curr_max * self.dfs(n, m, k, i + 1, curr_max, curr_cost, dp) % 1_000_000_007

        # Case 2: num in range [currMax+1, m], newMax = num, newCost = currCost + 1
        if curr_cost + 1 <= k:
            for num in range(curr_max + 1, m + 1):
                ans += self.dfs(n, m, k, i + 1, num, curr_cost + 1, dp)
                ans %= 1_000_000_007

        dp[i][curr_max][curr_cost] = ans
        return ans
}
```

```python
class Solution:  
    def numOfArrays(self, n: int, m: int, k: int) -> int:  
        dp = [[[None]* (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]  
        return self.dfs(n, m, k, 0, 0, 0, dp)  
      
    def dfs(self, n: int, m: int, k: int, i: int, curr_max: int, curr_cost: int, dp: list) -> int:  
        if i == n:  
            if k == curr_cost: return 1  
            return 0  
        if dp[i][curr_max][curr_cost] is not None: return dp[i][curr_max][curr_cost]  
        ans = 0  
          
        # Case 1: num in range [1, currMax], newMax = currMax, newCost = currCost  
        ans += curr_max * self.dfs(n, m, k, i + 1, curr_max, curr_cost, dp) % 1_000_000_007  
  
        # Case 2: num in range [currMax+1, m], newMax = num, newCost = currCost + 1  
        if curr_cost + 1 <= k:  
            for num in range(curr_max + 1, m + 1):  
                ans += self.dfs(n, m, k, i + 1, num, curr_cost + 1, dp)  
                ans %= 1_000_000_007  
          
        dp[i][curr_max][curr_cost] = ans
        return ans
```