# Spiral matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

##Example:
```
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```
还是stefan大神的答案最吊。。(https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions)

```
||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
                 |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
                                     |8 7|      |7 6 5|
```


```python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
```

```python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + zip(*A[::-1])
        return A
```
