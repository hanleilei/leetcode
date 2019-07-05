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
注意else branch中的i-2。

再来一个简化, python简直了。。
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

每一层的第i个位置，等于上一层第i-1与第i个位置之和，设定rowlist是每一层的数组，临时数组为上一层的数组首尾各加0，rowlist第i个值为临时数组第i和i+1之和

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
Python 2 的 map版本：

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
1. 首先理解map操作，这样的写法：
```python
map(lambda x, y: arr1, arr2)
```
这将会把arr1中的全部元素和arr2中的全部元素相加，即返回：[arr1[0]+ arr2[0], arr1[1]+ arr2[1]....] 选取arr1和arr2中最短的那个数组长度。

2. 所谓杨辉三角的算法也就是上一行的数据，错位相加，不足的地方补零。即
res[-1] + [0], [0] + res[-1] 这种实现。
