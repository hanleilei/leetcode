# hamming distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

#### 异或

```python
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
```

在来几个快点的：
```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = 0
        while x > 0 or y > 0:
            d += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1
        return d
```

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y
```

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0;
        while(x > 0 or  y>0):
            if(x%2 != y%2):
                count = count+1;
            x = x//2;
            y = y//2;
        return count
```
