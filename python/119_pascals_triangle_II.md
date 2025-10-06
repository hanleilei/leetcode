# Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

```python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        tem=[0,1]
        l=[]
        for i in range(rowIndex+1):
            rowlist=[]
            for j in range(len(tem)-1):
                rowlist.append(tem[j]+tem[j+1])
            l.append(rowlist)
            tem=rowlist[:]
            tem.insert(0,0)
            tem.append(0)
        return  l[-1]

```

```Python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        for i in range(2,rowIndex+1):
            for j in range(i-1,0,-1):
                row[j] += row[j-1]
        return row

```

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
```

对上一个题目的小幅修改

```python
class Solution:
    def getRow(self, numRows: int) -> List[int]:
        if numRows == 0: return [1]
        res = [[1]]
        for i in range(numRows):
            temp = [0] + res[-1] + [0]
            t_list = list()
            for t in range(1, len(temp)):
                t_list.append(temp[t-1] + temp[t])
            res.append(t_list)
        return res[-1]
```

来一个复制很多次的方法：

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row  = [1]
        for _ in range(rowIndex):
            row = [0] + row + [0]
            row = [row[i] + row[i+ 1] for i in range(len(row)-1)]
        return row
```

同样思路，但是速度快很多：

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row  = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row
```

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                dp[j] += dp[j - 1]
        return dp
```

还可以用二项式公式来解决：

1. ​初始化​：第 rowIndex行的长度为 rowIndex + 1，且第一个数总是 1（即 C(n,0)=1）。
2. ​递推计算​：从第 1 个位置到第 rowIndex个位置，利用递推关系计算每个组合数：
$C(n,k)=C(n,k−1)× \frac{n - k + 1}{k}$
3. ​返回结果​：将计算出的组合数序列作为结果返回。

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)  # 初始化全为 1
        for k in range(1, rowIndex):
            # 递推计算 C(rowIndex, k)
            row[k] = row[k - 1] * (rowIndex - k + 1) // k
        return row
```
