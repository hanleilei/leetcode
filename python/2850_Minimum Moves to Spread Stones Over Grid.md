# Minimum Moves to Spread Stones Over Grid

You are given a 0-indexed 2D integer matrix grid of size 3 * 3, representing the number of stones in each cell. The grid contains exactly 9 stones, and there can be multiple stones in a single cell.

In one move, you can move a single stone from its current cell to any other cell if the two cells share a side.

Return the minimum number of moves required to place one stone in each cell.

## Example 1

```text
Input: grid = [[1,1,0],[1,1,1],[1,2,1]]
Output: 3
Explanation: One possible sequence of moves to place one stone in each cell is: 
1- Move one stone from cell (2,1) to cell (2,2).
2- Move one stone from cell (2,2) to cell (1,2).
3- Move one stone from cell (1,2) to cell (0,2).
In total, it takes 3 moves to place one stone in each cell of the grid.
It can be shown that 3 is the minimum number of moves required to place one stone in each cell.
```

## Example 2

```text
Input: grid = [[1,3,0],[1,0,0],[1,0,3]]
Output: 4
Explanation: One possible sequence of moves to place one stone in each cell is:
1- Move one stone from cell (0,1) to cell (0,2).
2- Move one stone from cell (0,1) to cell (1,1).
3- Move one stone from cell (2,2) to cell (1,2).
4- Move one stone from cell (2,2) to cell (2,1).
In total, it takes 4 moves to place one stone in each cell of the grid.
It can be shown that 4 is the minimum number of moves required to place one stone in each cell.
```

## Constraints

- `grid.length == grid[i].length == 3`
- `0 <= grid[i][j] <= 9`
- Sum of grid is equal to 9.

有大佬指出，这个就是[匈牙利算法](https://zh.wikipedia.org/wiki/%E5%8C%88%E7%89%99%E5%88%A9%E7%AE%97%E6%B3%95)

## Intuition

Lets build all possible combinations and choose the best from them

## Approach

We need to construct arrays target with empty cells and stones with cells with free stones. If we have more than one free stone in the cell, each one will be in the array separately
Now we need to match each stone from the array with a cell from the second
Just going through all the combinations, since the grid is 3 by 3, there will be no more than 20 of them

## Complexity

Time complexity: O(n!)O(n!)O(n!)
Space complexity: O(n)O(n)O(n)

```python
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        targets = [(x, y) for x in range(3) for y in range(3) if grid[x][y] == 0]
        stones = []
        for x in range(3):
            for y in range(3):
                if grid[x][y] > 1:
                    stones.extend([(x, y)] * (grid[x][y] - 1))
        
        ways = []
        for targets_perm in permutations(targets):
            ways.append(list(zip(targets_perm, stones)))
        
        res = 100000
        for way in ways:
            cur = 0
            for cell1, cell2 in way:
                cur += abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])
            res = min(res, cur)
        
        return res
```
