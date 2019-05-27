# max points in a line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

### Example 1:
```
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
```

### Example 2:

```
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
```

必须只能用gcd的方法，否则这个case：[[0,0],[94911151,94911150],[94911152,94911151]] 根本不行，达不到精度。


```python
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
class Solution(object):
    def maxPoints(self, points):
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'i': 1}
            same = 0
            for j in range(i+1, l):
                tx, ty = points[j][0], points[j][1]
                if tx == points[i][0] and ty == points[i][1]:
                    same += 1
                    continue
                if points[i][0] == tx:
                    slope = 'i'
                else:
                    num = (points[i][1] - ty)
                    dem = (points[i][0] - tx)
                    gcd = self.get_gcd(num, dem)
                    slope = (num / gcd, dem / gcd)
                    # slope = (points[i].y-ty) * 1.0 /(points[i].x-tx)
                if slope not in dic: dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m

    def get_gcd(self, num, den):
        while den:
            num, den = den, num % den
        return num

```

小改一下就超过96%的提交：

```python
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
class Solution(object):
    def maxPoints(self, points):
        if not points:
            return 0

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        ans = 0
        cnts = collections.Counter(map(tuple, points))

        while cnts:
            (x, y), cnt = cnts.popitem()
            ans = max(ans, cnt)

            if cnts:
                slopes = collections.defaultdict(lambda: cnt)

                for (_x, _y), _cnt in cnts.items():
                    dx = _x - x
                    dy = _y - y
                    d = gcd(dx, dy)
                    slopes[dx // d, dy // d] += _cnt

                ans = max(ans, max(slopes.values()))

        return ans
```
