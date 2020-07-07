# arranging coins


You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:

¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

很简单的问题，不用考虑什么算法，就是一个数学问题而已：

```Python
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.sqrt(n * 2 + 0.25) - 0.5)

```


另一种思路:


```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + sqrt(1 + 8*n)) // 2)
```
