# Path Crossing

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

## Example 1

![](https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123929-pm.png)

```text
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
```

## Example 2

![](https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123843-pm.png)

```text
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
```

## Constraints

```text
1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
```

阅读理解。。每次经过一个位置，添加到visited里，就判断是否再次经过visited的位置。

```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        x, y = 0, 0
        orig = (0, 0)
        s.add(orig)
        
        for p in path:
            if p == "N":
                x, y = 0, 1
            elif p == "S":
                x, y = 0, -1
            elif p == "W":
                x, y = -1, 0
            else:
                x, y = 1, 0
            orig = (orig[0] + x, orig[1] + y)
            if orig in s:
                return True
            s.add(orig)
        return False
        
```

```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moves = {
            "N": (0, 1),
            "S": (0, -1),
            "W": (-1, 0),
            "E": (1, 0)
        }
        visited = {(0, 0)}
        x, y = 0, 0
        for c in path:
            dx, dy = moves[c]
            x += dx
            y += dy

            if (x, y) in visited:
                return True
            visited.add((x,y))
        return False
```

惭愧，什么时候python开始支持match case语法了？？？

```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        locations = {(0, 0)}
        x, y = 0, 0 
        for character in path: 
            match character: 
                case "N":
                    y += 1 
                case "E":
                    x += 1 
                case "W":
                    x -= 1 
                case "S":
                    y -=1 
            if (x, y) in locations: return True 
            locations.add((x, y) )
        return False 
```
