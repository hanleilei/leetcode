# Equal Sum Grid Partition I

[[prefixSum]]

You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

    Each of the two resulting sections formed by the cut is non-empty.
    The sum of the elements in both sections is equal.

Return true if such a partition exists; otherwise return false.

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:

![](https://assets.leetcode.com/uploads/2025/03/30/lc.jpeg)

A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

Example 2:

Input: grid = [[1,3],[2,4]]

Output: false

Explanation:

No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

Constraints:

    1 <= m == grid.length <= 10^5
    1 <= n == grid[i].length <= 10^5
    2 <= m * n <= 10^5
    1 <= grid[i][j] <= 10^5

自己的解法是构造前缀和矩阵，判断每行或每列的前缀和是否等于总和的一半。

```python
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return
        # 构造前缀和矩阵
        self.preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 计算每个矩阵 [0, 0, i, j] 的元素和
                self.preSum[i][j] = (self.preSum[i - 1][j] + self.preSum[i][j - 1] +
                                     grid[i - 1][j - 1] - self.preSum[i - 1][j - 1])
        
        for i in range(len(self.preSum)):
            if self.preSum[i][-1] * 2 == self.preSum[-1][-1]:
                return True
        for j in range(len(self.preSum[0])):
            if self.preSum[-1][j] * 2 == self.preSum[-1][-1]:
                return True
        return False
```

```python
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)

        # 能否水平分割
        def check(a: List[List[int]]) -> bool:
            s = 0
            for row in a[:-1]:  # 最后一行无需遍历
                s += sum(row)
                if s * 2 == total:
                    return True
            return False

        # 水平分割 or 垂直分割
        return check(grid) or check(list(zip(*grid)))
```

```python
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        s = sum(sum(row) for row in grid)
        n, m = len(grid), len(grid[0])
        pref = 0
        for row in grid:
            pref += sum(row)
            if s - pref == pref:
                return True
            if s - pref < pref:
                break
        pref = 0
        for j in range(m):
            for i in range(n):
                pref += grid[i][j]
            if s - pref == pref:
                return True
            if s - pref < pref:
                break
        return False
```

速度最快的：

```python
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

                # Sum rows of the grid or its transpose and 
                # determine whether the equal partition exists
        def partitionExists(arr: list, sm = 0)-> bool:

            for row in arr:
                sm+= sum(row)
                if sm == halfSum: return True
                if sm >  halfSum: return False


                # Determine the target sum for each partition
                # and whether sum(grid) is odd
        halfSum, mod_ = divmod(sum(chain(*grid)), 2)
        if mod_ : return False

                # Check horizontal and vertical partitions
        return (partitionExists(grid) or 
                partitionExists(zip(*grid)))   
```
