# Uncrossed Lines

You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

## Example 1

![](https://assets.leetcode.com/uploads/2019/04/26/142.png)

```text
1   4    2
|    \
|      \
1   2    4
```

```text
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
```

## Example 2

```text
Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
```

## Example 3

```text
Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
```

## Constraints

- 1 <= nums1.length, nums2.length <= 500
- 1 <= nums1[i], nums2[j] <= 2000

这个题目和 edit distance 是一致的，直接上 dp

来看下 lee215 的方案：

1. Solution 1: Straight Forward 2D DP

```python
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp, m, n = collections.defaultdict(int), len(A), len(B)
        for i in range(m):
            for j in range(n):
                dp[i, j] = max(dp[i - 1, j - 1] + (A[i] == B[j]), dp[i - 1, j], dp[i, j - 1])
        return dp[m - 1, n - 1]
```

```cpp
    int maxUncrossedLines(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size(), dp[m+1][n+1];
        memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= m; ++i)
            for (int j = 1; j <= n; ++j)
                dp[i][j] = A[i - 1] == B[j - 1] ? dp[i - 1][j - 1] + 1 : max(dp[i][j - 1], dp[i - 1][j]);
        return dp[m][n];
    }
```

```java
    public int maxUncrossedLines(int[] A, int[] B) {
        int m = A.length, n = B.length, dp[][] = new int[m + 1][n + 1];
        for (int i = 1; i <= m; ++i)
            for (int j = 1; j <= n; ++j)
                if (A[i - 1] == B[j - 1])
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
        return dp[m][n];
    }
```

2. Solution 2: 1D DP

```java
     public int maxUncrossedLines(int[] A, int[] B) {
        int m = A.length, n = B.length;
        if (m < n) return maxUncrossedLines(B, A);

        int dp[] = new int[n+1];
        for (int i = 0; i < m; i++) {
            for (int j = 0, prev = 0, cur; j < n; j++) {
                cur = dp[j+1];
                if (A[i] == B[j]) dp[j+1] = 1+prev;
                else dp[j+1] = Math.max(dp[j+1], dp[j]);
                prev = cur;
            }
        }
        return dp[n];
    }
```

```python
    def maxUncrossedLines(self, A, B):
        m, n = len(A), len(B)
        dp = [0] * (n + 1)
        for i in xrange(m):
            for j in range(n)[::-1]:
                if A[i] == B[j]: dp[j + 1] = dp[j] + 1
            for j in range(n):
                dp[j + 1] = max(dp[j + 1], dp[j])
        return dp[n]
```

最后，来一个速度最快的：

```python
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)
        dp = [0] * n
        res = 0
        for t in nums2:
            cnt = 0
            for i in range(n):
                if cnt < dp[i]:
                    cnt = dp[i]
                elif t == nums1[i]:
                    dp[i] = cnt + 1
                    res = max(res, dp[i])
        return res
```
