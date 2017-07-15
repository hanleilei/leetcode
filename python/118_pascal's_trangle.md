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

## 每一层的第i个位置，等于上一层第i-1与第i个位置之和，设定rowlist是每一层的数组，临时数组为上一层的数组首尾各加0，rowlist第i个值为临时数组第i和i+1之和 

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
