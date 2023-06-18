# equal row and column pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:

```
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
```
Example 2:

```
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
```

Constraints:

* n == grid.length == grid[i].length
* 1 <= n <= 200
* 1 <= grid[i][j] <= 105

我想出来的单行版本，直接上tuple的比较。速度还是不够快，估计是重复太多了。。
```python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = 0
        return len([c for i in [tuple(i) for i in map(list,zip(*grid))] for j in [tuple(k) for k in grid] if i == j])
```
还是这个快，字典就是不一样。
```python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = defaultdict(int)
        count = 0

        for row in grid:
            row_count[tuple(row)] += 1
        for column in zip(*grid):
            count += row_count[tuple(column)]
        return count
```