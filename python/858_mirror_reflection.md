# mirror reflection

There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

 

Example 1:
```
![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/18/reflection.png)

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
```


Note:

1 <= p <= 1000
0 <= q <= p


```explanation
Divide p,q by 2 until at least one odd.

If p = odd, q = even: return 0
If p = even, q = odd: return 2
If p = odd, q = odd: return 1
I summary it as return 1 - p % 2 + q % 2
```

```python
class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        while p % 2 == 0 and q % 2 == 0: p, q = int(p / 2), int(q / 2)
        return int(1 - p % 2 + q % 2)

```
