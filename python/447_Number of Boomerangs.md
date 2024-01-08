# Number of Boomerangs

You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

## Example 1

```text
Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
```

## Example 2

```text
Input: points = [[1,1],[2,2],[3,3]]
Output: 2
```

## Example 3

```text
Input: points = [[1,1]]
Output: 0
```

## Constraints

```text
n == points.length
1 <= n <= 500
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
```

来一个速度快的：

```python
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = 0
        for a, b in points:
            counter = dict()
            for x, y in points:
                key = (x - a) ** 2 + (y - b) ** 2
                if key in counter:
                    n += 2 * counter[key]
                    counter[key] += 1
                else:
                    counter[key] = 1
        return n
```

似乎，只有上面的这个O(n**2)的方法，没有其他更巧妙的方法了，又是一个阅读理解的问题。。。

我们写成这样更好理解，但是速度慢很多：

```python
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = 0
        for i in points:
            counter = defaultdict(int)
            for j in points:
                key = math.dist(i,j)
                n += 2 * counter[key]
                counter[key] += 1
        return n
```

这里用到了defaultdict的一个特性：访问不存在的key时，直接返回0。
