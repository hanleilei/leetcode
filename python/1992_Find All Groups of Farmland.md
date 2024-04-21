# Find All Groups of Farmland

[[dfs]]

You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.

## Example 1

![1](https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-23-15-copy-of-diagram-drawio-diagrams-net.png)

```text
Input: land = [[1,0,0],[0,1,1],[0,1,1]]
Output: [[0,0,0,0],[1,1,2,2]]
Explanation:
The first group has a top left corner at land[0][0] and a bottom right corner at land[0][0].
The second group has a top left corner at land[1][1] and a bottom right corner at land[2][2].
```

## Example 2

![2](*https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-30-26-copy-of-diagram-drawio-diagrams-net.png)

```text
Input: land = [[1,1],[1,1]]
Output: [[0,0,1,1]]
Explanation:
The first group has a top left corner at land[0][0] and a bottom right corner at land[1][1].
```

## Example 3

![3](https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-32-24-copy-of-diagram-drawio-diagrams-net.png)

```text
Input: land = [[0]]
Output: []
Explanation:
There are no groups of farmland.
```

## Constraints

```python
m == land.length
n == land[i].length
1 <= m, n <= 300
land consists of only 0's and 1's.
Groups of farmland are rectangular in shape.
```

来一个有点难懂的DFS：

```python
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        group = list()
        m, n = len(land), len(land[0])

        def dfs(row: int, col: int) -> (int, int):
            if row >=m or col >= n or land[row][col] == 0: return [0, 0]
            land[row][col] = 0

            h_r1, h_c1 = dfs(row + 1, col)
            h_r2, h_c2 = dfs(row, col + 1)
            h_r = max(h_r1, h_r2, row)
            h_c = max(h_c1, h_c2, col)
            
            return (h_r, h_c)
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    x, y = dfs(i, j)
                    group.append([i, j, x, y])
                    
        return group
```

Initialize an empty list result to store the coordinates of the top-left and bottom-right corners of each group of farmland.
Traverse the 2D matrix land using two nested loops.
For each cell in land, if the cell contains farmland (value = 1), call the findFarmlandCoordinates method to find the coordinates of the farmland group.
Inside the findFarmlandCoordinates method, start with the current cell and traverse down and right to find the bottom-right corner of the farmland group.
While traversing down and right, mark all visited cells as 0 to avoid revisiting them.
Return the coordinates of the top-left and bottom-right corners of the farmland group.
Add the coordinates to the result list.
After traversing the entire land, return the result list.

1. 初始化一个空列表结果，用于存储每组农田左上角和右下角的坐标。
2. 使用两个嵌套循环遍历二维矩阵 land。
3. 对land中的每个单元格，如果该单元格包含农田（值 = 1），则调用 dfs 方法查找农田组的坐标。
4. 在 dfs 方法中，从当前单元格开始向下和向右遍历，找到农田组的右下角。
5. 向下和向右遍历时，将所有访问过的单元格标记为 0，以避免再次访问。
6. 返回农田组左上角和右下角的坐标。
7. 将坐标添加到结果列表中。
8. 遍历整个land后，返回结果列表。

```python
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(land), len(land[0])
        
        def dfs(row, col):
            coordinates = [row, col]
            r, c = row, col
            
            while r < m and land[r][col] == 1:
                r += 1
            while c < n and land[row][c] == 1:
                c += 1
            
            coordinates.extend([r - 1, c - 1])
            
            for i in range(row, r):
                for j in range(col, c):
                    land[i][j] = 0
            
            return coordinates
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    res.append(dfs(i, j))
        
        return res
```

先找左上角，找到后找当前land的右下角，很多重复计算。

```python
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m=len(land)
        n=len(land[0])
        res=[]
        for i in range(m):
            for j in range(n):
                if land[i][j]==1 and (i==0 or land[i-1][j]==0) and (j==0 or land[i][j-1]==0):
                    x,y=i,j
                    while y+1<n and land[x][y+1]==1:y+=1
                    while x+1<m and land[x+1][y]==1:x+=1
                    res.append([i,j,x,y])
        return res
```

缩少一下计算量：

```python
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m=len(land)
        n=len(land[0])
        res=[]
        ones = [(x,y) for x in range(m) for y in range(n) if land[x][y] == 1]

        for i, j in ones:
            if (i==0 or land[i-1][j]==0) and (j==0 or land[i][j-1]==0):
                x,y=i,j
                while y+1<n and land[x][y+1]==1:y+=1
                while x+1<m and land[x+1][y]==1:x+=1
                res.append([i,j,x,y])
        return res
```

这么看来，DFS还是蛮套路的，找到一个点持续向下和向右遍历，直到找到边界，然后返回结果。