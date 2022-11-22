# Nearest Exit from Entrance in Maze

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:

```
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].

- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
  It is impossible to reach [2,3] from the entrance.
  Thus, the nearest exit is [0,2], which is 1 step away.
```

Example 2:

```

Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].

- You can reach [1,2] by moving 2 steps right.
  Thus, the nearest exit is [1,2], which is 2 steps away.

```

Example 3:

```

Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.

```

Constraints:

```

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.

```

```python
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        q = deque([entrance])

        ### Using extra space to keep track of the visited positions.
        visited = {tuple(entrance)}

        ### Use steps to keep track of the level of the BFS.
        steps = 0
        while q:

            ### Since we are tracking the steps using a variable,
            ### we need to pop all elements at each level, then increase the steps.
            for _ in range(len(q)):
                xo,yo = q.popleft()
                if (0 in [xo,yo] or xo==m-1 or yo==n-1) and [xo,yo]!=entrance:
                    return steps
                for xn,yn in directions:
                    x,y = xo+xn,yo+yn
                    ### Check if the new position has been visited or not., and only go into the unvisited ones.
                    if 0<=x<m and 0<=y<n and maze[x][y]=='.' and (x,y) not in visited:
                        visited.add((x,y))
                        q.append([x,y])
            ### Increase the steps since we finished one level.
            steps += 1

        return -1
```

```python
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ### Get the maze size, used later to check whether the neighbor is valid.
        m,n = len(maze),len(maze[0])

        ### The directions that we can go at each position.
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        ### We use deque to make the pop more efficient
        ### We also have the steps stored at each position, and at any time, if we see an exit, we simply return the steps.
        ### Note that if you don't put the steps along with the positions, you will need to keep track of the levels you are at during the search (see style2).
        q = deque([[entrance[0],entrance[1],0]])

        ### We don't need to use extra space to store the visited positions,
        ### since we can directly change the empty position in the maze to a wall.
        maze[entrance[0]][entrance[1]] = '+'

        ### Doing a regular BFS search using deque; if there is anything left in the q, we will keep doing the search
        while q:
            ### Pop form left of the q,
            ### Since we have steps stored at each position, we don't need to make a loop here (see style2 for the loop version).
            xo,yo,steps = q.popleft()

            ### Check if the current location is an exit, and make sure it is not the entrance.
            if (0 in [xo,yo] or xo==m-1 or yo==n-1) and [xo,yo]!=entrance:
                return steps

            ### We go in four directions.
            for xn,yn in directions:
                x,y = xo+xn,yo+yn
                ### Make sure the new location is still inside the maze and empty.
                if 0<=x<m and 0<=y<n and maze[x][y]=='.':
                    ### We make the empty space into a wall, so we don't visit it in the future.
                    maze[x][y] = '+'
                    ### We need to increase the steps.
                    q.append([x,y,steps+1])

        ### If we don't find the result in BFS, we need to return -1
        return -1
```
