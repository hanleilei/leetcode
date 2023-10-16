# Pascal's angle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]
Subscribe to see which companies asked this question

先更具下面的总结，上一个自制的算法：

```Python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        for i in range(1, numRows+1):
            level = list()
            for j in range(i):
                if j == 0 or j == i - 1:
                    level.append(1)
                else:
                    level.append(res[i-2][j-1] + res[i-2][j])
            res.append(level)
        return res
```

注意 else branch 中的 i-2。

如果觉得上面 -2 的方法有点诡异，那么这个方法更容易理解：对于数组直接构造一个[0] + res[-1] + [0] 临时数组：

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        res = [[1]]
        for i in range(numRows -1):
            temp = [0] + res[-1] + [0]
            t_list = list()
            for t in range(1, len(temp)):
                t_list.append(temp[t-1] + temp[t])
            res.append(t_list)
        return res
```

再来一个简化, python 简直了。。

```Python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        for i in range(1, numRows+1):
            level = [1 if j == 0 or j == i - 1 else res[i-2][j-1] + res[i-2][j] for j in range(i)]
            res.append(level)
        return res
```

换个角度，设想其为一个二维数组，满足这样的公式：res[i][j] = res[i-1][j-1] + res[i-1][j]

```Python
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [None] * numRows
        for i in range(numRows):
            res[i] = [None] * (i+1)
            res[i][0] = res[i][i] = 1
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
```

或者：

```Python
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            now = [1]*(i+1)
            if i >= 2:
                for n in range(1,i):
                    now[n] = pre[n-1]+pre[n]
            result += [now]
            pre = now
        return result
```

每一层的第 i 个位置，等于上一层第 i-1 与第 i 个位置之和，设定 rowlist 是每一层的数组，临时数组为上一层的数组首尾各加 0，rowlist 第 i 个值为临时数组第 i 和 i+1 之和

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        tem=[0,1]
        l=[]
        for i in range(numRows):
            rowlist=[]
            for j in range(len(tem)-1):
                rowlist.append(tem[j]+tem[j+1])
            l.append(rowlist)
            tem=rowlist[:]
            tem.insert(0,0)
            tem.append(0)
        return  l

```

Python 2 的 map 版本：

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]

```

这个办法非常的巧妙：

1. 首先理解 map 操作，这样的写法：

```python
map(lambda x, y: arr1, arr2)
```

这将会把 arr1 中的全部元素和 arr2 中的全部元素相加，即返回：[arr1[0]+ arr2[0], arr1[1]+ arr2[1]....] 选取 arr1 和 arr2 中最短的那个数组长度。

2. 所谓杨辉三角的算法也就是上一行的数据，错位相加，不足的地方补零。即
   res[-1] + [0], [0] + res[-1] 这种实现。

由于 Python3 中，map 返回的不再是 list 类型，而是 map 对象类型，需要强制转换一下：

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]
```

来一个更简洁的：

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row  = [1]
        res = list()
        res.append(row)
        for _ in range(numRows-1):
            row = [0] + row + [0]
            row = [row[i] + row[i+ 1] for i in range(len(row)-1)]
            res.append(row)
        return res
```
