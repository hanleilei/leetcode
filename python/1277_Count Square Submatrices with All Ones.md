# Count Square Submatrices with All Ones1277. Count Square Submatrices with All Ones

[[dp]]

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.  
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.

Constraints:

```text
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
```

```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        dp=[[0]*c for _ in range(r)]

        count=0

        for j in range(c):
            if(matrix[0][j]==1):
                dp[0][j]=1
                count+=1
        
        for i in range(1, r):
            if(matrix[i][0]==1):
                dp[i][0]=1
                count+=1

        for i in range(1, r):
            for j in range(1, c):
                if(matrix[i][j]==0):
                    continue
                # 下面的两个条件可以合并
                elif dp[i-1][j]==0 or dp[i-1][j-1]==0 or dp[i][j-1]==0:
                    dp[i][j]=1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                
                count+=dp[i][j]
        
        return count
```

或者

解释下面的代码：

```text
dp[i][j] means the size of biggest square with A[i][j] as bottom-right corner.
dp[i][j] also means the number of squares with A[i][j] as bottom-right corner.

If A[i][j] == 0, no possible square.
If A[i][j] == 1,
we compare the size of square dp[i-1][j-1], dp[i-1][j] and dp[i][j-1].
min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 is the maximum size of square that we can find.
```

```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        return sum(map(sum, matrix))
```

或者

```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                # 快速跳过0值
                if matrix[i][j] == 0:
                    continue
                    
                # 处理边界情况
                if i == 0 or j == 0:
                    res += matrix[i][j]
                    continue
                    
                # 只在所有相邻值都大于0时才计算
                if matrix[i-1][j] > 0 and matrix[i][j-1] > 0 and matrix[i-1][j-1] > 0:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                
                res += matrix[i][j]
        
        return res
```

这个题目很有趣，找正方形，如果只用动态规划的思路，可能会比较复杂。其实可以用一个简单的数学公式来解决这个问题。假设我们已经找到了以 (i, j) 为右下角的最大正方形边长为 k，那么以 (i, j) 为右下角的所有正方形的数量就是 1 + 2 + ... + k = k * (k + 1) / 2。这样我们就可以在 O(n) 的时间复杂度内计算出所有正方形的数量。
