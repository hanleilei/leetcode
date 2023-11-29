# Number of Ways to Divide a Long Corridor

[[dp]]

Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.

## Example 1

![](https://assets.leetcode.com/uploads/2021/12/04/1.png)

```text
Input: corridor = "SSPPSPS"
Output: 3
Explanation: There are 3 different ways to divide the corridor.
The black bars in the above image indicate the two room dividers already installed.
Note that in each of the ways, each section has exactly two seats.
```

## Example 2

![](https://assets.leetcode.com/uploads/2021/12/04/2.png)

```text
Input: corridor = "PPSPSP"
Output: 1
Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
Installing any would create some section that does not have exactly two seats.
```

## Example 3

![](https://assets.leetcode.com/uploads/2021/12/12/3.png)

```text
Input: corridor = "S"
Output: 0
Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.
```

## Constraints

```text
n == corridor.length
1 <= n <= 105
corridor[i] is either 'S' or 'P'.
```
from lee215

Assume a[i] is the index of ith seat,
there are a[i+1] - a[i] ways to put a divider between ith and i+1th seats.
We only needs to calculate the produit of all these a[i+1] - a[i].

If the number of seat is odd or is less than 2, then no way to divide the corridor.

Time O(n)
Space O(1)

```python
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7
        d = [i for i, c in enumerate(corridor) if c == "S"]
        res = 1
        for i in range(1, len(d) - 1, 2):
            res *= d[i+1] - d[i]
        return res % mod * (len(d)% 2 == 0 and len(d) >= 2)
```

a the number of 0 seat
b the number of 1 seat
c the number of 2 seats

Time O(n)
Space O(1)

```python
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        a, b, c = 1, 0, 0
        for ch in corridor:
            if ch == 'S':
                a, b, c = 0, a + c, b
            else:
                a, b, c = a + c, b, c
        return c % (10**9+7)  
```

再来一个速度最快的：

```python
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7
        left  = 0 
        mid   = 0
        right = 1  
        
        for item in corridor : 
            if item == "S" : 
                left = mid 
                mid, right = right, mid 
            else : 
                right = (right + left) % mod 
        
        return left 
```

