# Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

####### 重复上一题目的算法

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
